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
    @commands.command(name='ask', help='Ask question. Please put question text in quotes. Add *anonymous* or *anon* if desired.'
                                       'EX: $ask /"When is the exam?/" anonymous')
    async def askQuestion(self, ctx, qs: str, anonymous=''):

        # make sure to check that this is actually being asked in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please send questions to the #q-and-a channel.')
            await ctx.message.delete()
            return

        if not qs or qs.isspace():
            await ctx.author.send("Please enter a valid question.")
            await ctx.message.delete()
            return

        if len(qs) <= 2:
            await ctx.author.send('Question too short.')
            await ctx.message.delete()
            return

        # get author
        if anonymous == '':
            author = ctx.message.author.id
        elif anonymous == 'anonymous':
            author = None
        elif anonymous == 'anon':
            author = None
        else:
            await ctx.author.send('Unknown input for *anonymous* option. Please type **anonymous**, **anon**, or leave blank.')
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
                      help='Answer question. Please put answer text in quotes. Add *anonymous* or *anon* if desired.'
                           'EX: $answer 1 /"Oct 12/" anonymous')
    async def answer(self, ctx, num, ans: str, anonymous=''):
        ''' answer the specific question '''
        # make sure to check that this is actually being asked in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please send answers to the #q-and-a channel.')
            await ctx.message.delete()
            return

        if not ans or ans.isspace():
            await ctx.author.send("Please enter a valid answer.")
            await ctx.message.delete()
            return

