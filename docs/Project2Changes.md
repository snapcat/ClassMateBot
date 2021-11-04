# Project 2 Changes
## Additions
### Question and Answer Commands
A common usage for our current class Discord is for students to ask questions. The new question and answer commands allow students to ask questions that are automatically numbered. Both students and instructors can answer the question which will be attached to the original answer and they can choose to post anonymously. Please see [/docs/QandA](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/QandA) for more details.

### Review Questions Commands
An essential part of studying is going over questions related to the exam topics. The new review questions commands allow instructors to add review questions for students to use as a study resource. Students can get the questions in a random order and view the hidden answers whenever they are ready. Please see [/docs/ReviewQs](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/ReviewQs) for more details.

### Cloud Deployment
The bot can now be run through a Heroku dyno, allowing for better bot up-time and consistency and removing the inconvenience of forcing someone to run the bot locally on their own computer.

### Multi-server Support
Previously, the bot would only work for a single Discord server, which creates obvious problems with scaling the app to a general-purpose bot. We added functionality to allow the bot to store different data for different Discord servers, allowing the bot to be used in multiple servers concurrently.

## Modifications

### Database
Previously, all persistent data was stored in local files and each action would overwrite the entirety of data files. However, this approach suffers at scale, where datasets are large and operations are done frequently and concurrently. We transitioned persistent storage to use a PostgreSQL instance hosted through the Heroku cloud platform, to solve these issues.

### Usability
Existing commands were improved for usability where there were prior gaps. The following are some of the changes identified to improve the existing commands.

Message Pinning: The pinnedmessages for example had no way to view pinned messages unless you remembered what was the pin tag. If that was forgotten, the message would forever be lost. Also, it was very specific formatting for requiring a link and became tedious to use. The command was made more usable by having only a tag and description, providing ways to find all of the messages, and other changes focused on usability.

Groups: The groups commands allowed a person to join multiple groups. This was limited to one. The command to list groups was $group, so that was changed to $groups and a group command was added to display your group or specific other groups and the members inside. The $remove command was changed to $leave and removes you from your current group (since you are only in one now).

Deadline: The database stores UTC time and trying to put in a time based on your current clock without realizing this would be wrong. Added a command to get the offset needed to get the proper times to input.

Voting: The voting for a project was improved with the output and being able to change a vote, which you could not do previously.

## Documentation
This version includes a more detailed [Installation Guide](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/installation.md) including the new database and cloud setup instructions.
