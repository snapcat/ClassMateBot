# Project 2 Changes
## Additions
### Question and Answer Commands
The new question and answer commands allow students to ask questions that are automatically numbered. Both students and instructors can answer the question which will be attached to the original answer. Please see [/docs/QandA](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/QandA) for more details.

### Review Questions Commands
The new review questions commands allow instructors to add review questions for students to use as a study resource. Students can get the questions in a random order and view the hidden answers whenever they are ready. Please see [/docs/QandA](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/ReviewQs) for more details.

### Cloud Deployment
The bot can now be run through a Heroku dyno, allowing for better bot up-time and consistency and removing the inconvenience of forcing someone to run the bot locally on their own computer.

### Multi-server Support
Previously, the bot would only work for a single Discord server, which creates obvious problems with scaling the app to a general-purpose bot. We added functionality to allow the bot to store different data for different Discord servers, allowing the bot to be used in multiple servers concurrently.

## Modifications

### Database
Previously, all persistent data was stored in local files and each action would overwrite the entirety of data files. However, this approach suffers at scale, where datasets are large and operations are done frequently and concurrently. We transitioned persistent storage to use a PostgreSQL instance hosted through the Heroku cloud platform, to solve these issues.

## Documentation
This version includes a more detailed [Installation and Testing Guide](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/InstallationTesting.md) including the new database and cloud setup instructions.
