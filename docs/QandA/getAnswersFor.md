# About $getAnswersFor _(New Project 3 Command)_

This command gets a question and all its answers and DMs them to the user.

It will also notify the user if the question has been deleted (zombie) or hidden (ghost). 

```
Zombies are questions that were manually deleted from the channel. They need to be
assigned new message IDs in order to be restored--that is, they need to be reposted.
Ghosts are questions that were deleted (or hidden) with the deleteQuestion command.
Because their message IDs remain the same, their contents can just be unhidden.
```

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/cogs/qanda.py).

# Code Description
## Functions
getAllAnsFor(self, ctx, num): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the number of the question to retrieve.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
the #q-and-a channel and enter the command `$getAnswersFor QUESTION_NUM`.

```
$getAnswersFor QUESTION_NUM
$getAnswersFor 3
```

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/getAnswersFor/answersfor1.png?raw=true" width="500">

Successful execution of this command will DM the user the question and all its answers.

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/getAnswersFor/answersfor2.png?raw=true" width="500">


