# This functionality provides mechanism for students to ask and answer questions
# Students and instructors can choose ask and answer questions anonymously or have their names displayed
from discord import NotFound
from discord.ext import commands
import db
import re


class Qanda(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: askQuestion(self, ctx, qs: str, anonymous)
    #    Description: takes question from user and reposts anonymously and numbered
    #    Inputs:
    #       - ctx: context of the command
    #       - qs: question text
    #       - anonymous: option if user wants their question to be shown anonymously
    #    Outputs:
    #       - User question in new post
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='ask', help='Ask question. Please put question text in quotes. Add *anonymous* if desired.'
                                       'EX: $ask /"When is the exam?/" anonymous')
    async def askQuestion(self, ctx, qs: str, anonymous=''):

        # make sure to check that this is actually being asked in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please send questions to the #q-and-a channel.')
            await ctx.message.delete()
            return

        # get author
        if anonymous == '':
            author = ctx.message.author.id
        elif anonymous == 'anonymous':
            author = None
        else:
            await ctx.author.send('Unknown input for *anonymous* option. Please type **anonymous** or leave blank.')
            await ctx.message.delete()
            return

        # get number of questions + 1
        num = db.query('SELECT COUNT(*) FROM questions WHERE guild_id = %s', (ctx.guild.id,))[0][0] + 1

        # format question
        author_str = 'anonymous' if author is None else (await self.bot.fetch_user(author)).name
        q_str = f"Q{num}: {qs} by {author_str}"

        message = await ctx.send(q_str)

        # add to db
        db.query(
            'INSERT INTO questions (guild_id, number, question, author_id, msg_id) VALUES (%s, %s, %s, %s, %s)',
            (ctx.guild.id, num, qs, author, message.id)
        )

        # delete original question
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: ask_error(self, ctx, error)
    #    Description: prints error message for ask command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @askQuestion.error
    async def ask_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the ask command, do: $ask \"QUESTION\" anonymous*<optional>* \n '
                '(For example: $ask \"What class is this?\" anonymous)')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    # Function: answer
    # Description: adds user answer to specific question and post anonymously
    # Inputs:
    #      - ctx: context of the command
    #      - num: question number being answered
    #      - ans: answer text to question specified in num
    #      - anonymous: option if user wants their question to be shown anonymously
    # Outputs:
    #      - User answer added to question post
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='answer',
                      help='Answer question. Please put answer text in quotes. Add *anonymous* if desired.'
                           'EX: $answer 1 /"Oct 12/" anonymous')
    async def answer(self, ctx, num, ans, anonymous=''):
        ''' answer the specific question '''
        # make sure to check that this is actually being asked in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please send answers to the #q-and-a channel.')
            await ctx.message.delete()
            return

        # to stop SQL from freezing. Only allows valid numbers.
        if not re.match(r'^([1-9]\d*|0)$', num):
            await ctx.author.send('Please include a valid question number. EX: $answer 1 /"Oct 12/" anonymous')
            await ctx.message.delete()
            return

        #if not isinstance(ans, str):
            #await ctx.author.send('Please include a valid answer. EX: $answer 1 /"Oct 12/" anonymous')
           # await ctx.message.delete()
           # return

        # get author
        if anonymous == '':
            author = ctx.message.author.id
        elif anonymous == 'anonymous':
            author = None
        else:
            await ctx.author.send('Unknown input for *anonymous* option. Please type **anonymous** or leave blank.')
            await ctx.message.delete()
            return

        # check if question number exists
        q = db.query('SELECT number, question, author_id, msg_id FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('Invalid question number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return
        q = q[0]

        # check if message exists
        try:
            message = await ctx.fetch_message(q[3])
        except NotFound:
            await ctx.author.send('Invalid question number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        # add answer to db
        if "instructor" in [y.name.lower() for y in ctx.author.roles]:
            role = 'Instructor'
        else:
            role = 'Student'
        db.query(
            'INSERT INTO answers (guild_id, q_number, answer, author_id, author_role) VALUES (%s, %s, %s, %s, %s)',
            (ctx.guild.id, num, ans, author, role)
        )

        # generate and edit msg with answer
        q_author_str = 'anonymous' if q[2] is None else (await self.bot.fetch_user(q[2])).name
        new_answer = f"Q{q[0]}: {q[1]} by {q_author_str}\n"

        # get all answers for question and add to msg
        answers = db.query('SELECT answer, author_id, author_role FROM answers WHERE guild_id = %s AND q_number = %s',
                           (ctx.guild.id, num))
        for answer, author, role in answers:
            a_author = 'anonymous' if author is None else (await self.bot.fetch_user(author)).name
            new_answer += f"{a_author} ({role}) Ans: {answer}\n"

        # edit message
        try:
            await message.edit(content=new_answer)
        except NotFound:
            await ctx.author.send('Invalid question number: ' + str(num))

        # delete user msg
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: answer_error(self, ctx, error)
    #    Description: prints error message for answer command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @answer.error
    async def answer_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the answer command, do: $answer QUESTION_NUMBER \"ANSWER\" anonymous*<optional>*\n '
                '(For example: $answer 2 \"Yes\")')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteAllAnswersFor
    #    Description: Deletes all answers for a question. Instructor only.
    #    Inputs:
    #       - ctx: context of the command
    #       - num: question number
    #    Outputs:
    #       -
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='DALLAF', help='(PLACEHOLDER NAME) Delete all answers for a question.\n'
                                    'EX: $DALLAF 1\n'
                                    'THIS ACTION IS IRREVERSIBLE.\n'
                                    'Before deletion, archive the question and its answers with\n'
                                    '$getAnswersFor QUESTION_NUMBER'
                                    )
    async def deleteAllAnsFor(self, ctx, num):

        # make sure to check that this is actually being asked in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # to stop SQL from freezing. Only allows valid numbers.
        if not re.match(r'^([1-9]\d*|0)$', num):
            await ctx.author.send('Please include a valid question number. EX: $DALLAF 1')
            await ctx.message.delete()
            return

        # check if question number exists
        q = db.query('SELECT number, question, author_id, msg_id FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('Invalid question number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return
        q = q[0]

        # retrieve question msg
        q_author_str = 'anonymous' if q[2] is None else (await self.bot.fetch_user(q[2])).name
        qstr = f"Q{q[0]}: {q[1]} by {q_author_str}\n"

        rows_deleted = db.query(
            'SELECT * FROM answers WHERE guild_id = %s AND q_number = %s',
            (ctx.guild.id, num)
        )
        # Delete all answers for question
        db.query('DELETE FROM answers WHERE guild_id = %s AND q_number = %s',
                (ctx.guild.id, num))

        if len(rows_deleted) == 0:
            await ctx.author.send(
                f"No answers exist for Q{num}")
        else:
            await ctx.author.send(
                f"deleted {len(rows_deleted)} answers for Q{num}")

        # check if message exists on the channel. If it does, restore the question!
        try:
            message = await ctx.fetch_message(q[3])
        except NotFound:
            nf_str = f"Question {num} not found in channel. It may have been deleted."
            await ctx.author.send(nf_str)
            # delete user msg
            await ctx.message.delete()
            return

        await message.edit(content=qstr)
        # delete user msg
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteAllAnswersFor_error(self, ctx, error)
    #    Description: prints error message for deleteAllAnswersFor command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @deleteAllAnsFor.error
    async def deleteAllAnsFor_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the deleteAllAnswersFor command, do: $DALLAF QUESTION_NUMBER\n '
                '(Example: $DALLAF 1)')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: getAllAnsFor
    #    Description: gets all answers for a question and DMs them to the user.
    #    Inputs:
    #       - ctx: context of the command
    #       - num: question number
    #    Outputs:
    #       - All answers for a question, if any
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='getAnswersFor', help='Get a question and all its answers\n'
                                       'EX: $getAnswersFor 1')
    async def getAllAnsFor(self, ctx, num):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # to stop SQL from screaming. Only allows valid numbers.
        if not re.match(r'^([1-9]\d*|0)$', num):
            await ctx.author.send('Please include a valid question number. EX: $getAnswersFor 1')
            await ctx.message.delete()
            return

        # check if question number exists
        q = db.query('SELECT number, question, author_id, msg_id FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('Invalid question number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        q = q[0]

        # check if message exists on channel
        try:
            await ctx.fetch_message(q[3])
        except NotFound:
            nf_str = f"Question {num} not found. It may have been deleted."
            await ctx.author.send(nf_str)
            # delete user msg
            await ctx.message.delete()
            return

        # retrieve question msg
        q_author_str = 'anonymous' if q[2] is None else (await self.bot.fetch_user(q[2])).name
        qstr = f"Q{q[0]}: {q[1]} by {q_author_str}\n"

        # get all answers for question and add to msg
        answers = db.query('SELECT answer, author_id, author_role FROM answers WHERE guild_id = %s AND q_number = %s',
                           (ctx.guild.id, num))

        # if there are no answers, return
        if len(answers) == 0:
            qstr += f"No answers for Q{q[0]}\n"
            await ctx.author.send(qstr)
            await ctx.message.delete()
            return

        for answer, author, role in answers:
            a_author = 'anonymous' if author is None else (await self.bot.fetch_user(author)).name
            qstr += f"{a_author} ({role}) Ans: {answer}\n"

        # send the question and answers to user
        await ctx.author.send(qstr)

        # delete user msg
        #try:
        await ctx.message.delete()
        #except NotFound:
        #    pass

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: getAllAnsFor_error(self, ctx, error)
    #    Description: prints error message for getAnswersFor command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @getAllAnsFor.error
    async def getAllAnsFor_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the getAnswersFor command, do: $getAnswersFor QUESTION_NUMBER\n '
                '(Example: $getAnswersFor 1)')
        else:
            await ctx.author.send(error)
        #try:
        await ctx.message.delete()
        #except NotFound:
        #    pass

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: archiveQA
    #    Description: DM all questions and their answers to the user.
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       - DMs all questions and answers to the user
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='archiveQA', help='(PLACEHOLDER NAME) DM all questions and their answers\n'
                                       'EX: $archiveQA')
    async def archiveQA(self, ctx):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # get questions
        q = db.query('SELECT number, question, author_id, msg_id FROM questions WHERE guild_id = %s',
                     (ctx.guild.id,))
        if len(q) == 0:
            await ctx.author.send('No questions found in database.')
            # delete user msg
            await ctx.message.delete()
            return

        for number, question, author_id, msg_id in q:

            # prevent receiving any deleted questions.
            try:
                await ctx.fetch_message(msg_id)
            except NotFound:
                nf_str = f"Q{number} is a ghost!"
                await ctx.author.send(nf_str)
                #go to next question
                continue

            q_author_str = 'anonymous' if author_id is None else (await self.bot.fetch_user(author_id)).name
            qstr = f"Q{number}: {question} by {q_author_str}\n"

            # get all answers for question and add to msg
            answers = db.query('SELECT answer, author_id, author_role FROM answers WHERE guild_id = %s AND q_number = %s',
                           (ctx.guild.id, number))

            if len(answers) == 0:
                qstr += f"No answers for Q{number}\n"
            else:
                for answer, author, role in answers:
                    a_author = 'anonymous' if author is None else (await self.bot.fetch_user(author)).name
                    qstr += f"{a_author} ({role}) Ans: {answer}\n"

            # send the question and answers to user
            await ctx.author.send(qstr)

        # delete msg
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: archiveqa_error(self, ctx, error)
    #    Description: prints error message for archiveQA command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @archiveQA.error
    async def archiveqa_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'archiveQA doesn\'t need any arguments. Just use $archiveQA')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteAllQAs
    #    Description: Deletes all questions and answers from the database and channel.
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       -
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='deleteAllQA', help='(PLACEHOLDER NAME) Delete all questions and answers from the database and channel.\n'
                                       'EX: $deleteAllQA\n'
                                       'THIS COMMAND IS IRREVERSIBLE.\n'
                                       'BE SURE TO ARCHIVE ALL QUESTIONS BEFORE DELETION. ($archiveQA)'
                                       )
    async def deleteAllQAs(self, ctx):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # get questions
        q = db.query('SELECT msg_id FROM questions WHERE guild_id = %s',
                     (ctx.guild.id,))
        if len(q) == 0:
            await ctx.author.send('No questions found in database.')
            return

        #Questions that were previously deleted on the channel but not in the database.
        ghostqs = 0
        # delete questions in channel
        for msg_id in q:
            mid = msg_id[0]
            try:
                message = await ctx.fetch_message(mid)
            except NotFound:
                ghostqs += 1
                continue
            else:
                await message.delete()

        # count deleted questions
        qs_deleted = db.query(
            'SELECT * FROM questions WHERE guild_id = %s',
            (ctx.guild.id,)
        )

        numqs = len(qs_deleted)

        # Delete all questions
        db.query('DELETE FROM questions WHERE guild_id = %s',
                (ctx.guild.id,))

        # Delete all answers
        db.query('DELETE FROM answers WHERE guild_id = %s',
                (ctx.guild.id,))

        report = f"Deleted {numqs} questions from the database, including {ghostqs} ghost questions."
        await ctx.author.send(report)

        # delete user msg
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteAllQAs_error(self, ctx, error)
    #    Description: prints error message for deleteAllQA command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @deleteAllQAs.error
    async def deleteAllQAs_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'deleteAllQA doesn\'t need any arguments. Just use $deleteAllQA')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteOneQuestion
    #    Description: Delete one question and all of its answers. Instructor only.
    #    Inputs:
    #       - ctx: context of the command
    #       - num: number of the question to delete
    #    Outputs:
    #       -
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='deleteQuestion', help='Delete one question and all its answers.'
                                    ' Leaves database ghosts. (RESURRECTION COMING SOON)\n'
                                    'EX: $deleteQuestion QUESTION_NUMBER\n'
                                    )
    async def deleteOneQuestion(self, ctx, num):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # to stop SQL from freezing. Only allows valid numbers.
        if not re.match(r'^([1-9]\d*|0)$', num):
            await ctx.author.send('Please include a valid question number. EX: $deleteQuestion 1')
            await ctx.message.delete()
            return

       # check if question number exists
        q = db.query('SELECT number, msg_id FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('Question number not in database: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        q = q[0]

        # check if message exists on channel
        try:
            msg = await ctx.fetch_message(q[1])
        except NotFound:
            nf_str = f"Q{q[0]} is already a ghost!"
            await ctx.author.send(nf_str)
        else:
            await msg.delete()
            haunt = f"Q{q[0]} is now a ghost. To see ghost handling options, use the $help command."
            await ctx.author.send(haunt)

        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteOneQuestion_error(self, ctx, error)
    #    Description: prints error message for deleteQuestion command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @deleteOneQuestion.error
    async def deleteOneQuestion_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the deleteQuestion command, do: $deleteQuestion QUESTION_NUMBER\n '
                '(Example: $deleteQuestion 1')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()

def setup(bot):
    n = Qanda(bot)
    bot.add_cog(n)
