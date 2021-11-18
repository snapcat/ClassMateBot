# Copyright (c) 2021 War-Keeper
import discord
import os
from datetime import datetime, timedelta
import discord.ext.test as dpytest
from dotenv import load_dotenv
import pytest
from discord.ext import commands


# ------------------------------------------------------------------------------------------------------
# Main file bot testing. Uses dpytest to test bot activity on a simulated server with simulated members
# ------------------------------------------------------------------------------------------------------


# -------------------
# Tests cogs/ping.py
# -------------------
@pytest.mark.asyncio
async def test_ping(bot):
    await dpytest.message("$ping")
    assert dpytest.verify().message().contains().content("Pong!")


# TODO Test user join messages


# ---------------------
# Tests cogs/groups.py
# ---------------------
@pytest.mark.asyncio
async def test_groupJoin(bot):
    # first leave all groups just in case in any
    await dpytest.message("$leave")
    dpytest.get_message()

    # Try to join a group
    await dpytest.message("$join 99")
    assert dpytest.verify().message().content("You are now in Group 99! There are now 1/6 members.")

    # try to join a different group
    await dpytest.message("$join 1")
    assert dpytest.verify().message().content("You are already in Group 99")

    # leave your group
    await dpytest.message("$leave")
    assert dpytest.verify().message().content("You have been removed from Group 99!")

    # leave with no group
    await dpytest.message("$leave")
    assert dpytest.verify().message().content("You are not in a group!")


# ------------------------------------
# Tests cogs/groups.py error handling
# ------------------------------------
@pytest.mark.asyncio
async def test_groupError(bot):
    # Try to join a group that doesn't exist
    await dpytest.message("$join -1")
    assert dpytest.verify().message().content('Not a valid group')
    assert dpytest.verify().message().content(
        'To use the join command, do: $join <Num> where 0 <= <Num> <= 99 \n ( For example: $join 0 )')

    try:
        await dpytest.message("$join")
        # should not reach here
        assert False
    except:
        assert dpytest.verify().message().content(
            'To use the join command, do: $join <Num> \n ( For example: $join 0 )')


# -----------------------
# Tests cogs/deadline.py
# -----------------------
@pytest.mark.asyncio
async def test_deadline(bot):
    # Clear our reminders: Only if testing fails and leaves a reminders.JSON file with values behind
    # await dpytest.message("$clearreminders")
    # assert dpytest.verify().message().contains().content("All reminders have been cleared..!!")
    # Test reminders while none have been set
    await dpytest.message("$coursedue CSC505")
    assert dpytest.verify().message().content("Rejoice..!! You have no pending homeworks for CSC505..!!")
    # Test setting 1 reminder
    await dpytest.message("$addhw CSC505 DANCE SEP 21 2050 10:00")
    assert dpytest.verify().message().contains().content(
        "A date has been added for: CSC505 homework named: DANCE which is due on: 2050-09-21 10:00:00")
    # Test setting a 2nd reminder
    await dpytest.message("$addhw CSC510 HW1 DEC 21 2050 19:59")
    assert dpytest.verify().message().contains().content(
        "A date has been added for: CSC510 homework named: HW1 which is due on: 2050-12-21 19:59:00")
    # Test deleting reminder
    await dpytest.message("$deletereminder CSC510 HW1")
    assert dpytest.verify().message().content(
        "Following reminder has been deleted: Course: CSC510, Homework Name: HW1, Due Date: 2050-12-21 19:59:00")
    # Test re-adding a reminder
    await dpytest.message("$addhw CSC510 HW1 DEC 21 2050 19:59")
    assert dpytest.verify().message().contains().content(
        "A date has been added for: CSC510 homework named: HW1 which is due on: 2050-12-21 19:59:00")
    # Clear reminders at the end of testing since we're using a local JSON file to store them
    await dpytest.message("$clearreminders")
    assert dpytest.verify().message().content("All reminders have been cleared..!!")


