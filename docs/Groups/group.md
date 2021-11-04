# About $group _(New Project 2 Command)_
This command lets the student view the names of members in their group or the names of members in a specified group. This is useful for students to contact each other and for instructors to find out the names of people in a specific group.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/groups.py).

# Code Description
## Functions
def group(self, ctx, group_num: int = -1): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and an optional group number.

# How to run it?
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. You can view the members in a group by typing `group` and an optional group number.
```
$group GROUP_NUMBER(optional)
```
Successful execution of this command will display the names of members in the group.

![image](https://user-images.githubusercontent.com/32313919/140251786-390e5656-4234-44f9-a663-32fad3d0fcb7.png)
