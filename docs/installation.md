# Setup/Installation Guide
To set up and run the ClassMate Bot:
1. Ensure you have the following installed:
    * [Python 3](https://www.python.org/downloads/) 
    * [pip](https://pip.pypa.io/en/stable/installation/)
2. Clone this repo onto your local machine
    ```
    git clone https://github.com/SE21-Team2/ClassMateBot.git
    cd ClassMateBot
    ```
3. In the repository directory, run `pip install -r src/requirements.txt`
4. Create a `.env` file in your project's root directory (we will put things into it later)
5. Create a Discord bot and get its token:
   1. Create a [Discord Account](https://discord.com/login)
   2. Create a Discord server for the bot to run in
   3. Create a Discord bot in the [Developer Portal](https://discord.com/developers/applications) by [following instructions here](https://realpython.com/how-to-make-a-discord-bot-python/). Copy the bot's token into the `.env` file:
      ```
      # .env
      DISCORD_TOKEN={your-bot-token}
      ```
6. Set up the database. ClassMate Bot currently uses [Heroku](https://www.heroku.com/) as a cloud platform for running the bot, and uses a PostgreSQL database hooked up to the Heroku application that runs the bot.
   1. [Create a Heroku account](https://signup.heroku.com/login).
   2. Sign in to Heroku and create a new Heroku application.
   3. Add the Heroku Postgres extension (in the `Resources` tab of the Heroku application web UI).
   4. Acquire the PostgreSQL database connection URL (In the web UI inside the Heroku app, navigate to `Resources > Heroku Postgres > Settings > View Credentials...` and note the URI). Copy this URI into the `.env` file; your `.env` file should now look like this:
      ```
      # .env
      DISCORD_TOKEN={your-bot-token}
      DATABASE_URL={your-database-url}
      ```
7. Start the bot. From the project root directory, run `python3 src/bot` (or `python src/bot.py` on Windows)
8. Invite the bot to your server ([Follow instructions here](https://realpython.com/how-to-make-a-discord-bot-python/)) (**Please ensure the bot is running in order for server intialization to happen properly**)
    * NOTE:  When using the OAuth2 URL Generator, make sure you check the box which gives your bot Administrative permissions
9. You should now be able to input commands and get responses from the bot as appropriate.

## Running the bot through Heroku

In order to run the bot through Heroku, first ensure that the bot is connected to, and deployed from, your GitHub repo. In the Heroku web UI for your app, navigate to `Deploy > GitHub` and connect the app to your ClassMateBot fork. After the app is deployed, navigate to `Resources` and click the pencil icon, flip the switch to on, and click confirm, within the `worker` dyno.

## Working with the Heroku PostgreSQL database
Working directly with the PostgreSQL database can be done through the PostgreSQL command line interface `psql`.

Setup:
1. [Install PostgreSQL on your system](https://www.postgresql.org/download/) (details differ depending on OS) and ensure you can access the `psql` program through a terminal.
2. Set up the heroku command line tool:
   1. [Install the heroku command line tool](https://devcenter.heroku.com/articles/heroku-cli)
   2. Authenticate to the Heroku CLI: `heroku login`
   3. Connect the Heroku CLI to your Heroku app: from your project's root directory run `heroku git:remote -a <name-of-your-app>`

You should now be able to connect to the Heroku PostgreSQL database through the `psql` client by running `heroku pg:psql` (if this step fails you may have not installed PostgreSQL correctly. Documentation for `psql` can be found [here](https://www.postgresql.org/docs/13/app-psql.html)

## Running Tests
This bot is tested using pytest and [dpytest](https://dpytest.readthedocs.io/en/latest/index.html). To run tests on the ClassMate Bot, run `pytest` in the root directory.