# --------------------------------
# Test listing multiple reminders
# --------------------------------
@pytest.mark.asyncio
async def test_listreminders(bot):
    # Test listing multiple reminders
    await dpytest.message("$addhw CSC505 DANCE SEP 21 2050 10:00")
    assert dpytest.verify().message().contains().content(
        "A date has been added for: CSC505 homework named: DANCE which is due on: 2050-09-21 10:00:00")
    # Test setting a 2nd reminder
    await dpytest.message("$addhw CSC510 HW1 DEC 21 2050 19:59")
    assert dpytest.verify().message().contains().content(
        "A date has been added for: CSC510 homework named: HW1 which is due on: 2050-12-21 19:59:00")
    await dpytest.message("$listreminders")
    assert dpytest.verify().message().contains().content(
        "CSC505 homework named: DANCE which is due on: 2050-09-21 10:00:00")
    assert dpytest.verify().message().contains().content(
        "CSC510 homework named: HW1 which is due on: 2050-12-21 19:59:00")
    # Test $coursedue
    await dpytest.message("$coursedue CSC505")
    assert dpytest.verify().message().contains().content(
        "DANCE is due at 2050-09-21 10:00:00")
    # Try to change the due date of DANCE to something impossible
    await dpytest.message("$changeduedate CSC505 DANCE 4")
    assert dpytest.verify().message().contains().content(
        "Due date could not be parsed")
    # Clear reminders at the end of testing since we're using a local JSON file to store them
    await dpytest.message("$clearreminders")
    assert dpytest.verify().message().contains().content("All reminders have been cleared..!!")

    # Tests cogs/deadline.py


# ------------------------------
# Tests reminders due this week
# ------------------------------
@pytest.mark.asyncio
async def test_duethisweek(bot):
    # Try adding a reminder due in an hour
    now = datetime.now() + timedelta(hours=1)
    dt_string = now.strftime("%b %d %Y %H:%M")
    await dpytest.message(f'$addhw CSC600 HW0 {dt_string}')
    assert dpytest.verify().message().contains().content(
        "A date has been added for: CSC600 homework named: HW0")
    # Check to see that the reminder is due this week
    await dpytest.message("$duethisweek")
    assert dpytest.verify().message().contains().content("CSC600 HW0 is due this week")
    # Clear reminders at the end of testing since we're using a local JSON file to store them
    await dpytest.message("$clearreminders")
    assert dpytest.verify().message().contains().content("All reminders have been cleared..!!")


# --------------------
# Tests cogs/pinning
# --------------------
@pytest.mark.asyncio
async def test_pinning(bot):
    # Test pinning a message
    await dpytest.message("$pin TestMessage www.google.com this is a test")
    # print(dpytest.get_message().content)
    assert dpytest.verify().message().contains().content(
        "A new message has been pinned with tag: TestMessage and description: www.google.com this is a test")
    await dpytest.message("$pin TestMessage www.discord.com this is also a test")
    assert dpytest.verify().message().contains().content(
        "A new message has been pinned with tag: TestMessage and description: www.discord.com this is also a test")

    #clean up
    #await dpytest.message("$unpin TestMessage")


# ----------------
# Tests unpinning
# ----------------
@pytest.mark.asyncio
async def test_unpinning(bot):
    # Test pinning a message
    await dpytest.message("$pin TestMessage www.google.com this is a test")
    assert dpytest.verify().message().contains().content(
        "A new message has been pinned with tag: TestMessage and description: www.google.com this is a test")
    await dpytest.message("$pin TestMessage www.discord.com this is also a test")
    assert dpytest.verify().message().contains().content(
        "A new message has been pinned with tag: TestMessage and description: www.discord.com this is also a test")
    # Tests unpinning a message that doesn't exist
    await dpytest.message("$unpin None")
    assert dpytest.verify().message().contains().content(
        "No message found with the combination of tagname: None, and author:")
    # Tests unpinning messages that DO exist
    await dpytest.message("$unpin TestMessage")
    assert dpytest.verify().message().contains().content(
        "2 pinned message(s) has been deleted with tag: TestMessage")
    # Tests adding another message to update pins
    await dpytest.message("$pin TestMessage2 www.discord.com test")
    assert dpytest.verify().message().contains().content(
        "A new message has been pinned with tag: TestMessage2 and description: www.discord.com test")
    await dpytest.message("$updatepin TestMessage2 www.zoom.com test")
    assert dpytest.verify().message().contains().content(
        "1 pinned message(s) has been deleted with tag: TestMessage2")
    assert dpytest.verify().message().contains().content(
        "A new message has been pinned with tag: TestMessage2 and description: www.zoom.com test")


