# The_Eliza_chatbot_Therapist
Eliza is Keyword/rule-based chatbot that mimickes a human psychiatrist. It means that Eliza's responce is not based on
# whole sentence but to a specifice word or a phrase, that is it does on "word-spotting". This program is build on Python and uses "regular expressions" 
# to achive its goal as mimicking human psyhiatrist.
#The program matches user input ( specific keywood  witha scripted responce build by the user. 
#*******************************************************
### Example: Dialogue with Eliza ###
#*******************************************************
# Hello! Welcome to student psychology services
# Please feel free to express yourself
# Please enter 'quit' if you wish to discontinue at any point
#********************************************************
# (Eliza) Hi, My name is Eliza. What is your name?
# (User) >> Bill
# (Eliza) Hello Bill, How are you feeling today?
# (User) >> I am feeling abit off today
# (Eliza) Tell me more!
#(User) >> I dont know why I am sad 
# (Eliza) Did something happened that caused you to be sad?
# (User) >> family issue, i guess
# (Eliza) Tell me more about your family.
# (User) >> quit
# (Eliza) See you soon, take care.
#*********************************************************
# Eliza is a chatbot developed in 1966 by German computer Scientist Joseph Weizenbaum, with aim at tricking its user
# by making them believe they are have conversation with real human being.
# For instance in above example Eliza picked up keyword 'sad" and responded with a follow-up question "Did something happened that caused you to be sad?'
# The alogorithm used in this programming is called rule-based alogorithm, which uses predefined answere based on user's input
# The most important part is setting the rules or search patterns, which is achived using "Regular Expression".
# "Regular expression" or "regexp" A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, 
# using a specialized syntax held in a pattern.
# Here we have mainly divided the program in 4 steps
## 1) Building a dictionay that is used to transform the pronouns from first-person to second-person.
## 2) Building a dictionary that contain keys and list values. 
# The keys of the dictionary represents that possible patterns of words (using regex) and sentences in the input that the user may enter
## 3) The greeting method and vaidation , it is important as it is the first dialogue the user will see.
## 4) The main program that executes Eilza.
# libaries used are "re" - regular expression, "random"- for ramdon selection, "nltk"- for tokenizing.
