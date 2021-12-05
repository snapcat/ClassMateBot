# About $dewhitelist _(New Project 3 Command)_

Command that adds removes a word or sentence from the censor whitelist. Instructor only.

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [bot.py](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/bot.py).

# Code Description
## Functions
dewhitelistWord(ctx, *, word=''): <br>
This function takes as arguments the context in which the command was called, and a word or sentence to 
 remove from the whitelist.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #instructor-commands channel and enter the command `$dewhitelist WORD`.

```
$dewhitelist WORD
$dewhitelist vodka
$dewhitelist a lot of words
```
Successful execution of this command will remove a word or sentence from the list of words that will not be censored by the bot.

Note: BananaBot is also a ClassMateBot

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/profanity/filterdemo1.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/profanity/filterdemo2.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/profanity/vodka.png?raw=true" width="500">

<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/profanity/filterdemo3.png?raw=true" width="500">