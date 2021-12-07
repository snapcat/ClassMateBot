# About $overdue _(New Project 3 Command)_

This command lists all overdue reminders/assignments. 

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/dealine.py](https://github.com/CSC510-Group-25/ClassMateBot/tree/main/cogs/deadline.py).

# Code Description
## Functions
oevrdue(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and the context in which the command was called and sends a private message to
with all assignments that are past the due date. 

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #reminder channel, enter the command $overdue

```
$overdue
```
Successful execution of this command will send a message with all over due reminders.

<img width="666" alt="Screen Shot 2021-12-04 at 10 02 21 AM" src="https://user-images.githubusercontent.com/78971563/144714572-795322dd-a29c-4a1d-8fd4-5c15acd6f41a.png">
