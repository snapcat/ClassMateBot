# About $deleteQuestion _(New Project 3 Command)_

Would be more accurate to call it hideQuestion.
Delete one question but leave answers untouched. Instructor only.

(assigns ghost status to a question.)


```
Zombies are questions that were manually deleted from the channel. They need to be
assigned new message IDs in order to be restored--that is, they need to be reposted.
Ghosts are questions that were deleted (or hidden) with the deleteQuestion command.
Because their message IDs remain the same, their contents can be unhidden.
```

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/cogs/qanda.py).

# Code Description
## Functions
deleteOneQuestion(self, ctx, num): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the number of the question to delete.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #q-and-a channel and enter the command `$deleteQuestion <num>`.

```
$deleteQuestion <num>
$deleteQuestion 2
```

Successful execution of this command will hide the question and all its answers.

Note: BananaBot is also a ClassMateBot

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/deleteQuestion/deleteq1.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/deleteQuestion/deleteq2.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/deleteQuestion/deleteq3.png?raw=true" width="500">
