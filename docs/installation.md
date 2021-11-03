# Installation Guide 
### Create a Discord Bot
To create a Discord Bot, you must:
* have a [Discord Account](https://discord.com/login)
* have a Discord server for the bot
* create a Discord bot in the [Developer Portal](https://discord.com/developers/applications) by [following instructions here](https://realpython.com/how-to-make-a-discord-bot-python/). **DO NOT ADD to your server yet**

### Setup Cloud Database and Server
ClassMate Bot currently uses [Heroku](https://www.heroku.com/) as a cloud platform for running the bot, and uses a PostgreSQL database hooked up to the Heroku application that runs the bot.

To access the cloud database credentials to run the bot locally:
1. [Create a Heroku account](https://signup.heroku.com/login).
2. Gain access to the class-mate-bot Heroku app. Contact Alex Snezhko (alexsnezhko89@gmail.com) to request access to the app.
3. Acquire the PostgreSQL database connection URL (In the web UI inside the class-mate-bot Heroku app, navigate to `Resources > Heroku Postgres > Settings > View Credentials...` and note the URI to use later during bot setup).

To gain complete ownership of the app and transfer the app to your fork of ClassMateBot:
 - Please contact alexsnezhko89@gmail.com to request a complete transfer of ownership to the Heroku app.
 - In order to run the bot through Heroku, first ensure that the bot is connected to, and deployed from, your GitHub repo. In the web UI, navigate to `Deploy > GitHub` and connect the app to your ClassMateBot fork. After the app is deployed, navigate to `Resources` and click the pencil icon, flip the switch to on, and click confirm, within the `worker` dyno.

Working directly with the PostgreSQL database can be done through the PostgreSQL command line interface.

Setup:
1. [Install PostgreSQL on your system](https://www.postgresql.org/download/) (details differ depending on OS) and ensure you can access the `psql` program through a terminal.
2. Set up the heroku command line tool:
   1. [Install the heroku command line tool](https://devcenter.heroku.com/articles/heroku-cli)
   2. Authenticate to the Heroku CLI: `heroku login`
   3. Connect the Heroku CLI to the class-mate-bot app: `heroku git:remote -a class-mate-bot`

You should now be able to connect to the Heroku PostgreSQL database through the `psql` client by running `heroku pg:psql` (if this step fails you may have not installed PostgreSQL correctly. Documentation for `psql` can be found [here](https://www.postgresql.org/docs/13/app-psql.html)


### Run ClassMate Bot Locally
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
4. Create a `.env` file with your Bot Token and PostgreSQL database URL (from the cloud database setup), and add this file to your .gitignore.  
 **Discord will automatically regenerate your token if you accidentally upload it to Github.**
    ```
    # .env
    DISCORD_TOKEN={your-bot-token}
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
