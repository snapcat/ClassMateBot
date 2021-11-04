# About $unpin _(Modified Command in Project 2)_
This command lets the student to delete a pinned message from their private pinning board.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/pinning.py).

# Code Description
## Functions
deleteMessage(self, ctx, tagname: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the tag-name of the pinned message.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'unpin' and the tagname of the message you want to unpin.
```
$unpin TAGNAME 
$unpin HW 
```
Successful execution of this command will unpin the message with the tagname for the specific user.

![image](https://user-images.githubusercontent.com/32313919/140254980-48641eed-7cd0-4eba-8481-3b8537679823.png)
