# About $reviveGhost _(New Project 3 Command)_

Unhides a ghost (question hidden with the deleteQuestion command) or restores a manually deleted question (zombie) to the channel. Instructor only.

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
restoreGhost(self, ctx, num): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the number of the question to restore.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #q-and-a channel and enter the command `$reviveGhost <num>`.

```
$reviveGhost <num>
$reviveGhost 3
```

Successful execution of this command will restore a question to the channel.

Note: BananaBot is also a ClassMateBot

Restoring a zombie:

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/reviveghost/reviveghost1.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/reviveghost/reviveghost2.png?raw=true" width="500">


Restoring a ghost:

```
$reviveGhost <num>
$reviveGhost 2
```

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/reviveghost/reviveghost1b.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/reviveghost/reviveghost1c.png?raw=true" width="500">