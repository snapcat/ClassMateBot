# About $pin _(Modified Command in Project 2)_
This command lets the student to pin a message from the discord channel to their private pinning board.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/pinning.py)

# Code Description
## Functions
addMessage(self, ctx, tagname: str, *, description: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, tagname of the pinned message, and the description of the pinned message.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'pin' pass in all the parameters as a space separated inputs in the following order:
tagname and description.
```
$pin TAGNAME DESCRIPTION
$pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder
```
Successful execution of this command will pin the message for the specific user.

![image](https://user-images.githubusercontent.com/32313919/140243037-8e4c192c-5842-4fd9-85b0-6cccaf3f74ab.png)
