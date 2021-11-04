# About $verify
This command verifies the user by getting their full name, storing this with their username in the database, and then granting access to the guild channels

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/bot.py) and [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/newComer.py).

# Code Description
## Functions
1. def on_guild_join(guild): <br>
This function gets called when the ClassMateBot joins a new guild. It will check if the required roles (Instructor, verified, and unverified) exist in the guild, and if they do not, will create them with the correct permissions. The function then gives the guild owner these Instructor and verified roles, and every other member will be given the unverified role. Note: the bot must be running *before* it is added to a new guild in order for this function to run.

2. def on_member_join(member): <br>
This function gets called when a new member joins the guild. It sends a DM to the new member asking him/her to verify with appropriate instructions. It takes as arguments the object of the member who has joined the server.

3. def verify(self, ctx, *, name: str = None): <br>
This command is used to get the full name of the user and assign user the verified role. It takes as arguments the values provided by the constructor through self, context in which the command was called and full name of the user. It will then store the guild, username, and verified name of the user in the name_mapping table in the database. Once this information is stored, the bot will remove the "unverified" role from the user and replace it with the "verified" role, allowing the user to interact within the guild.

# How to run it? (Small Example)
Let's say that you join the server that has the Classmate Bot active and online, you won't have the access to the channels as you will be assigned some unverified role. You will receive a DM from the Classmate Bot to verify yourself to get access to the channels with appropriate instructions. All you have to do is 
enter the command '$verify' pass in your full name as a parameters as a space seperated inputs.
```
$verify your_full_name
$verify Jane Doe
```
Successful execution of this command will assign you some verified role and give you the access to the channels. You will also receive a welcome message from ClassMateBot with important links related to the course.

![$verify Jane Doe](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/verify.gif)
