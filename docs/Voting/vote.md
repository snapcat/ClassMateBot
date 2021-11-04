# About $vote _(Modified Command in Project 2)_
This command lets the groups vote on projects that they want to be working on next.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/voting.py)

# Code Description
## Functions
vote(self, ctx, project_num : int): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the project number argument.

# How to run it? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. All you have to do is 
enter the command 'vote <number>'.
```
$vote <NUMBER>
$vote 2
```
Successful execution of this command will return a message saying you have voted for a project.

![image](https://user-images.githubusercontent.com/32313919/140250549-8de514c0-d411-41fe-976c-6b43c7bd1edf.png)
  
It is simple enough to change vote by just voting for a different project.
  
![image](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/votechange.gif)
