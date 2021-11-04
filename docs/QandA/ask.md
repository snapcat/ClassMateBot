# About $ask _(New Project 2 Command)_
This command lets users ask a question in the #q-and-a channel. The questions are automatically numbered and can be asked anonymously or display the author.

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/qanda.py).

# Code Description
## Functions
askQuestion(self, ctx, qs: str, anonymous=''): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the question string, and the anonymous option.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #q-and-a channel, enter the command `ask` and type the question in quotes. If you want the
  question to be displayed anonymously, you can add the option `anonymous` to the end of the
   command.
```
$ask "QUESTION" anonymous_<optional>_
$ask "When is the exam?" anonymous
$ask "When is the project due?"
```
Successful execution of this command will delete the user's original message and the bot will
 send a new message with the question.

![image](https://user-images.githubusercontent.com/32313919/140245147-80aca7ff-525a-4cfb-89d0-df5d10afd691.png) 