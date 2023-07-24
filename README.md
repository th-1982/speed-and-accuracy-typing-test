# Speed and Accuracy Typing Test
(Developer: Theresa Wolff)

![Mockup image]

[Live webpage]

## Table of Content


1. [Introduction](#Introduction)
2. [Project Goals](#Project-Goals)

   i. [User Goals](#User-Goals)

   ii. [Site Owner Goals](#Site-Owner-Goals)
3. [User Experience](#User-Experience)

   i. [Strategy](#Strategy)

   * [Target Audience](#Target-Audience)
   * [User Requirements & Expectations](#User-Requirements-&-Expectations)
   * [User Stories](#User-Stories)

   ii. [Scope](#Scope)
   * [Initial Stage](#Initial-Stage)
   * [Future Additions](#Future-Additions)

   iii. [Structure](#Structure)

   iv. [Flowchart](#Flowchart)

   v. [Surface](#Surface)
   * [Color Scheme](#Color-Scheme)
   * [Font](#Font)

   vi. [Features](#Features)
   * [Main Menu](#Main-Menu)
   * [Information Sections](#Information-Sections)
   * [Scoresheet Sections](#Score-Sheet-Sections)
   * [Testing Section](#Testing-Section)
   * [Exit Test](#Exit-Test)
   * [Future Additions](#Future-Additions)

4. [Technologies Used](#Technologies-Used)

   i. [Language](#Languages)

   ii. [Frameworks & Tools](#Frameworks-Tools)

   iii. [Helpful Sites](#Helpful-Sites)
5. [Testing and Validation](#Testing-&-Validation)

   i. [PEP8 Python Linter](#Pep8-ci-Python-Linter)

   ii. [HTML Validation](#HTML)

   iii. [CSS Validation](#CSS)

   iv. [Lighthouse Testing](#Lighthouse)

   v. [User Stories](#User-Stories)

   vi. [Manual Testing](#Manual-Testing)
6. [Bugs & Fixes](#Bugs-&-Fixes)
7. [Deployment & Development](#Deployment-&-development)
8. [Google Sheet Access](#google-sheet-access)
9. [Credits](#Credits)


## Introduction

The Speed and Accuracy Typing Test is a program designed to allow users to test their typing skills, measure their typing speed and accuracy, and save their results to a Google Sheets spreadsheet using the Google Sheets API. It also allows the users to access information such as reading test instructions and tips on improving their skills and score, viewing old scores, deleting their score sheet, and exiting the program. The program is designed in Python and is run through a terminal window.


## Project Goals

### User Goals
* The site's users want to test their typing skills to measure their typing speed and accuracy.
* The user wants to view instructions for effectively using the program and taking the test.
* The user wants to choose a level and start the typing test.
* The user wants to create a score sheet by signing up with a username to save their results and track their progress.		

### Site Owner Goals
* The site owner aims to offer a typing test program to help users measure and improve their typing skills.
* The site owner desires to provide typing Tips and allow users to save their scores.
* The site owner's goal is to encourage users to practice and improve their typing speed and accuracy using the program.
* The owner's goal is to enable the user to return to the test to retest their skill and review previous results.			

## User Experience

### Strategy

#### Target Audience
* Users are interested in testing, monitoring, and improving their speed and accuracy typing skills.
* Users are entering a field of work where typing is essential and who are trying to improve this skill.			

#### User Requirements and Expectations
* Include clear instructions on how to use the program effectively and process flow.
* Simple, easy, and intuitive navigation system.
* Differently, difficulty levels suit their typing skills.
* Scores are to be saved and accessible for future reference. 
* Error handling and immediate feedback on results.

#### User Stories

##### First-time User
As a first-time user, I want to ...
1. ... read test instructions.
2. ... quickly and intuitively move through the test
3. ... know Tips to improve my score and my typing skills.
4. ... sign up with a unique username to save my score.
5. ... select a difficulty level for the typing test.
6. ... see a random paragraph to type accurately and quickly.
7. ... understand how my score fits in with standard averages.
8. ... be able to type the paragraph and receive the test results
9. ... save my results for future reference.


##### Returning Users
As a returning user, I want to ...
1. ... log in using my existing username to access my saved test scores.
2. ... see and access my previous results.
3. ... delete a prior scoresheet if needed.
4. ... take another typing test and save the new test scores.
5. ... see the progress over time in improving my typing skills.

##### Site Owner
As the site owner, I want users to ...
1. ... provide clear instructions and Tips to guide users in using the program.
2. ... provide multiple difficulty levels to cater to users with varying typing skills.
3. ... ensure the accuracy of test results and avoid any potential bugs.
4. ... develop an application that is easy and simple to use.
5. ... handle errors effectively to provide a smooth user experience.
6. ... encourage users to improve their typing skills, save their scores and return to the program.

### Scope

#### Initial Stage

At the early stage, the application will include a main menu where the user can choose from a few options to obtain information, such as instructions and information on improving their typing skills. The user can select a difficulty level (beginner, intermediate, Advanced) for the typing test. The users can take a typing test by typing a random paragraph. The user can also opt to signup, create a username, and use a score sheet to record results; they can review old results and delete a previously developed and populated score sheet. The users can save their test scores to a Google sheet spreadsheet with their username. Then the user will be able to run the test and see immediate feedback in the form of a typing speed in characters/minutes and words/minute as well as a percentage accuracy.										

#### Future Additions

Currently, a Python library called 'Wonderworks' creates a short string of sentences for the user to copy into the terminal window. The sentences are, for the most part, nonsensical and serve the purpose of testing the user's ability to type text by copying it from the terminal window. In a future edition of the application, the developer would like to add Leaderboard to display the top scorers or highest typists on a Leaderboard based on their previous test results. Practice Mode will also be added in the future, where users can practice typing without the pressure of being timed. User Settings will also be added to customize the appearance and behavior of the typing test according to their preferences. Finally, I will also like to calculate efficiency in addition to accuracy.

### Structure

The site's structure consists of a one-page website display containing a terminal window. The Speed and Accuracy Typing Test is run in the terminal window. Above the terminal window, the heading 'Speed and Accuracy Typing Test' is displayed, and a button allows the user to restart the program as many times as desired.

### Flowchart/Skeleton

The following flow chart was created using LucidChart to illustrate the approximate flow of the program and the choices the user can make.

![Flowchart](docs/testing.md/Flowcharts.jpeg)