# ----------------------
# Tests invalid pinning
# ----------------------
@pytest.mark.asyncio
async def test_pinError(bot):
    # Tests pinning without a message, will fail
    try:
        await dpytest.message("$pin")

        #shouldnt reach here
        assert False
    except:
        assert dpytest.verify().message().content(
            "To use the pin command, do: $pin TAGNAME DESCRIPTION \n ( For example: $pin HW8 https://"
            "discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder )")


# --------------------
# Tests cogs/newComer
# --------------------

@pytest.mark.asyncio
async def test_verify(bot):
    user = dpytest.get_config().members[0]
    guild = dpytest.get_config().guilds[0]
    channel = await guild.create_text_channel('general')

    await dpytest.message("$verify Student Name", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Warning: Please make sure the verified and unverified roles exist in this server!')

    # Test self-verification - unverified role assigned
    await guild.create_role(name="unverified")
    await guild.create_role(name="verified")
    role = discord.utils.get(guild.roles, name="unverified")
    await dpytest.add_role(user, role)
    await dpytest.message("$verify Student Name", channel=channel)
    assert dpytest.verify().message().contains().content(
        f'Thank you for verifying! You can start using {guild.name}!')
    dpytest.get_message()


@pytest.mark.asyncio
async def test_verifyNoName(bot):
    guild = dpytest.get_config().guilds[0]
    await guild.create_role(name="unverified")
    await guild.create_role(name="verified")
    # Test verification without proper argument given
    await dpytest.message("$verify")
    # print(dpytest.get_message().content)
    assert dpytest.verify().message().contains().content(
        'To use the verify command, do: $verify <FirstName LastName> \n ( For example: $verify Jane Doe )')

# We cannot currently test newComer.py in a meaningful way due to not having a way to DM the test bot directly,
# as well as inability to have dpytest add/remove roles to test specific cases


# --------------------
# Tests cogs/Voting
# --------------------
@pytest.mark.asyncio
async def test_voting(bot):
    # Test voting
    await dpytest.message(content="$vote 1")
    assert dpytest.verify().message().content(
        "You are not in a group. You must join a group before voting on a project.")
    await dpytest.message("$join 99")
    dpytest.get_message()
    await dpytest.message(content="$vote 1")
    assert dpytest.verify().message().content(
        "Group 99 has voted for Project 1!")
    await dpytest.message(content="$vote 2")
    assert dpytest.verify().message().content(
        "Group 99 removed vote for Project 1")
    assert dpytest.verify().message().content(
        "Group 99 has voted for Project 2!")
    await dpytest.message(content="$vote 2")
    assert dpytest.verify().message().content(
        "You already voted for Project 2")
    try:
        await dpytest.message(content="$vote")
        #shouldnt reach here
        assert False
    except:
        assert dpytest.verify().message().contains().content(
            "To join a project, use the join command, do: $vote <Num> \n( For example: $vote 0 )")
    await dpytest.message(content="$vote -1")
    assert dpytest.verify().message().content(
        "A valid project number is 1-99.")

# --------------------
# Tests cogs/qanda
# --------------------
@pytest.mark.asyncio
async def test_qanda(bot):
    # Test q and a functionalities
    # create channel and get user
    user = dpytest.get_config().members[0]
    guild = dpytest.get_config().guilds[0]
    channel = await guild.create_text_channel('q-and-a')
    await guild.create_role(name="Instructor")
    role = discord.utils.get(guild.roles, name="Instructor")
    await dpytest.add_role(user, role)

    ###### NEW TEST
    # Test archiveQA: no questions in database
    await dpytest.message("$archiveQA",channel=channel)
    assert dpytest.verify().message().contains().content(
        'No questions found in database.')
    ##### END OF NEW TEST

    # Test asking a question anonymously
    await dpytest.message("$ask \"What class is this?\" anonymous", channel=channel)
    assert dpytest.verify().message().contains().content(
        'What class is this? by anonymous')

    # Test asking a question with name
    await dpytest.message("$ask \"When is the last day of classes?\"", channel=channel)
    assert dpytest.verify().message().contains().content(
        'When is the last day of classes? by ' + user.name)

    ######### TESTS FOR Q&A ROUND 1, MERGE WITH UPDATED TEST FILES LATER
    gen_channel = await guild.create_text_channel('general')

    # Tests answering a nonexistent question (answer)
    await dpytest.message("$answer 100 \"nope\"", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Invalid question number: 100')

    # Tests answering with bad input (answer)
    await dpytest.message("$answer \"nope\" lol", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Please include a valid question number. EX: $answer 1 /"Oct 12/" anonymous')

    # Tests getting answers: no answers
    await dpytest.message("$getAnswersFor 1", channel=channel)
    assert dpytest.verify().message().contains().content(
        'No answers for Q1')

    # Tests getting answers for nonexistent question
    await dpytest.message("$getAnswersFor 100", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Invalid question number: 100')

    # Test that getting answers does not work outside of QA
    msg = await dpytest.message("$getAnswersFor 1", channel=gen_channel)
    with pytest.raises(discord.NotFound):
        await gen_channel.fetch_message(msg.id)
    # Tests that the bot sent the appropriate message
    assert dpytest.verify().message().contains().content(
        'Please use this command inside the #q-and-a channel.')

    # Tests getting answers with bad input
    with pytest.raises(commands.MissingRequiredArgument):
        await dpytest.message("$getAnswersFor", channel=channel)
    assert dpytest.verify().message().contains().content(
        'To use the getAnswersFor command, do: $getAnswersFor QUESTION_NUMBER\n '
        '(Example: $getAnswersFor 1)')

    # Test archiveQA: questions without answers
    await dpytest.message("$archiveQA",channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q1: What class is this? by anonymous\n'
        'No answers for Q1\n')
    assert dpytest.verify().message().contains().content(
        'Q2: When is the last day of classes? by ' + user.name + '\n'
        'No answers for Q2\n')

    # Test answering a question
    await dpytest.message("$answer 2 \"TestA\"", channel=channel)
    # Test answering a question anonymously
    await dpytest.message("$answer 2 \"TestB\" anonymous", channel=channel)

    # Tests getting answers: question has answers
    await dpytest.message("$getAnswersFor 2", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q2: When is the last day of classes? by ' + user.name + '\n'
        + user.name + ' (Instructor) Ans: TestA\n'
        'anonymous (Instructor) Ans: TestB\n')

    # Test archiveQA: questions with answers
    await dpytest.message("$archiveQA",channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q1: What class is this? by anonymous\n'
        'No answers for Q1\n')
    assert dpytest.verify().message().contains().content(
        'Q2: When is the last day of classes? by ' + user.name + '\n'
        + user.name + ' (Instructor) Ans: TestA\n'
        'anonymous (Instructor) Ans: TestB\n')

    # Test that deleting answers does not work outside of QA
    msg = await dpytest.message("$DALLAF 1", channel=gen_channel)
    with pytest.raises(discord.NotFound):
        await gen_channel.fetch_message(msg.id)
    # Tests that the bot sent the appropriate message
    assert dpytest.verify().message().contains().content(
        'Please use this command inside the #q-and-a channel.')

    # test deleting all answers with bad input: no args
    with pytest.raises(commands.MissingRequiredArgument):
        await dpytest.message("$DALLAF", channel=channel)
    assert dpytest.verify().message().contains().content(
        'To use the deleteAllAnswersFor command, do: $DALLAF QUESTION_NUMBER\n '
        '(Example: $DALLAF 1)')

    # test deleting all answers with bad input
    await dpytest.message("$DALLAF abc", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Please include a valid question number. EX: $DALLAF 1')

    # test deleting all answers for a question with none
    await dpytest.message("$DALLAF 1", channel=channel)
    assert dpytest.verify().message().contains().content(
        'No answers exist for Q1')

    # test deleting all answers
    await dpytest.message("$DALLAF 2", channel=channel)
    assert dpytest.verify().message().contains().content(
        'deleted 2 answers for Q2')

    # Test archiveQA again; ensure proper deletion
    await dpytest.message("$archiveQA",channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q1: What class is this? by anonymous\n'
        'No answers for Q1\n')
    assert dpytest.verify().message().contains().content(
        'Q2: When is the last day of classes? by ' + user.name + '\n'
        'No answers for Q2\n')

    # answer a question
    await dpytest.message("$answer 1 \"TestA\"", channel=channel)
    await dpytest.message("$answer 1 \"TestB\" anonymous", channel=channel)

    # Test that deleting questions does not work outside of QA
    msg = await dpytest.message("$deleteQuestion 1", channel=gen_channel)
    with pytest.raises(discord.NotFound):
        await gen_channel.fetch_message(msg.id)
    assert dpytest.verify().message().contains().content(
        'Please use this command inside the #q-and-a channel.')

    # test deleting questions with bad input: no args
    with pytest.raises(commands.MissingRequiredArgument):
        await dpytest.message("$deleteQuestion", channel=channel)
    assert dpytest.verify().message().contains().content(
        'To use the deleteQuestion command, do: $deleteQuestion QUESTION_NUMBER\n '
        '(Example: $deleteQuestion 1')

    # test deleting question with bad input
    await dpytest.message("$deleteQuestion abc", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Please include a valid question number. EX: $deleteQuestion 1')

    # test deleting a non-existent question
    await dpytest.message("$deleteQuestion 100", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Question number not in database: 100')

    # Test deleting a question
    await dpytest.message("$deleteQuestion 1", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q1 is now a ghost. To see ghost handling options, use the $help command.')

    # Test deleting a ghost question
    await dpytest.message("$deleteQuestion 1", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q1 is already a ghost!')

    # SET UP FOR GHOST TESTING
    await dpytest.message("$ask \"I AM NOT A GHOST\" anonymous", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q3: I AM NOT A GHOST by anonymous')

    # Test archiveQA again; ensure haunting
    await dpytest.message("$archiveQA",channel=channel)
    assert dpytest.verify().message().contains().content(
        'Q1 is a ghost!')
    assert dpytest.verify().message().contains().content(
        'Q2: When is the last day of classes? by ' + user.name + '\n'
        'No answers for Q2\n')
    assert dpytest.verify().message().contains().content(
        'Q3: I AM NOT A GHOST by anonymous\n'
        'No answers for Q3\n')

    # Test that deleting all QAs does not work outside of QA
    msg = await dpytest.message("$deleteAllQA", channel=gen_channel)
    with pytest.raises(discord.NotFound):
        await gen_channel.fetch_message(msg.id)
    assert dpytest.verify().message().contains().content(
        'Please use this command inside the #q-and-a channel.')

    # Test deleting all QAs
    await dpytest.message("$deleteAllQA", channel=channel)
    assert dpytest.verify().message().contains().content(
        'Deleted 3 questions from the database, including 1 ghost questions.')

    # Test deleting all QAs without any questions
    await dpytest.message("$deleteAllQA", channel=channel)
    assert dpytest.verify().message().contains().content(
        'No questions found in database.')

    # Test archiveQA again: deleting all QAs
    await dpytest.message("$archiveQA",channel=channel)
    assert dpytest.verify().message().contains().content(
        'No questions found in database.')

    ####### END OF NEW TESTS

# --------------------
# Tests cogs/reviewQs
# --------------------
@pytest.mark.asyncio
async def test_review_qs(bot):
    # Test review question functionalities
    # create roles and get user
    user = dpytest.get_config().members[0]
    guild = dpytest.get_config().guilds[0]
    await guild.create_role(name="Instructor")
    role = discord.utils.get(guild.roles, name="Instructor")
    await dpytest.add_role(user, role)

    # Test adding a question
    await dpytest.message("$addQuestion \"What class is this?\" \"CSC510\"", member=user)
    assert dpytest.verify().message().contains().content(
        'A new review question has been added! Question: What class is this? and Answer: CSC510.')

    # Test getting a question
    await dpytest.message("$getQuestion", member=user)
    assert dpytest.verify().message().contains().content(
        "What class is this? \n ||CSC510||")

    # Test error
    with pytest.raises(Exception):
        await dpytest.message("$addQuestion \"Is this a test question?\"", member=user)
    assert dpytest.verify().message().contains().content(
        'To use the addQuestion command, do: $addQuestion \"Question\" \"Answer\" \n'
        '(For example: $addQuestion \"What class is this?\" "CSC510")')
