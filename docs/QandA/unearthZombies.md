# About $unearthZombies _(New Project 3 Command)_

Assigns ghost status to all manually deleted questions in case there is a need to restore them. Instructor only.

Note: to create a zombie, manually delete a question in the Q&A channel.

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
unearthZombieQs(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
the #q-and-a channel and enter the command `$unearthZombies`.

`$unearthZombies`

Successful execution of this command will DM the user the number of zombies discovered.

Note: BananaBot is also a ClassMateBot

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/unearthZombies/zombie1.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/unearthZombies/zombie2.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/unearthZombies/zombie3.png?raw=true" width="500">