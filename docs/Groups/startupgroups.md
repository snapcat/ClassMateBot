# About $startupgroups _(New Project 2 Command)_
This command lets the user set up the roles required for the grouping. This is required as a part of the group making/joining/leaving functionality.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/groups.py).

# Code Description
## Functions
def startupgroups(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called.

# How to run it?
In any channel of the server, you can set upp the roles for the group by typing `startupgroups`.
```
$startupgroups
```
Successful execution of this command will create 100 unassigned group roles for the users in the server.

![group demo](https://user-images.githubusercontent.com/89809302/140447516-76271758-a52d-423f-b342-cdfc13359ce3.png)
