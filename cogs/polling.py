# This cog provides functionality for commands related to polls and quizzes.
import discord
from discord.ext import commands
import re

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.emojiLetters = [
            "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
        ]

    # parses the title, which should be in between curly brackets ('{ title }')
    #def find_title(self, message):
        # this is the index of the first character of the title
        #first = message.find('{') + 1
        # index of the last character of the title
        #last = message.find('}')

        #if first == last: # if the character after '{' is '}' ... does not check for whitespace.
        #    return ""

        #if first == 0 or last == -1:
        #    return ""
        #return message[first:last]

    # parses the options (recursively), which should be in between square brackets ('[ option n ]')
    #def find_options(self, message, options):
        # first index of the first character of the option
        #first = message.find('[') + 1
        # index of the last character of the title
        #last = message.find(']')
        #if (first == 0 or last == -1):
        #    if len(options) < 2:
        #        return "Not using the command correctly"
        #    else:
        #        return options
        #options.append(message[first:last])
        #message = message[last + 1:]
        #return self.find_options(message, options)

        # @commands.Cog.listener()


    # @commands.cooldown(2, 60, BucketType.user)
    # -----------------------------------------------------------------------------------------------------------------
    #    Function: quizpoll(self, ctx, title: str, *, ops)
    #    Description: Allows the user to begin quiz polls; that is, multi-reaction polls with listed options.
    #    Inputs:
    #       - ctx: context of the command
    #       - title: a string enclosed in double quotes; the quiz title
    #       - ops: up to six options, each in brackets
    #    Outputs:
    #       - an embedded quiz
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="quizpoll",
        help = 'Create a multi reaction poll by typing \n$poll "TITLE" [option 1] ... [option 6]\n '
                'Be sure to enclose title with quotes and options with brackets!\n'
                'EX: $quizpoll "I am a poll" [Vote for me!] [I am option 2]')
    async def quizpoll(self, ctx, title: str, *, ops):
        #message = ctx.message
        #messageContent = message.clean_content

        #title = self.find_title(messageContent)
        #options = self.find_options(messageContent, [])

        # if title is blank, whitespace only, or just too short!
        if not title or title.isspace():
            await ctx.author.send("Please enter a valid title.")
            await ctx.message.delete()
            return

        if len(title) <= 2:
            await ctx.author.send("Title too short.")
            await ctx.message.delete()
            return

        # regex: extracts every string between brackets
        options = re.findall(r'\[([^[\]]*)\]', ops)

        if len(options) < 2:
            await ctx.author.send(
                "Polls need at least two options.")
            await ctx.message.delete()
            return

        if len(options) > 6:
            await ctx.author.send(
                "Polls cannot have more than six options.")
            await ctx.message.delete()
            return

        try:
            pollMessage = ""
            i = 0
            for choice in options:
                if not choice or choice.isspace(): # if empty or whitespace only
                    await ctx.author.send("Options cannot be blank or whitespace only.")
                    await ctx.message.delete()
                    return
                if not i == len(options):
                    pollMessage = pollMessage + "\n\n" + self.emojiLetters[i] + "     " + choice
                i += 1

            ads = [""]

            e = discord.Embed(title="**" + title + "**",
                                description=pollMessage + ads[0],
                                colour=0x83bae3)
            pollMessage = await ctx.send(embed=e)
            i = 0
            #final_options = []  # There is a better way to do this for sure, but it also works that way
            for choice in options:
                if not i == len(options) and not options[i] == "":
                    #final_options.append(choice)
                    await pollMessage.add_reaction(self.emojiLetters[i])
                i += 1
        except KeyError:
            await ctx.author.send(
                'To use the quizpoll command, do: $quizpoll "TITLE" [option1] [option2] ... [option6]\n '
                'Be sure to enclose title with quotes and options with brackets!\n'
                'EX: $quizpoll "I am a poll" [Vote for me!] [I am option 2]')
            await ctx.message.delete()
            return
        # delete user message
        else:
            await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: quizpoll_error(self, ctx, error)
    #    Description: prints error message for quizpoll command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @quizpoll.error
    async def quizpoll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the quizpoll command, do: $quizpoll "TITLE" [option1] [option2] ... [option6]\n '
                'Be sure to enclose title with quotes and options with brackets!\n'
                'EX: $quizpoll "I am a poll" [Vote for me!] [I am option 2]')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: poll(self, ctx, qs)
    #    Description: Allows the user to create a simple reaction poll with thumbs up, thumbs down, and unsure.
    #    Inputs:
    #       - ctx: context of the command
    #       - qs: question string; the poll question
    #    Outputs:
    #       - an embedded reaction poll
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="poll", help = 'Create a reaction poll by typing $poll QUESTION\n'
                                            'EX: $poll What do you think about cats?')
    async def poll(self, ctx, *, qs=''):

        if qs == '':
            await ctx.author.send("Please enter a question for your poll.")
            #await ctx.send(
                #'To use the poll command, do: $poll QUESTION\n'
                #'EX: $poll Is this a good idea?')
            await ctx.message.delete()
            return

        # if using qs:str instead of *; checks for empty and whitespace only strings
        #if not qs or qs.isspace():
        #    await ctx.author.send("Please enter a question for your poll.")
            #await ctx.send(
            #    'To use the poll command, do: $poll QUESTION\n'
            #    'EX: $poll Is this a good idea?')
            #await ctx.message.delete()
        #    return

        if len(qs) <= 2:
            await ctx.author.send("Poll question too short.")
            await ctx.message.delete()
            return

        # can make it anonymous or not, is anonymous by default.
        if "instructor" in [y.name.lower() for y in ctx.author.roles]:
            author = 'Instructor'
        else:
            author = 'Student'

        #author = ctx.message.author.id
        #author_str = (await self.bot.fetch_user(author)).name

        # create a poll, post to channel, and add reactions.
        #pollmsg = f"**POLL by {author_str}**\n\n{pollstr}\n** **"
        pollmsg = f"**POLL by {author}**\n\n{qs}\n** **"
        message = await ctx.send(pollmsg)

        #TODO: ADD POLL ID TO DATABASE.
        #Need to check for deleted IDs when fetching poll results later.

        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')

        # delete original message
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: poll_error(self, ctx, error)
    #    Description: prints error message for poll command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                'To use the poll command, do: $poll QUESTION\n'
                'EX: $poll Is this a good idea?')
        else:
            await ctx.author.send(error)
        await ctx.message.delete()

def setup(bot):
    n = Poll(bot)
    bot.add_cog(n)
