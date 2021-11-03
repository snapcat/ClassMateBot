<p align="center"><img width=20.5% src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/neworange.png"></p>
<h1 align="center" >ClassMate Bot</h1>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.8+-yellow.svg)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5539956.svg)](https://doi.org/10.5281/zenodo.5539956)
![Build Status](https://github.com/SE21-Team2/ClassMateBot/actions/workflows/main.yml/badge.svg)
![GitHub issues](https://img.shields.io/github/issues/shikhanair/TeachersPetBot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/SE21-Team2/ClassMateBot)
![Lines of code](https://img.shields.io/tokei/lines/github/SE21-Team2/ClassMateBot)
[![codecov](https://codecov.io/gh/SE21-Team2/ClassMateBot/branch/main/graph/badge.svg)](https://codecov.io/gh/SE21-Team2/ClassMateBot)

<p align="center">
  <a href="#dart-basic-overview">Basic Overview</a>
  ::
  <a href="#orange_book-description">Description</a>
  ::
  <a href="#arrow_down-installation">Installation</a>
  ::
  <a href="#computer-commands">Commands</a>
  ::
  <a href="#earth_americas-future-scope">Future Scope</a>
  ::
  <a href="#pencil2-contributors">Contributors</a>
  
</p>

---

## :dart: Basic Overview

This project helps to improve the life of students, TAs and teachers by automating many mundane tasks which are sometimes done manually. ClassMateBot is a discord bot made in Python and could be used for any discord channel.

---

## :orange_book: Description

There are three basic user groups in a ClassMateBot, which are Students, Professor and TAs. Some basic tasks for the bot for the students user group should be automating the task of group making for projects or homeworks, Projection deadline reminders, asking questions, getting questions for review etc. For TAs it is taking up polls, or answering questions asked by the students. 


Our ClassMateBot focuses on the student side of the discord channel, i.e. currently it focuses on the problems faced by the students while using these discord channels.

The user stories covered here would be more concerned about the activities for the channel for Software Engineering class in North Carolina State University for the Fall 2021 semester.

---

### 1 - Student Verification
Once the new member joins the server, before giving them the access to the channels there is a need to get the real full name of the member to map it with the discord nick name. This mapping can later be used for group creation, voting and so on. To do this we first assign the unverified role to the new comer and then ask them to verify their identity using $verify command. If that goes through, the member is assigned a student role and has full access to the server resources. The bot then welcomes the member and also provides important links related to the course. A little example is provided below.
![$verify Jane Doe](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/verify.gif)

### 2 - Project Voting
The most important task in the upcoming semester that the bot automates is Project Voting which takes place at the end of the month of September and October. Our ClassMateBot allows the student to vote for a particular project which they would like to work on in the coming cycle. This task if done manually could be tedious as the students would have to wait for the TAs or Professor to announce which project they would be getting if voting is done manually. But the bot automates this process and would give out the results as soon as all the students have voted for their choices. A little example is provided below.
![$vote HW](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/vote.gif)

### 3 - Deadline Reminder
Next important thing our project covers is the Deadline reminder feature of our bot. Whenever a homework or project deadline is close the bot itself sends out a reminder to all the students so that they could submit their work on time. This feature also lets the students add other reminders along with the scheduled ones. For example, HW4 is due on 7th october, along with that the student is working on different assignments or homeworks of other subjects then they could add the other reminders too so that they are in touch with all their pending work. A little example is provided below.
![$addhw CSC510 HW2 SEP 25 2024 17:02](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/addhomework.gif)

### 4 - Personally Pinning Messages
Another problem that the students face is that they cannot pin the important messages which they could come back to if they need so. This could be done through the bot as the students could send in the link of the message they would want to pin and the bot would do that. This way all the students could pin the messages personally through the bot. The pinned messages of other students would not be visible to the current user as we have added the validation of only showing the reminders added by the user not by other students. A little example is provided below.
![$pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/pin.gif)

### 5 - Group Creation
Another unique and useful feature of our ClassMateBot is that it helps the students in the process of group making for their projects. Through this feature the bot could help the students to identify other members of the class who have the same requirements and acts as a medium to connect them initially. Afterwards, they can talk to each other in any way possible. This feature is also helpful for times when a person is randomly assigned to a group then the members could ask the bot to connect them with the new member and this would not only save time for the students but also, saves effort as many times students do not have their names as their usernames on discord. Through this students can join, leave or connect with others. A little example is provided below. 
![$join HW](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/join.gif)

### 6 - Question and Answer **(New Project 2 Commands)**
A common usage for our current class Discord is for students to ask questions about the course. It is helpful for the questions to be numbered and for the answers to be attached to the question so it be easily found. Some students may feel more comfortable asking and answering questions anonymously. It is also helpful for users to know if the question is answered by a student or instructor. This feature keeps the questions and answers all in one channel so it does not clutter other channels and can be more easily viewed. 

### 7 - Review Questions **(New Project 2 Commands)**
An essential part of studying is going over questions related to the exam topics. This feature allows instructors to add review questions and students to get random review questions. To enhance its effectiveness, the answers to the review questions are hidden as a *spoiler* that students can choose to unveil when they are ready. 

---


## :arrow_down: Installation
To install and run the ClassMate Bot, follow instructions in the [Installation Guide](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/installation.md).

---

## :computer: Commands
For the newComer.py file

:open_file_folder: [$verify command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Verification/verify.md)

For the voting.py file

:open_file_folder: [$projects command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Voting/projects.md)

:open_file_folder: [$vote command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Voting/vote.md)

For the deadline.py file

:open_file_folder: [$add_homework command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/add_homework.md)

:open_file_folder: [$change_reminder_due_date command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/change_reminder_due_date.md)

:open_file_folder: [$clear_all_reminders command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/clear_all_reminders.md)

:open_file_folder: [$course_due command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/course_due.md)

:open_file_folder: [$delete_reminder command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/delete_reminder.md)

:open_file_folder: [$due_this_week command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/due_this_week.md)

:open_file_folder: [$due_today command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/due_today.md)

:open_file_folder: [$list_reminders command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Reminders/list_reminders.md)

For the pinning.py file

:open_file_folder: [$pin command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/PinMessage/pin.md)

:open_file_folder: [$unpin command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/PinMessage/unpin.md)

:open_file_folder: [$pinnedmessages command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/PinMessage/pinnedmessages.md)

:open_file_folder: [$updatepin command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/PinMessage/updatepin.md)

For the groups.py file

:open_file_folder: [$group command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Groups/group.md)

:open_file_folder: [$join command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Groups/join.md)

:open_file_folder: [$remove command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/Groups/remove.md)

For the qanda.py file 

:open_file_folder: [$ask command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/QandA/ask.md) **(New Project 2 command)**

:open_file_folder: [$answer command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/QandA/answer.md) **(New Project 2 command)**

For the reviewqs.py file 

:open_file_folder: [$addQuestion command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/ReviewQs/addQuestion.md) **(New Project 2 command)**

:open_file_folder: [$getQuestion command](https://github.com/SE21-Team2/ClassMateBot/blob/main/docs/ReviewQs/getQuestion.md) **(New Project 2 command)**

---

## :earth_americas: Future Scope
[Project 3](https://github.com/SE21-Team2/ClassMateBot/projects/2) suggested tasks are located in the Projects tab. 

---

## :pencil2: Contributors for Project 2

<table>
  <tr>
    <td align="center"><a href="https://github.com/TanyaChu"><img src="https://github.com/tanyachu.png" width="75px;" alt=""/><br /><sub><b>Tanya Chu</b></sub></a></td>
    <td align="center"><a href="https://github.com/SteveJones92"><img src="https://github.com/SteveJones92.png" width="75px;" alt=""/><br /><sub><b>Steven Jones</b></sub></a></td>
    <td align="center"><a href="https://github.com/shikhanair"><img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/shikhanair.png" width="75px;" alt=""/><br /><sub><b>Shikha Nair</b></sub></a></td>
    <td align="center"><a href="https://github.com/alexsnezhko3"><img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/alexsnezhko3.png" width="75px;" alt=""/><br /><sub><b>Alex Snezhko</b></sub></a></td>
    <td align="center"><a href="https://github.com/prdhnchtn"><img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/prdhnchtn.png" width="75px;" alt=""/><br /><sub><b>Pradhan Chetan Venkataramaiah</b></sub></a></td>
  </tr>
</table>

---

## :pencil2: Contributors for Project 1

<table>
  <tr>
    <td align="center"><a href="https://github.com/War-Keeper"><img src="https://avatars.githubusercontent.com/u/87688584?v=4" width="75px;" alt=""/><br /><sub><b>Chaitanya Patel</b></sub></a></td>
    <td align="center"><a href="https://github.com/wevanbrown"><img src="https://avatars.githubusercontent.com/u/89553353?v=4" width="75px;" alt=""/><br /><sub><b>Evan Brown</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/kunwarvidhan"><img src="https://avatars.githubusercontent.com/u/51852048?v=4" width="75px;" alt=""/><br /><sub><b>Kunwar Vidhan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sunil1511"><img src="https://avatars.githubusercontent.com/u/43478410?v=4" width="75px;" alt=""/><br /><sub><b>Sunil Upare</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/salvisumedh2396"><img src="https://avatars.githubusercontent.com/u/72020618?s=96&v=4" width="75px;" alt=""/><br /><sub><b>Sumedh Salvi</b></sub></a><br /></td>
  </tr>
</table>