#        if len(ans) == 0:
#            await ctx.author.send('Answer too short.')
#            await ctx.message.delete()
#            return

        # get author
        if anonymous == '':
            author = ctx.message.author.id
        elif anonymous == 'anonymous':
            author = None
        elif anonymous == 'anon':
            author = None
        else:
            await ctx.author.send('Unknown input for *anonymous* option. Please type **anonymous**, **anon**, or leave blank.')
            await ctx.message.delete()
            return

        # to stop SQL from freezing. Only allows valid numbers.
        if not re.match(r'^([1-9]\d*|0)$', num):
            await ctx.author.send('Please include a valid question number. EX: $answer 1 /"Oct 12/" anonymous')
            await ctx.message.delete()
            return

        # check if question number exists
        q = db.query('SELECT number, question, author_id, msg_id, is_ghost FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('No such question with the number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return
        q = q[0]

        # if is_ghost is true:
        if q[4]:
            await ctx.author.send("You can't answer a ghost!")
            await ctx.message.delete()
            return

        # check if message exists
        try:
            message = await ctx.fetch_message(q[3])
        except NotFound:
            nf_str = f"Question {num} not found. It's a zombie!"
            await ctx.author.send(nf_str)
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
            nf_str = f"Question {num} not found. It's a zombie!"
            await ctx.author.send(nf_str)
            #await ctx.author.send('Invalid question number: ' + str(num))

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
        q = db.query('SELECT number, question, author_id, msg_id, is_ghost FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('No such question with the number: ' + str(num))
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

        rd = len(rows_deleted)

        # Delete all answers for question
        db.query('DELETE FROM answers WHERE guild_id = %s AND q_number = %s',
                (ctx.guild.id, num))

        if rd == 0:
            await ctx.author.send(
                f"No answers exist for Q{num}")
        else:
            await ctx.author.send(
                f"deleted {rd} answers for Q{num}")

        # if it's a ghost, return.
        if q[4]:
            ghost = f"Q{num} is a ghost!"
            await ctx.author.send(ghost)
            await ctx.message.delete()
            return

        # check if message exists on the channel. If it does, restore the question!
        try:
            message = await ctx.fetch_message(q[3])
        except NotFound:
            nf_str = f"Q{num} is a zombie!"
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
        q = db.query('SELECT number, question, author_id, msg_id, is_ghost FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('No such question with the number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        q = q[0]

        # if the question is a ghost, return.
        if q[4]:
            nf_str = f"Q{q[0]} is a ghost!"
            await ctx.author.send(nf_str)
            await ctx.message.delete()
            return
        # check if message exists on channel
        try:
            await ctx.fetch_message(q[3])
        except NotFound:
            nf_str = f"Question {num} not found. It's a zombie!"
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
        await ctx.message.delete()


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
        await ctx.message.delete()

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
        q = db.query('SELECT number, question, author_id, msg_id, is_ghost FROM questions WHERE guild_id = %s ORDER BY number ASC',
                     (ctx.guild.id,))
        if len(q) == 0:
            await ctx.author.send('No questions found in database.')
            # delete user msg
            await ctx.message.delete()
            return

        for number, question, author_id, msg_id, is_ghost in q:

            # prevent receiving any hidden questions.
            if is_ghost:
                nf_str = f"Q{number} is a ghost!"
                await ctx.author.send(nf_str)
                #go to next question
                continue

            # prevent receiving any deleted questions.
            try:
                await ctx.fetch_message(msg_id)
            except NotFound:
                if not is_ghost:
                    nf_str = f"Q{number} was deleted. It's a zombie!"
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
    @commands.command(name='deleteAllQA', help='Delete all questions and answers from the database and channel.\n'
                                'EX: $deleteAllQA\n'
                                'THIS COMMAND IS IRREVERSIBLE.\n'
                                'BE SURE TO ARCHIVE ALL QUESTIONS BEFORE DELETION.\n'
                                'To archive, use the $unearthZombies command followed by $allChannelGhosts,'
                                ' and then use $archiveQA.'
                                )
    async def deleteAllQAs(self, ctx):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # get questions
        q = db.query('SELECT msg_id, is_ghost FROM questions WHERE guild_id = %s',
                     (ctx.guild.id,))

        numqs = len(q)
        if numqs == 0:
            await ctx.author.send('No questions found in database.')
            return

        # Zombies are questions that were manually deleted from the channel. They need to be
        # assigned new message IDs in order to be restored--that is, they need to be reposted.
        # Ghosts are questions that were deleted (or hidden) with the deleteQuestion command.
        # Because their message IDs remain the same, their contents can just be unhidden.

        # track ghosts and zombies, and delete messages in the channel
        zombies = 0
        ghosts = 0
        for msg_id, is_ghost in q:
            if is_ghost:
                ghosts += 1
            try:
                message = await ctx.fetch_message(msg_id)
            except NotFound:
                if not is_ghost:
                    zombies += 1
                continue
            else:
                await message.delete()

        # count ghosts
        #spooks = db.query(
        #    'SELECT * FROM questions WHERE guild_id = %s AND is_ghost IS TRUE',
        #    (ctx.guild.id,)
        #)

        #spooky = len(spooks)

        # Delete all questions
        db.query('DELETE FROM questions WHERE guild_id = %s',
                (ctx.guild.id,))

        # Delete all answers
        db.query('DELETE FROM answers WHERE guild_id = %s',
                (ctx.guild.id,))

        report = f"Deleted {numqs} questions from the database, including {zombies} zombies and {ghosts} ghosts."
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
        await ctx.author.send(error)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteOneQuestion
    #    Description: Delete one question but leave answers untouched. Instructor only.
    #    Inputs:
    #       - ctx: context of the command
    #       - num: number of the question to delete
    #    Outputs:
    #       -
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='deleteQuestion', help='Delete (hide) one question but leave answers untouched.'
                                    ' Leaves database ghosts.\n'
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
        q = db.query('SELECT number, msg_id, is_ghost FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('Question number not in database: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        q = q[0]

        # if is_ghost is false, set to true
        if not q[2]:
            db.query('UPDATE questions SET is_ghost = NOT is_ghost WHERE guild_id = %s AND number = %s',
            (ctx.guild.id, num))
        else:
            sendme = f"Q{q[0]} is already a ghost!"
            await ctx.author.send(sendme)
            return

        # check if message exists on channel.
        try:
            msg = await ctx.fetch_message(q[1])
        except NotFound:
            nf_str = f"Q{q[0]} was not found in channel. To restore it, use: $reviveGhost {q[0]}"
            await ctx.author.send(nf_str)
        else:
            cstr = f"Q{q[0]}: _hidden_"
            await msg.edit(content=cstr)
            haunt = f"Q{q[0]} is now a ghost. To restore it, use: $reviveGhost {q[0]}"
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


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: channelOneGhost
    #    Description: Gets a specific ghost question. Instructor only.
    #    Inputs:
    #       - ctx: context of the command
    #       - num: question number
    #    Outputs:
    #       - All answers for a ghost question, if any
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='channelGhost', help='Gets a specific ghost (question deleted with command) and all its answers.\n'
                                       'EX: $channelGhost 1')
    async def channelOneGhost(self, ctx, num):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # to stop SQL from screaming. Only allows valid numbers.
        if not re.match(r'^([1-9]\d*|0)$', num):
            await ctx.author.send('Please include a valid question number. EX: $channelGhost 1')
            await ctx.message.delete()
            return

        # check if question number exists
        q = db.query('SELECT number, question, author_id, is_ghost FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('No such question with the number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        q = q[0]

        if not q[3]:
            await ctx.author.send('This question is not a ghost. Fetching anyway. . .')

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
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: channelOneGhost_error(self, ctx, error)
    #    Description: prints error message for channelGhost command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @channelOneGhost.error
    async def channelOneGhost_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the channelGhost command, do: $channelGhost QUESTION_NUMBER\n '
                '(Example: $channelGhost 1)')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: channelGhostQs
    #    Description: Get the questions that are in the database but not in the channel. Instructor only.
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       -
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='allChannelGhosts', help='Get all the questions that are in the database but '
                                    'not in the channel. Does not detect zombies.\n'
                                    'EX: $allChannelGhosts\n'
                                    'To detect zombies and convert them to ghosts, use $unearthZombies'
                                    )
    async def channelGhostQs(self, ctx):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

         # get questions
        q = db.query('SELECT number, question, author_id FROM questions WHERE guild_id = %s AND is_ghost IS TRUE ORDER BY number ASC',
                     (ctx.guild.id,))
        if len(q) == 0:
            await ctx.author.send('No ghosts found in database.')
            # delete user msg
            await ctx.message.delete()
            return

        for number, question, author_id in q:

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
    #    Function: channelGhostQs_error(self, ctx, error)
    #    Description: prints error message for allChannelGhosts command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @channelGhostQs.error
    async def channelGhostQs_error(self, ctx, error):
        await ctx.author.send(error)
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: unearthZombieQs
    #    Description: Assign ghost status to all manually deleted questions in case there is a
    #                 need to restore them. Instructor only.
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       -
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='unearthZombies', help='Assign ghost status to all manually deleted questions '
                                    'in case there is a need to restore them.\n'
                                    'EX: $unearthZombies\n'
                                    )
    async def unearthZombieQs(self, ctx):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # get questions
        q = db.query('SELECT number, msg_id FROM questions WHERE guild_id = %s AND is_ghost IS FALSE',
                     (ctx.guild.id,))
        if len(q) == 0:
            await ctx.author.send('No zombies detected.')
            # delete user msg
            await ctx.message.delete()
            return

        zombies = 0
        for number, msg_id in q:
            try:
                await ctx.fetch_message(msg_id)
            except NotFound:
                zombies += 1
                db.query('UPDATE questions SET is_ghost = NOT is_ghost WHERE guild_id = %s AND number = %s',
                (ctx.guild.id, number))

        if zombies == 0:
            await ctx.author.send("No zombies detected.")
        else:
            zomstr = f"Found {zombies} zombies and assigned them ghost status.\n"
            zomstr += "To view them, use: $allChannelGhosts\n"
            zomstr += "To restore a question, use: $reviveGhost QUESTION_NUMBER"
            await ctx.author.send(zomstr)

        # delete msg
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: unearthZombieQss_error(self, ctx, error)
    #    Description: prints error message for unearthZombies command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @unearthZombieQs.error
    async def unearthZombieQs_error(self, ctx, error):
        await ctx.author.send(error)
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: restoreGhost
    #    Description: Restores a ghost or deleted question to the channel. Instructor only.
    #    Inputs:
    #       - ctx: context of the command
    #       - num: question number
    #    Outputs:
    #       - All answers for a ghost question, if any
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='reviveGhost', help='Restores a ghost or deleted/hidden question to the channel.\n'
                                       'EX: $reviveGhost 1')
    async def restoreGhost(self, ctx, num):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        # to stop SQL from screaming. Only allows valid numbers.
        if not re.match(r'^([1-9]\d*|0)$', num):
            await ctx.author.send('Please include a valid question number. EX: $reviveGhost 1')
            await ctx.message.delete()
            return

        # check if question number exists
        q = db.query('SELECT number, question, author_id, msg_id, is_ghost FROM questions WHERE guild_id = %s AND number = %s',
                     (ctx.guild.id, num))
        if len(q) == 0:
            await ctx.author.send('No such question with the number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        q = q[0]

        # retrieve question msg
        q_author_str = 'anonymous' if q[2] is None else (await self.bot.fetch_user(q[2])).name
        qstr = f"Q{q[0]}: {q[1]} by {q_author_str}\n"

        # get all answers for question and add to msg
        answers = db.query('SELECT answer, author_id, author_role FROM answers WHERE guild_id = %s AND q_number = %s',
                           (ctx.guild.id, num))

        # if there are answers, restore them
        if len(answers) != 0:
            for answer, author, role in answers:
                a_author = 'anonymous' if author is None else (await self.bot.fetch_user(author)).name
                qstr += f"{a_author} ({role}) Ans: {answer}\n"

        try:
            msg = await ctx.fetch_message(q[3])
        except NotFound:
            # if the question was manually deleted, post it again (with all its answers)!
            message = await ctx.send(qstr)
            db.query('UPDATE questions SET msg_id = %s WHERE guild_id = %s AND number = %s',
            (message.id, ctx.guild.id, num))
        else:
            # restore the question
            await msg.edit(content=qstr)

        # if is_ghost is true, set to false
        if q[4]:
            db.query('UPDATE questions SET is_ghost = NOT is_ghost WHERE guild_id = %s AND number = %s',
            (ctx.guild.id, num))


        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: restoreGhost_error(self, ctx, error)
    #    Description: prints error message for reviveGhost command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @restoreGhost.error
    async def restoreGhost_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the reviveGhost command, do: $reviveGhost QUESTION_NUMBER\n '
                '(Example: $reviveGhost 1)')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()






    # -----------------------------------------------------------------------------------------------------------------
    #    Function: countGhosts
    #    Description: Counts the number of ghost and zombie questions in the channel. Just for fun, but may be useful
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       - The number of ghost questions
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='spooky', help='Is this channel haunted?\n'
                                       'EX: $spooky')
    async def countGhosts(self, ctx):

        # make sure to check that this is actually being used in the Q&A channel
        if not ctx.channel.name == 'q-and-a':
            await ctx.author.send('Please use this command inside the #q-and-a channel.')
            await ctx.message.delete()
            return

        q = db.query('SELECT msg_id, is_ghost FROM questions WHERE guild_id = %s',
                     (ctx.guild.id,))
        # if database is empty
        if len(q) == 0:
            await ctx.author.send("This channel isn't haunted.")
            await ctx.message.delete()
            return

        zombies = 0
        ghosts = 0
        for msg_id, is_ghost in q:
            # if it is a ghost, it doesn't matter if it isn't found.
            if is_ghost:
                ghosts += 1
                continue
            # if the message isn't found and it isn't a ghost, it's a zombie.
            try:
                await ctx.fetch_message(msg_id)
            except NotFound:
                zombies += 1

        if zombies == 0 and ghosts == 0:
            await ctx.author.send("This channel isn't haunted.")
            await ctx.message.delete()
            return

        spookstr = f"This channel is haunted by {ghosts} ghosts and {zombies} zombies."
        await ctx.author.send(spookstr)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: countGhosts_error(self, ctx, error)
    #    Description: prints error message for spooky command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @countGhosts.error
    async def countGhosts_error(self, ctx, error):
        await ctx.author.send(error)
        await ctx.message.delete()


def setup(bot):
    n = Qanda(bot)
    bot.add_cog(n)
