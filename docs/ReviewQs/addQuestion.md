# About $addQuestion _(New Project 2 Command)_
This command lets instructors add review questions to the system. 

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/reviewQs.py](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/reviewQs.py).

# Code Description
## Functions
addQuestion(self, ctx, qs: str, ans: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the question string, and the answer string.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You enter the command `addQuestion` and type the question and answer in separate quotes. 
```
$addQuestion "QUESTION" "ANSWER"
$addQuestion "What class is this?" "CSC510"
```
Successful execution of this command will add a review question to the database and return a success message.

![image](https://user-images.githubusercontent.com/32313919/140245925-22769537-ef22-420f-9ed2-b9153a71938e.png)