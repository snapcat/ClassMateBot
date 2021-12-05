# About $poll _(New Project 3 Command)_

This command allows the user to create a simple reaction poll with thumbs up, thumbs down, and unsure reactions.

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/polling.py](https://github.com/CSC510-Group-25/ClassMateBot/tree/main/cogs/polling.py).

# Code Description
## Functions
poll(self, ctx, *, qs=''): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and a question qs.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. From any channel,
 enter the command `$poll QUESTION`.

```
$poll QUESTION
$poll What do you think about cats?
```
Successful execution of this command will create a reaction poll.

Note: BananaBot is also a ClassMateBot

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/polling/poll1.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/polling/poll2.png?raw=true" width="500">