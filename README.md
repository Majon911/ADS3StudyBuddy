# README.TXT

Version 1.0.2

What is StudyBuddy?

StudyBuddy is an application in which you can find a tutor within your universities structue. You provide your details and details about the problem you need to get help for and our algorithm analyses your needs and chooses a most suitable tutor for you. Tutors are chosen upon scores - a point metric system upon which our algorithm chooses most suitable tutors.


How to use StudyBuddy?

It is pretty easy and can be done in a few stepes:
1) Make sure you have python installed on your computer, if not install it from here: https://www.python.org/downloads/
2) Download the "ADS Project 3.py" from this repository.
3) Run the app by clicking on it follow the prompts inside.


What should I provide inside the StudyBuddy application?

For now, 3 things only, that is: the year of studies you are on, the field in which the question posted is and the bachelor you are doing. After that is correctly provided StudyBuddy will return a list of tutors in the systems list, fitted to your need by the algorithm. Currently available categories are:

Years - From 1 to 4
Fields - STATISTICS, MATH, LAW, BUSINESS, FINANCE, MENTORSHIP, OTHER (Note: Needs to be provided in CAPS, cat. other will search amongst all other fields.)
Degree - BBA, BDBA, BA, IR, BLL, BAM (Note: Needs to be provided in CAPS, as for now only those bachelors available.)


How does the algorithm work?

The algorithm calculates a score depending how much the tutor fits the necessary profile, if he/she is an the same degree, specializes in the same field and if they are on the same or older year of studies then you. The number of questions previously answered and the time active on the platform in months also are taken into account by the algorithm. The most suitable tutor is returned on the top of the list, with less suitable going downwards. 


My tutor list is empty, what's wrong?

This means there is no tutor in our database suitable to help you, the tutor list is limited for now, but will expand in future.
