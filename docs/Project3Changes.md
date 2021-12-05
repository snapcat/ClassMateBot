# ClassMateBot Project 3 Changes
## Project 2 vs Project 3

## New Additions

### New commands and tasks
We added various new commands. These are mentioned below along with their description.

## Profanity filter changes

Previously, upon detecting profanity, the bot would delete the original message and replace it with "{User} says: \**" for all to see, thereby preventing users without admin privileges from deleting or editing their messages.  

Due to a bug, the censor did not function properly. Instead of single words being censored, the entire message would be replaced. 

Example: "I really wanna talk about vodka but it's censored for some reason" results in this being posted to the channel:

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/data/proj3media/profanity/filtering.png?raw=true" width="300">

This bug was fixed in project 3, and while posts containing profanity are still deleted from the channel if the filter is active, the bot now sends the user a DM instead of reposting the message.

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/data/proj3media/profanity/filterdm.png?raw=true" width="500">

### New profanity filter commands:

Previously, the user had no control over what the bot censored. Words such as kill, len, slope, or strip were censored without any way to de-censor them, which is obviously problematic for anyone working with programming languages or attempting to explain how to calculate the slope of a line.

To allow greater control over profanity filtering, we implemented the following commands:  

* $toggleFilter: toggles the profanity filter on/off, instructor/admin only
* $whitelist (word): adds a word or sentence to the whitelist, instructor/admin only
* $dewhitelist (word): removes a word or sentence from the whitelist, instructor/admin only

The documentation for these commands can be found here: https://github.com/CSC510-Group-25/ClassMateBot/tree/group25-documentation/docs/ProfanityFilter

## Q&A Changes

We greatly expanded Q&A functionality and made several quality improvements.

Previously, Q&A only had two commands: ask and answer. In order to ask/answer a question anonymously, the user would have to type:  
`$ask "Question" anonymous`  
`$answer 1 "Answer" anonymous`

which became very tedious after a while. For the sake of convenience, this was changed so that the user can type "anon" or "anonymous."  

In addition, we added the following input controls:
* Users cannot ask empty/blank/whitespace only questions.
* Users can only answer valid questions. That is to say, the number of the question must be valid. 
* Users can't answer with empty/blank/whitespace only strings.
* Users can't answer deleted or hidden questions.

### New Q&A commands:

* $getAnswersFor (num) -- get all answers for a question. Ignores ghosts (hidden questions) and zombies (manually deleted questions).
* $DALLAF (num) -- deletes all answers for a question. Instructor only.
* $archiveQA -- sends all questions and answers to the user via DM. Ignores ghosts and zombies.
* $deleteAllQA -- deletes all questions and answers from the database and channel. Also cleans up ghosts and zombies. Instructor only.
* $deleteQuestion (num) -- deletes a single question from the channel and leaves a database ghost. (It hides the question.) Instructor only.

We also added commands to help maintain database integrity. 

* $spooky: Used to check the number of zombies and ghosts in the channel. Fun for students, useful for instructors.
* $channelGhost (num): Get the ghost question and its answers with that number. Also works for zombies and non-ghost questions. (Basically, getAnswersFor but doesn't ignore ghosts or zombies.) Instructor only.
* $allChannelGhosts: get all channel ghosts via DM. Instructor only. (Does not work with zombies).
* $reviveGhost (num): Restores a ghost or zombie question and all its answers. Instructor only.
* $unearthZombies: finds all zombies (manually deleted questions) and assigns ghost status. Instructor only.

Documentation can be found here: https://github.com/CSC510-Group-25/ClassMateBot/tree/group25-documentation/docs/QandA

## Reminder changes

### $addhw and $changeduedate
* Now instuctor only.
* Date input is more flexible. (ie both of these are now valid - NOV 30 2050, 11/30/2050)
* Users can add a timezone to the time as well

### $duetoday and $duethisweek
* Shows time delta between now and duedate so users don't have to manually covert systen time to local
* Dates are formatted with timezome (ie NOV 11 2050 12:00+0000)

### New Reminder commands:

* $overdue: lists all overdue reminders
* $clearoverdue: deletes overdue reminders

### Reminder Tasks
* Reminder task that runs once per day at 8am to give reminders of anything due that day
* Reminder task that runs once per hour to give reminder of anything due that hour

## Polling

This is an entirely new feature that we introduced. Test coverage is currently 89% for this module.

The user may now create polls.

$poll command creates a simple reaction poll with thumbs up, thumbs down, or unsure. Documentation:
https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/docs/Polling/poll.md

$quizpoll command creates a multi-reaction poll with options A-F. Documentation:
https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/docs/Polling/quizpoll.md


## Other changes

### Error handlers

We added error handlers to everything to prevent the bot from breaking.

### Tests

We added 70 (exhaustive!) tests for Q&A and coverage increased from 35% to 95%.

eadlines/reminders: added 9 tests. Coverage increased from 62% to 75%

Pinning.py: added 6 tests. Coverage increased from 64% to 83%

groups.py: added 5 tests, Coverage increased from 52% to 67%

Overall, we increased code coverage from 63% to 89%.

