# About $updatepin _(Modified Command in Project 2)_
This command lets the student to update a pinned message with a new link from the discord channel to their private pinning board.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/pinning.py).

# Code Description
## Functions
updatePinnedMessage(self, ctx, tagname: str, *, description: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, tagname of the old pinned message, and the new description given by the student.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'updatepin' and pass in the tagname and new description of the message.
```
$updatepin TAGNAME DESCRIPTION
$updatepin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890814489480531969 HW8 reminder
```
Successful execution of this command will update the description of the pinned message.

![image](https://user-images.githubusercontent.com/32313919/140256002-0ae1f0c6-b84a-43a4-9f83-42356d47cc7b.png)
