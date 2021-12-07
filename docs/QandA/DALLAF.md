# About $DALLAF (deleteAllAnswersFor) _(New Project 3 Command)_

This command lets instructors remove all answers for a question in the #q-and-a channel.
Deletes all answers for a question. Instructor only.

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/cogs/qanda.py).

# Code Description
## Functions
deleteAllAnsFor(self, ctx, num): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the number of the question to delete answers for.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
the #q-and-a channel and enter the command `$DALLAF <q_num>`.

Before deletion, archive the question and its answers with
`$getAnswersFor QUESTION_NUMBER`

Or, if it's a ghost or zombie:
`$channelGhost QUESTION_NUMBER` 

```
$DALLAF <q_num>
$DALLAF 7
```

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/dallaf/dallaf1.png?raw=true" width="500">

Successful execution of this command will delete all answers for the question on the channel and in the database, 

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/dallaf/dallaf2.png?raw=true" width="500">

and DM the user the number of answers that were deleted.

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/dallaf/dallaf3.png?raw=true" width="500">

