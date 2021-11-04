# About $answer _(New Project 2 Command)_
This command lets users answer a question in the #q-and-a channel. The answers are automatically appended to the question and the role (Instructor/Student) of the sender will be shown. The user can choose to display their name or answer the question anonymously. 

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/qanda.py).

# Code Description
## Functions
answer(self, ctx, num, ans, anonymous=''): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the question number that is being answered, the answer string, and the anonymous option.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #q-and-a channel, enter the command `answer` along with the question number and answer text in quotes. If you want the answer to be displayed anonymously, you can add the option `anonymous` to the end of the command.
```
$answer QUESTION_NUM "ANSWER" anonymous(optional)
$answer "The project is due on Nov 4" anonymous
$answer "The final essay is due on Dec 3"
```
Successful execution of this command will delete the user's original message and the bot will
 append the answer to the question it refers to. 

![image](https://user-images.githubusercontent.com/32313919/140245276-e2752e1b-eea0-4998-9dcc-2f6c6df6dac4.png)