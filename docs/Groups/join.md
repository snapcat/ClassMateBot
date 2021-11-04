# About $join _(Modified Command in Project 2)_
This command lets the student add their name to the group member list. This is used to ensure that all students can get into a group and making sure no duplicates occur in the process

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/groups.py).

# Code Description
## Functions
join(self, ctx, group_num: int: <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the group number argument.

# How to run it? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. All you have to do is 
enter the command 'join <group_number>'.
```
$join GROUP_NUMBER
$join 2
```
Successful execution of this command will return a message saying you have joined the group.

![image](https://user-images.githubusercontent.com/32313919/140244316-7fac7ce4-32a7-444d-b8cf-b3b8b2d2dea1.png)