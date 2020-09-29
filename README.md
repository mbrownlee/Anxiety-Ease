# Anxiety-Ease

<img src="https://raw.githubusercontent.com/mbrownlee/Anxiety-Ease-Client/master/src/AnxietyEaseLogo.png" alt="logo" width="200"/>

Anxiety Ease is a Djnago REST API to companion with Anxiety Ease Client. 

## About the Project 
Many people are afflicated with anxiety - whether it be situational or full blown anxiety disorder. It is estimated 18% of US adults have Anxiety Disorder and many more deal with situational anxiety stemming from every day life. We are living in times of uncertain economy, social media stress, poor sleep habits, work stress, family stress, political upheaval, and more recently a global pandemic. Anxeity Ease is a self help app of calming activites so an individual might be able to divert an anxiety attack. Users are presented with different activites that have proven effective in helping others deal with anxiety: deep breathing, a grounding technique, progressive muscle relaxation, and positive facts about anxiety. After participating in an activity, the user is given the opportunity to rate the effectiveness of the activity and to take notes. The user can choose to come back to that later if they aren't feeling calm yet. The notes section allows the users to make note of what triggered the anxiety, how they felt before and during, and anything else relavent. THis allows users to be aware of what might trigger their anxiety in the future as well as lets them track information to discuss their anxiety with their doctor or therapist if they feel it is a problem.

Anxiety Ease is intended to be a mobile app so that users can always have it available in their pocket when they begin to feel anxious.


<img src="https://raw.githubusercontent.com/mbrownlee/Anxiety-Ease/master/anxietyapp/images/Screen%20Shot%202020-09-29%20at%202.42.29%20PM.png" alt="logo" height="450"/>

Anxiety Ease is not meant to treat or diagnose anyone who suffers from anxiety. It is purely for self help.

## Set Up

1. Clone Anxiety Ease by running: git clone https://github.com/mbrownlee/Anxiety-Ease in your terminal
2. Next, cd into the directory then run the following commands in your terminal:
3. pip install -r requirements.txt
4. python manage.py migrate
5. mython manage.py loaddata anxietyapp/fixtures
6. python manage.py runserver This will open the project on http://localhost:3000


![alt text](https://raw.githubusercontent.com/mbrownlee/Anxiety-Ease/master/anxietyapp/images/Screen%20Shot%202020-09-09%20at%201.31.01%20PM.png)
