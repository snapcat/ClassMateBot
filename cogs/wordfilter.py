# This functionality provides functionality for profanity filter management.
# TODO THIS WHOLE THING MAY NEED TO BE MOVED INTO BOT.PY TO ACCESS profanity_helper
import os

from discord import NotFound
from discord.ext import commands
import db
#import profanity_helper

class WordFilter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # TODO
    # whitelistWord
    # remove from white list
    # clear whitelist
    # load whitelist
    # add custom word
    # remove custom word
    # clear custom words
    # load custom words
    # reset filter (doesn't clear any saved lists. It just prevents better-profanity from using any saved lists.)
    # prevent commands from being blacklisted

    #custom_badwords = ['happy', 'jolly', 'merry']
    #profanity.add_censor_words(custom_badwords)


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: whitelistWord
    #    Description: allow instructors to add words to censor whitelist
    #    Inputs:
    #       - ctx: context of the command
    #       - word: the word to whitelist
    #    Outputs:
    #       - success message
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(
        name='whitelisttest',
        help='Add a word to the censor whitelist. Enclose in quotation marks. EX: $whitelist \"WORD\"')
    async def whitelistWordTest(self, ctx, word: str =''):

        #if not ctx.channel.name == 'instructor-commands':
        #    await ctx.author.send('Please use this command inside #instructor-commands')
        #    await ctx.message.delete()
        #    return





        await ctx.send(
            f"_{word}_ has been added to the whitelist. TODO")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: whitelistWord_error(self, ctx, error)
    #    Description: prints error message for whitelist command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @whitelistWordTest.error
    async def whitelistWord_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'Todo')
        else:
            await ctx.send(error)
        print(error)
        await ctx.message.delete()


    # -----------------------------------------------------------------------------------------------------------------
    #    Function: clearwhitelist
    #    Description: allow instructors to clear their saved whitelist
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       - success message
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(
        name='clearWhitelist',
        help='Clears all words from the saved whitelist. EX: $clearwhitelist')
    async def clearWhitelist(self, ctx):

        if not ctx.channel.name == 'instructor-commands':
            await ctx.author.send('Please use this command inside #instructor-commands')
            await ctx.message.delete()
            return

        # clear whitelist and reconstruct.


        await ctx.send("Whitelist has been cleared. TODO")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: whitelistWord_error(self, ctx, error)
    #    Description: prints error message for whitelist command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @clearWhitelist.error
    async def clearWhitelist_error(self, ctx, error):
        print(error)
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: loadWhitelist
    #    Description: allow instructors to load their saved whitelist
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       - success message
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(
        name='loadWhitelist',
        help='Adds all words in the saved whitelist to the censor whitelist. EX: $loadWhitelist')
    async def loadWhitelist(self, ctx):

        if not ctx.channel.name == 'instructor-commands':
            await ctx.author.send('Please use this command inside #instructor-commands')
            await ctx.message.delete()
            return


        await ctx.send("Whitelist has been loaded. TODO")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: loadWhitelist_error(self, ctx, error)
    #    Description: prints error message for loadWhitelist command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @loadWhitelist.error
    async def loadWhitelist_error(self, ctx, error):
        print(error)
        await ctx.message.delete()

def setup(bot):
    n = WordFilter(bot)
    bot.add_cog(n)
