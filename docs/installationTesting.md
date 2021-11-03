# Installation and Testing Guide 
### Create a Discord Bot
To create a Discord Bot, you must:
* have a [Discord Account](https://discord.com/login)
* have a Discord server for the bot
* create a Discord bot in the [Developer Portal](https://discord.com/developers/applications) by [following instructions here](https://realpython.com/how-to-make-a-discord-bot-python/). **DO NOT ADD to your server yet**

### Run ClassMate Bot
*Please also see the database setup guide to set up database.*  
To run the ClassMate Bot:
1. Ensure you have the following installed:
    * [Python 3](https://www.python.org/downloads/) 
    * [pip](https://pip.pypa.io/en/stable/installation/)
2. Clone this repo onto your local machine
    ```
    git clone https://github.com/SE21-Team2/ClassMateBot.git
    cd ClassMateBot
    ```
3. In the repository directory, run `pip install -r src/requirements.txt`
4. Create a `.env` file with your Bot Token and add this file to your .gitignore.  
 **Discord will automatically regenerate your token if you accidentally upload it to Github.**
    ```
    # .env
    DISCORD_TOKEN={your-bot-token}
    GUILD={your-guild-name}
    DATABASE_URL={your-database-url}
    ```

    NOTE: Run the bot before inviting it to your server in order for auto-initiate commands to run
    
    This includes:
    * Creating Roles (Verified, Unverified, Instructor)
    * Adding server owner to `Verified` Role
    * Creating Bot channels
5. Run `python src/bot.py` to start the bot
6. Invite the bot to your server ([Follow instructions here](https://realpython.com/how-to-make-a-discord-bot-python/))
    * NOTE:  When using the OAuth2 URL Generator, make sure you check the box which gives your bot Administrative permissions



### Run Tests
This bot is tested using pytest and [dpytest](https://dpytest.readthedocs.io/en/latest/index.html). To run tests on the ClassMate Bot, run `pytest` in the root directory.
