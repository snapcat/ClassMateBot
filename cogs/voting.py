# Copyright (c) 2021 War-Keeper
import os
import sys

from discord.ext import commands

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db
# -----------------------------------------------------------
# This File contains commands for voting on projects,
# displaying which groups have signed up for which project
# -----------------------------------------------------------
class Voting(commands.Cog):

    # -----------
    # initialize
    # -----------
    def __init__(self, bot):
        self.bot = bot

    # ----------------------------------------------------------------------------------------------------------
    #    Function: vote(self, ctx, arg2='-1')
    #    Description: "votes" for the given project by adding the users group to it
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - project_num: the number of the project to vote for with group
    #    Outputs: adds the user to the given project, switching if already in a project
    #             or returns an error if the project is invalid or the user is not in a valid group
    # ----------------------------------------------------------------------------------------------------------
    @commands.command(name='vote', help='Used for voting for Projects, \
    To use the vote command, do: $vote <Num> \n \
    (For example: $vote 0)', pass_context=True)
    async def vote(self, ctx, project_num : int):
        # get the name of the caller
        member_name = ctx.message.author.display_name.upper()

        if project_num < 0 or project_num > 99:
            await ctx.send("A valid project number is 1-99.")
            return

        group = db.query(
            'SELECT group_num FROM group_members WHERE guild_id = %s AND member_name = %s',
            (ctx.guild.id, member_name)
        )

        # error handle if member is not in a group
        if len(group) == 0:
            await ctx.send("You are not in a group. You must join a group before voting on a project.")
            return

        group = group[0][0]

        num_groups = db.query(
            'SELECT COUNT(*) FROM project_groups WHERE guild_id = %s AND project_num = %s',
            (ctx.guild.id, project_num)
        )[0]

        # check if project has more than 6 groups voting on it
        if num_groups == 3:
            await ctx.send('Projects are limited to 3 groups, please select another project.')
            return

        voted_for = db.query(
            'SELECT project_num FROM project_groups WHERE guild_id = %s AND group_num = %s',
            (ctx.guild.id, group)
        )

        if voted_for:
            voted_for = voted_for[0][0]
            if voted_for == project_num:
                await ctx.send(f'You already voted for Project {voted_for}')
                return

            db.query(
                'DELETE FROM project_groups WHERE guild_id = %s AND group_num = %s',
                (ctx.guild.id, group)
            )
            await ctx.send(f'Group {group} removed vote for Project {voted_for}')

        # add the group to the project list
        db.query(
            'INSERT INTO project_groups (guild_id, project_num, group_num) VALUES (%s, %s, %s)',
            (ctx.guild.id, project_num, group)
        )
        await ctx.send(f'Group {group} has voted for Project {project_num}!')

    # this handles errors related to the vote command
    @vote.error
    async def vote_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send('To join a project, use the join command, do: $vote <Num> \n'
            '( For example: $vote 0 )')
        print(error)

    # ----------------------------------------------------------------------------------
    #    Function: projects(self, ctx)
    #    Description: prints the list of current projects
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints the list of current projects
    # ----------------------------------------------------------------------------------
    @commands.command(name='projects', help='print projects with groups assigned to them', pass_context=True)
    # @commands.dm_only()
    async def projects(self, ctx):
        projects = db.query(
            "SELECT project_num, string_agg(group_num::text, ', ') AS group_members "
            "FROM project_groups WHERE guild_id = %s GROUP BY project_num",
            (ctx.guild.id,)
        )

        if len(projects) > 0:
            await ctx.send('\n'.join(f'Project {project_num}: Group(s) {group_members}'
                                     for project_num, group_members in projects))
        else:
            await ctx.send('There are currently no votes for any project numbers.')


# -----------------------------------------------------------
# add the file to the bot's cog system
# -----------------------------------------------------------
def setup(bot):
    bot.add_cog(Voting(bot))
