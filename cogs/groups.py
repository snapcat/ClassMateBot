# Copyright (c) 2021 War-Keeper
import os
import sys

import discord
from discord.ext import commands

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


# -----------------------------------------------------------
# This File contains commands for joining a group, leaving a group,
# and displaying which groups are available
# -----------------------------------------------------------
class Groups(commands.Cog):
    student_pool = {}

    # -----------------------------------------------------------
    # initialize
    # -----------------------------------------------------------
    def __init__(self, bot):
        self.bot = bot

    # -------------------------------------------------------------------------------------------------------
    #    Function: join(self, ctx, group_num='-1')
    #    Description: joins the user to the given group
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - group_num: the number of the group
    #    Outputs: adds the user to the given group or returns an error if the group is invalid or in case of
    #             syntax errors
    # -------------------------------------------------------------------------------------------------------
    @commands.command(name='join', help='To use the join command, do: $join <Num> \n \
    ( For example: $join 0 )', pass_context=True)
    async def join(self, ctx, group_num: int):
        # get the name of the caller
        member_name = ctx.message.author.display_name.upper()

        if group_num < 0 or group_num > 99:
            await ctx.send('Not a valid group')
            await ctx.send("To use the join command, do: $join <Num> "
                           "where 0 <= <Num> <= 99 \n ( For example: $join 0 )")
            return

        group_count = db.query(
            'SELECT COUNT(group_num) FROM group_members WHERE guild_id = %s AND group_num = %s',
            (ctx.guild.id, group_num)
        )

        if group_count == 6:
            await ctx.send('A group cannot have more than 6 people!')
            return

        current_group_num = db.query(
            'SELECT group_num FROM group_members WHERE guild_id = %s AND member_name = %s',
            (ctx.guild.id, member_name)
        )

        if current_group_num:
            await ctx.send(f'You are already in Group {current_group_num[0][0]}')
            return

        db.query(
            'INSERT INTO group_members (guild_id, group_num, member_name) VALUES (%s, %s, %s)',
            (ctx.guild.id, group_num, member_name)
        )
        await ctx.send(f'You are now in Group {group_num}! There are now {group_count[0][0] + 1}/6 members.')

    # this handles errors related to the join command
    @join.error
    async def join_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('To use the join command, do: $join <Num> \n ( For example: $join 0 )')
        print(error)

    # -------------------------------------------------------------------------------------------------------
    #    Function: leave(self, ctx)
    #    Description: removes the user from the given group
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - arg: the name of the group
    #    - arg2: the number of the group
    #    Outputs: removes the user from the given group or returns an error if the group is invalid or in
    #             case of syntax errors
    # -------------------------------------------------------------------------------------------------------
    @commands.command(name='leave', help='To use the leave command, do: $leave \n \
    ( For example: $leave )', pass_context=True)
    async def leave(self, ctx):
        # get the name of the caller
        member_name = ctx.message.author.display_name.upper()

        current_group_num = db.query(
            'SELECT group_num FROM group_members WHERE guild_id = %s AND member_name = %s',
            (ctx.guild.id, member_name)
        )

        if current_group_num:
            db.query(
                'DELETE FROM group_members WHERE guild_id = %s AND member_name = %s',
                (ctx.guild.id, member_name)
            )

            await ctx.send(f'You have been removed from Group {current_group_num[0][0]}!')
        else:
            await ctx.send('You are not in a group!')

    # -------------------------------------------------------------------------------------------------------
    #    Function: group(self, ctx)
    #    Description: prints the list of groups
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints the list of groups
    # -------------------------------------------------------------------------------------------------------
    @commands.command(name='groups', help='prints group counts', pass_context=True)
    # @commands.dm_only()
    # TODO maybe include channel where all groups displayed
    async def groups(self, ctx):
        # load groups csv
        groups = db.query(
            'SELECT group_num, array_agg(member_name) '
            'FROM group_members WHERE guild_id = %s GROUP BY group_num ORDER BY group_num',
            (ctx.guild.id,)
        )

        # create embedded objects
        embed = discord.Embed(title='Group List', color=discord.Color.teal())
        embed.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        for group_num, members in groups:
            embed.add_field(name=f'Group {group_num}', value=str(len(members)), inline=True)

        # print the embedded objects
        embed.set_footer(text="Number Represents the Group Size")
        await ctx.send(embed=embed)

        # -------------------------------------------------------------------------------------------------------
    #    Function: group(self, ctx, group_num)
    #    Description: prints the members of the group, or the current members group if they have a group
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - group_num: the group number to list names for
    #    Outputs: prints the name of people in the group
    # -------------------------------------------------------------------------------------------------------
    @commands.command(name='group', help='print names of members in a group, or current groups members \n \
    ( For example: $group or $group 8 )', pass_context=True)
    # @commands.dm_only()
    # TODO maybe include channel where all groups displayed
    async def group(self, ctx, group_num: int = -1):

        if group_num == -1:
            member_name = ctx.message.author.display_name.upper()

            group_num = db.query(
                'SELECT group_num FROM group_members WHERE guild_id = %s and member_name = %s',
                (ctx.guild.id, member_name)
            )

            if not group_num:
                await ctx.send('You are not in a group!')
                return

            group_num = group_num[0][0]

        # load groups csv
        group = db.query(
            'SELECT member_name FROM group_members WHERE guild_id = %s and group_num = %s',
            (ctx.guild.id, group_num)
        )

        # create embedded objects
        embed = discord.Embed(title='Group Members', color=discord.Color.teal())
        embed.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        members = ""

        for member in group:
            members += member[0] + '\n'

        if members == "":
            members = "None"

        embed.add_field(name=f'Group {group_num}: ', value=members, inline=True)

        # print the embedded objects
        await ctx.send(embed=embed)

    # -----------------------------------------------------------
    # This is a testing arg, not really used for anything else but adding to the csv file
    # -----------------------------------------------------------
    # @commands.command(name='test_name', help='add a name to the name_mapping.csv', pass_context=True)
    # async def test_name(self, ctx, arg, arg2):
    #     student_pool = load_pool()
    #     display_name = ctx.message.author.display_name
    #     display_name_upper = display_name.upper()
    #
    #     if student_pool.get(display_name_upper) is None:
    #         student_pool[display_name_upper] = arg.upper() + ' ' + arg2.upper()
    #     else:
    #         member_name = student_pool[display_name_upper]
    #         await ctx.send('You have already registered with the name: ' + member_name.title())
    #
    #     print_pool(student_pool)



# # ------------------------------------------------------------
# # Used to load the members from the csv file into a dictionary
# # ------------------------------------------------------------
# def load_pool() -> dict:
#     dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     os.chdir(dir)
#     os.chdir('data')
#     os.chdir('server_data')
#     with open('name_mapping.csv', mode='r') as infile:
#         reader = csv.reader(infile)
#         student_pools = {rows[0].upper(): rows[1].upper() for rows in reader}
#     return student_pools


# # -----------------------------------------------------------
# # Used to print the members to the csv file
# # -----------------------------------------------------------
# def print_pool(pools):
#     dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     os.chdir(dir)
#     os.chdir('data')
#     os.chdir('server_data')
#     with open('name_mapping.csv', mode='w', newline="") as outfile:
#         writer = csv.writer(outfile)
#         for key, value in pools.items():
#             writer.writerow([key, value])


# -----------------------------------------------------------
# add the file to the bot's cog system
# -----------------------------------------------------------
def setup(bot):
    bot.add_cog(Groups(bot))
