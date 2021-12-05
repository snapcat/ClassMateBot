<p align="center"><img width=20.5% src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/neworange.png"></p>
<h1 align="center" >ClassMate Bot</h1>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  
[![DOI](https://zenodo.org/badge/426029685.svg)](https://zenodo.org/badge/latestdoi/426029685)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/CSC510-Group-25/ClassMateBot)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Lines of code](https://img.shields.io/tokei/lines/github/CSC510-Group-25/ClassMateBot)
![GitHub repo size](https://img.shields.io/github/repo-size/CSC510-Group-25/ClassMateBot)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c1c81dbe55ac4b9ca27533ec23a8493d)](https://www.codacy.com/gh/CSC510-Group-25/ClassMateBot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=CSC510-Group-25/ClassMateBot&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/CSC510-Group-25/ClassMateBot/branch/main/graph/badge.svg?token=B1E9S0HRRC)](https://codecov.io/gh/CSC510-Group-25/ClassMateBot)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/CSC510-Group-25/ClassMateBot)](https://github.com/CSC510-Group-25/ClassMateBot/pulls)
[![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/CSC510-Group-25/ClassMateBot)](https://github.com/CSC510-Group-25/ClassMateBot/pulls?q=is%3Apr+is%3Aclosed)
[![GitHub issues](https://img.shields.io/github/issues/CSC510-Group-25/ClassMateBot)](https://github.com/CSC510-Group-25/ClassMateBot/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/CSC510-Group-25/ClassMateBot)](https://github.com/CSC510-Group-25/ClassMateBot/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub issues by-label](https://img.shields.io/github/issues-raw/CSC510-Group-25/ClassMateBot/bug?color=red&label=Active%20bugs)](https://github.com/CSC510-Group-25/ClassMateBot/issues?q=is%3Aissue+is%3Aopen+label%3Abug)
[![GitHub closed issues by-label](https://img.shields.io/github/issues-closed-raw/CSC510-Group-25/ClassMateBot/bug?color=green&label=Squished%20bugs)](https://github.com/CSC510-Group-25/ClassMateBot/issues?q=is%3Aissue+label%3Abug+is%3Aclosed)
[![Python application](https://github.com/CSC510-Group-25/ClassMateBot/actions/workflows/main.yml/badge.svg)](https://github.com/CSC510-Group-25/ClassMateBot/actions/workflows/main.yml)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/CSC510-Group-25/ClassMateBot/Python%20application)](https://github.com/CSC510-Group-25/ClassMateBot/actions/workflows/main.yml)
[![Pytest](https://github.com/CSC510-Group-25/ClassMateBot/actions/workflows/pytest.yml/badge.svg)](https://github.com/CSC510-Group-25/ClassMateBot/actions/workflows/pytest.yml)
[![Pylint](https://github.com/CSC510-Group-25/ClassMateBot/actions/workflows/pylint.yml/badge.svg)](https://github.com/CSC510-Group-25/ClassMateBot/actions/workflows/pylint.yml)



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
  ::
  <a href="https://github.com/CSC510-Group-25/ClassMateBot/wiki">Wiki</a>
  
</p>

---

Project 3 demo video:  

Watch it on youtube! https://www.youtube.com/watch?v=KBBqUkOTuSo  

Watch it here:  

https://user-images.githubusercontent.com/89357283/144730581-46b85493-3f5c-4c65-9d3f-fbcfffc729a3.mp4



---


https://user-images.githubusercontent.com/89809302/140442405-e043564d-c946-4116-bb79-e9f8a341da21.mp4

<a href="https://youtu.be/U59HyX21S7k">Watch on YouTube</a>


---

## :dart: Basic Overview

This project helps to improve the life of students, TAs and teachers by automating many mundane tasks which are sometimes done manually. ClassMateBot is a discord bot made in Python and could be used for any discord channel.  

This is Project 3 for the ClassMateBot. Changes are marked below and listed in [Project 3 Changes](https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/docs/Project3Changes.md).

---

## :orange_book: Description

There are three basic user groups in a ClassMateBot, which are Students, Professor and TAs. Some basic tasks for the bot for the students user group should be automating the task of group making for projects or homeworks, Projection deadline reminders, asking questions, getting questions for review etc. For TAs it is taking up polls, or answering questions asked by the students. 


Our ClassMateBot focuses on the student side of the discord channel, i.e. currently it focuses on the problems faced by the students while using these discord channels.

The user stories covered here would be more concerned about the activities for the channel for Software Engineering class in North Carolina State University for the Fall 2021 semester.

---

### 1 - Student Verification
Once the new member joins the server, before giving them the access to the channels there is a need to get the real full name of the member to map it with the discord nick name. This mapping can later be used for group creation, voting and so on. To do this we first assign the unverified role to the new comer and then ask them to verify their identity using $verify command. If that goes through, the member is assigned a student role and has full access to the server resources. The bot then welcomes the member and also provides important links related to the course.  


<img src="https://user-images.githubusercontent.com/32313919/140422661-ee3c4c68-8cb0-4032-b5a6-8192ee98ac10.png" width="500">
<!-- ![image](https://user-images.githubusercontent.com/32313919/140422661-ee3c4c68-8cb0-4032-b5a6-8192ee98ac10.png) -->

### 2 - Project Voting
Voting for projects is a common occurence that many students must endure. With the addition of a voting system, this task is made easier by allowing student groups to place themselves on projects through an easy to use discord system. With the combination of the ClassMateBot grouping system, teams can easily vote their group into a project, switch their votes, or view the full list of projects that have been voted for.  

<img src="https://user-images.githubusercontent.com/32313919/140250549-8de514c0-d411-41fe-976c-6b43c7bd1edf.png" width="350">
<!-- ![image](https://user-images.githubusercontent.com/32313919/140250549-8de514c0-d411-41fe-976c-6b43c7bd1edf.png) -->

<img src="https://user-images.githubusercontent.com/32313919/140250910-3aa8d6cd-000d-4b51-949a-0c60f3464c3b.png" width="350">
<!-- ![image](https://user-images.githubusercontent.com/32313919/140250910-3aa8d6cd-000d-4b51-949a-0c60f3464c3b.png) -->

### 3 - Deadline Reminder **(Updated in Project 3!)**

***Deadlines now send automatic messgages for assignments that are due that day and assignments that are due within the hour!*** Check out more [here](https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/docs/Project3Changes.md)

The next important thing our project covers is the Deadline reminder feature of our bot. Students may add homeworks, links, and due dates using the system, and then view their daily or weekly dues with ease. No longer will a student be vulnerable to those odd submission times like 3:00 PM. See homework specific to one class, due today, or due this week!

<img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/addhomework.gif" width="800">
<!-- ![$addhw CSC510 HW2 SEP 25 2024 17:02](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/addhomework.gif) -->



### 4 - Personally Pinning Messages
Another problem that the students face is that they cannot pin important messages they want to go back to later. With pinned messages, the student can save discord message links easily to point back to prior messages or just leave their own general messages. It is a very easy system to use and could be creatively used by a student in many different ways to promote better classroom success.


<img src="https://user-images.githubusercontent.com/32313919/140243037-8e4c192c-5842-4fd9-85b0-6cccaf3f74ab.png" width="700">
<!-- ![image](https://user-images.githubusercontent.com/32313919/140243037-8e4c192c-5842-4fd9-85b0-6cccaf3f74ab.png) -->




### 5 - Group Creation
Another unique and useful feature of our ClassMateBot is that it helps the students in the process of group making for their projects. Through this feature, the bot could help the students identify other members of the class with similar ideals and acts as a medium to connect them initially. This feature is also helpful for students randomly assigned to a group to connect with the new member which would not only save time, but also, saves effort as many times students do not have their names as their usernames on discord. Through this students can join, leave or connect with others. 



<img src="https://user-images.githubusercontent.com/32313919/140244316-7fac7ce4-32a7-444d-b8cf-b3b8b2d2dea1.png" width="500">
<!-- ![image](https://user-images.githubusercontent.com/32313919/140244316-7fac7ce4-32a7-444d-b8cf-b3b8b2d2dea1.png) -->



Moreover, the group creation feature allows members of the group to join a private text channel to communicate with ease! This works by assigning a role to the user when they join a group and giving them access to the private channel specically for their group, this is especially useful when switching groups because a change in the user's role will automatically revoke access to the private channel. Additionally, the private channels are set up so instructors can help with clarifications directly without having to reach out to them via DMs.


<img src="https://user-images.githubusercontent.com/89809302/140443462-e8a59aae-1235-4a74-8d32-47c77a597a01.png" width="600">
<!-- ![group demo](https://user-images.githubusercontent.com/89809302/140443462-e8a59aae-1235-4a74-8d32-47c77a597a01.png) -->

<img src="https://user-images.githubusercontent.com/89809302/140443855-11b040fb-0e17-4134-9e2e-4dcc903d7ae2.png" width="600">
<!-- ![group demo chg](https://user-images.githubusercontent.com/89809302/140443855-11b040fb-0e17-4134-9e2e-4dcc903d7ae2.png) -->



### 6 - Question and Answer **(Updated in Project 3!)**
A common usage for our current class Discord is for students to ask questions about the course. It is helpful for the questions to be numbered and for the answers to be attached to the question so it be easily found. Some students may feel more comfortable asking and answering questions anonymously. It is also helpful for users to know if the question is answered by a student or instructor. This feature keeps the questions and answers all in one channel so it does not clutter other channels and can be more easily viewed.  

![image](https://user-images.githubusercontent.com/32313919/140245147-80aca7ff-525a-4cfb-89d0-df5d10afd691.png)  
![image](https://user-images.githubusercontent.com/32313919/140245276-e2752e1b-eea0-4998-9dcc-2f6c6df6dac4.png)


### 7 - Review Questions
An essential part of studying is going over questions related to the exam topics. This feature allows instructors to add review questions and students to get random review questions. To enhance its effectiveness, the answers to the review questions are hidden as a *spoiler* that students can choose to unveil when they are ready.  


<img src="https://user-images.githubusercontent.com/32313919/140245925-22769537-ef22-420f-9ed2-b9153a71938e.png" width="600">
<!-- ![image](https://user-images.githubusercontent.com/32313919/140245925-22769537-ef22-420f-9ed2-b9153a71938e.png) -->

### 8 - Polling **(NEW in Project 3!)**

Users can now create polls! Instructor can ask for student opinions.
<img src = "https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/data/proj3media/polling/poll1.png?raw=true"  width = "600">

<img src = "https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/data/proj3media/polling/poll2.png?raw=true"  width = "600">

We can also create Quiz Poll\
<img src = "https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/data/proj3media/polling/quizpoll1.png?raw=true"  width = "600">

<img src = "https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-documentation/data/proj3media/polling/quizpoll2.png?raw=true"  width = "600">


---


## :arrow_down: Installation
To install and run the ClassMate Bot, follow instructions in the [Installation Guide](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/installation.md).

---

## :computer: Commands

General commands in bot.py

:open_file_folder: [$whitelist command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/ProfanityFilter/whitelist.md) **(New Command in Project 3)**

:open_file_folder: [$dewhitelist command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/ProfanityFilter/dewhitelist.md) **(New Command in Project 3)**

:open_file_folder: [$toggleFilter command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/ProfanityFilter/togglefilter.md) **(New Command in Project 3)**

For the newComer.py file

:open_file_folder: [$verify command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Verification/verify.md)

For the voting.py file 

:open_file_folder: [$projects command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Voting/projects.md) 

:open_file_folder: [$vote command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Voting/vote.md) 

For the deadline.py file **(Updated in Project 3!)**

:open_file_folder: [$add homework command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/add_homework.md) **(Updated in Project 3!)**

:open_file_folder: [$change reminder due date command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/change_reminder_due_date.md) **(Updated in Project 3!)**

:open_file_folder: [$clear all reminders command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/clear_all_reminders.md)

:open_file_folder: [$course due command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/course_due.md)

:open_file_folder: [$delete reminder command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/delete_reminder.md)

:open_file_folder: [$due this week command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/due_this_week.md) **(Updated in Project 3!)**

:open_file_folder: [$duetoday command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/due_today.md) **(Updated in Project 3!)**

:open_file_folder: [$listreminders command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/list_reminders.md)

:open_file_folder: [$timenow command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/timenow.md)

:open_file_folder: [$overdue command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/overdue.md) **(New Command in Project 3)**

:open_file_folder: [$clearoverdue command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Reminders/clearoverdue.md) **(New Command in Project 3)**


For the pinning.py file

:open_file_folder: [$pin command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/PinMessage/pin.md) 

:open_file_folder: [$unpin command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/PinMessage/unpin.md) 

:open_file_folder: [$pinnedmessages command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/PinMessage/pinnedmessages.md) 

:open_file_folder: [$updatepin command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/PinMessage/updatepin.md) 

For the groups.py file

:open_file_folder: [$startupgroups command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Groups/startupgroups.md) 

:open_file_folder: [$reset command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Groups/reset.md) 

:open_file_folder: [$connect command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Groups/connect.md)

:open_file_folder: [$groups command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Groups/groups.md)

:open_file_folder: [$group command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Groups/group.md)

:open_file_folder: [$join command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Groups/join.md)

:open_file_folder: [$leave command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Groups/leave.md)

For the qanda.py file **(Updated in Project 3!)**

:open_file_folder: [$ask command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/ask.md) **(Updated in Project 3)**

:open_file_folder: [$answer command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/answer.md) **(Updated in Project 3)**

:open_file_folder: [$DALLAF command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/DALLAF.md) **(New Command in Project 3)**

:open_file_folder: [$getAnswersFor command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/getAnswersFor.md) **(New Command in Project 3)**

:open_file_folder: [$deleteAllQA command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/deleteAllQA.md) **(New Command in Project 3)**

:open_file_folder: [$deleteQuestion command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/deleteQuestion.md) **(New Command in Project 3)**

:open_file_folder: [$archiveQA command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/archiveQA.md) **(New Command in Project 3)**

:open_file_folder: [$spooky command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/spooky.md) **(New Command in Project 3)**

:open_file_folder: [$allChannelGhosts command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/allChannelGhosts.md) **(New Command in Project 3)**

:open_file_folder: [$channelGhost command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/channelGhost.md) **(New Command in Project 3)**

:open_file_folder: [$unearthZombies command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/unearthZombies.md) **(New Command in Project 3)**

:open_file_folder: [$reviveGhost command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/QandA/reviveGhost.md) **(New Command in Project 3)**

For the reviewqs.py file

:open_file_folder: [$addQuestion command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/ReviewQs/addQuestion.md) 

:open_file_folder: [$getQuestion command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/ReviewQs/getQuestion.md) 


For the polling.py file **(All new in Project 3!)**

:open_file_folder: [$poll command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Polling/poll.md)

:open_file_folder: [$quizpoll command](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/docs/Polling/quizpoll.md)



---

## :earth_americas: Future Scope
[Future scope](https://github.com/CSC510-Group-25/ClassMateBot/projects/3) suggested tasks are located in the Projects tab. 


---


## :pencil2: Contributors

### :pencil2: (Fall 2021)

<table>
  <tr>
    <td><a href="https://github.com/CSC510-Group-25/ClassMateBot">Project 3</a></td>
    <td align="center"><a href="https://github.com/etracey7/"><img src="https://avatars.githubusercontent.com/u/78971563?v=4" width="75px;" alt=""/><br /><sub><b>Emily Tracey</b></sub></a></td>
    <td align="center"><a href="https://github.com/peeyush10234/"><img src="https://avatars.githubusercontent.com/u/10905673?v=4" width="75px;" alt=""/><br /><sub><b>Peeyush Taneja</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/jhnguye4/"><img src="https://avatars.githubusercontent.com/u/42051115?v=4" width="75px;" alt=""/><br /><sub><b>Jonathan Nguyen</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/snapcat/"><img src="https://avatars.githubusercontent.com/u/89357283?v=4" width="75px;" alt=""/><br /><sub><b>Leila Moran</b></sub></a><br /></td>
    <td align="center"><a href="https://www.github.com/shraddhamishra7"><img src="https://avatars.githubusercontent.com/u/7471821?v=4" width="75px;" alt=""/><br /><sub><b>Shraddha Mishra</b></sub></a><br /></td>
  </tr>
  
  <tr>
    <td><a href="https://github.com/SE21-Team2/ClassMateBot">Project 2</a></td>
    <td align="center"><a href="https://github.com/TanyaChu"><img src="https://github.com/tanyachu.png" width="75px;" alt=""/><br /><sub><b>Tanya Chu</b></sub></a></td>
    <td align="center"><a href="https://github.com/SteveJones92"><img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/SteveJones92.png" width="75px;" alt=""/><br /><sub><b>Steven Jones</b></sub></a></td>
    <td align="center"><a href="https://github.com/shikhanair"><img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/shikhanair.png" width="75px;" alt=""/><br /><sub><b>Shikha Nair</b></sub></a></td>
    <td align="center"><a href="https://github.com/alexsnezhko3"><img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/alexsnezhko3.png" width="75px;" alt=""/><br /><sub><b>Alex Snezhko</b></sub></a></td>
    <td align="center"><a href="https://github.com/prdhnchtn"><img src="https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/prdhnchtn.png" width="75px;" alt=""/><br /><sub><b>Pradhan Chetan Venkataramaiah</b></sub></a></td>
  </tr>
  
  
 <tr>
   
   <td><a href="https://github.com/War-Keeper/ClassMateBot">Project 1</a></td>
    <td align="center"><a href="https://github.com/War-Keeper"><img src="https://avatars.githubusercontent.com/u/87688584?v=4" width="75px;" alt=""/><br /><sub><b>Chaitanya Patel</b></sub></a></td>
    <td align="center"><a href="https://github.com/wevanbrown"><img src="https://avatars.githubusercontent.com/u/89553353?v=4" width="75px;" alt=""/><br /><sub><b>Evan Brown</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/kunwarvidhan"><img src="https://avatars.githubusercontent.com/u/51852048?v=4" width="75px;" alt=""/><br /><sub><b>Kunwar Vidhan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sunil1511"><img src="https://avatars.githubusercontent.com/u/43478410?v=4" width="75px;" alt=""/><br /><sub><b>Sunil Upare</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/salvisumedh2396"><img src="https://avatars.githubusercontent.com/u/72020618?s=96&v=4" width="75px;" alt=""/><br /><sub><b>Sumedh Salvi</b></sub></a><br /></td>
  </tr>
  
</table>

---



