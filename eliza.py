##############################################################################################################
# Anugh Shrestha,Sai Gauthami Kuravi, Dilpreet Singh Bedi
# Date- September 19 2020
# Team - Team 8 Section 2
##############################################################################################################
##### INTRODUCTION ####
### Eliza is Keyword/rule-based chatbot that mimickes a human psychiatrist. It means that Eliza's responce is not based on
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
#********************************************************************************************************
##############################################################################################################

import re
import random
from nltk.tokenize import word_tokenize
import time
from datetime import date, datetime
import datetime


##############################################
#replace method:
#input parameters: pattern_1, reponse_1, message_1
#This method takes the input parameters and performs the sub function to replace certain pattern
##############################################
def replace(pattern_1, response_1, message_1):

	sub = re.sub(pattern_1, response_1, message_1)
	return str(sub)

##############################################
#get_date method:
#This method is invoked when the user asks for today's date
#This method returns today's date in the following format:
# 'Today is <today's day>, <today's month> <today's day number> <today's year>'
##############################################
def get_date():
	today = date.today()
	day = date.today().strftime("%A")
	year = date.today().strftime("%Y")
	month = date.today().strftime("%B")
	day_num = date.today().strftime("%d")
	today_day = f"Today is {day}, {month} {day_num} {year}"
	return today_day

##############################################
#pronouns is a dictionary that is used to transform the pronouns from first-person to second-person
#When the program receives the user's input, the code will look the pronoun that is listed in the key of the dictionary
#When the pronoun is found on the key, that particular pronoun will be replace with the pronoun in the corresponding value
##############################################
pronouns = {
	"you": "me",
	"me": "you",
	"your": "my",
	"my" : "your",
	"are": "am",
	"am": "are",
	"i" : "you"
}

##############################################
#possible_response is a dictionary that contain keys and list values.
#The keys of the dictionary represents that possible patterns of words and sentences in the input that the user may enter
#The multi-dimensional list values represents the list of responses to the matching pattern of words and sentences in the input of the user
#When the pattern of words or responses matches a key, it will randomly pull a response from the first array of the multi-dimensinal list
#The second array in the multi-dimenstial list determines if the replace method (defined above) needs to be invoked. If the value is null then,
#the replace method will not be invoked. If the value is not null, the replace method will be invoked.

#For example: if the user's input has the word happy, the program will randomly select either Why are you happy?, 
#What made you happy?, or Oh, do you have an exciting news?

#In the response by the chat bot, {0} gets subsituted with set of word(s) that included after the word of the match pattern
#For example: if the user enters 'it is raining' (which matches the pattern [Ii]t is (.*), the bot might reply back with response that states 
#'Why is it raining?'
##############################################

possible_responses = {
	r'[Hh](ello|i).*' : [['Hey there!', 'Hello', 'Hi', 'Howdy'], []],
	r'\b[Ww]hat is your name?\b' : [['My name is Eliza', 'I am Eliza', 'Eliza'],[]],
	r'(.*)[Tt]oday\'s date(.*)': [[get_date()],[]], #invokes get_date method when it matches the pattern
	r'\b[Ww]hat is today\'s date\??\b': [[get_date()],[]], #invokes get_date method when it matches the pattern
	r'[Ii] am feeling (.*)' : [["Why are you feeling {0}", "Tell me more!", "What made you feel {0}"],[]],
	r'[Ii] am (.*)' :[["Why are you {0}", "How long for you been {0} for", "What caused you to be {0}"],[]],
	r'[Ii] had an?(.*)' :[["Tell me more about the {0}", "How did you have {0}"],[]],
	r'[Ii] have (.*)' : [["Why do you have {0}", "How did you get {0}", "Who/what gave you {0}"],[]],
	r'[Ii] would (.*)' : [["Why would you {0}"],[]],
	r'[Ii]t is (.*)' : [["Why is it {0}", "Is it really {0}?"],[]],
	r'^[Ii] gave (.+) to (.+)' : [["Why would you give -\\1 to \\2?", "Oh, is there a reason you gave -\\1 to \\2 "],["r"]], #invokes replace method
	r'^[Ii] do not like (.+)' : [["Why don't you like -\\1?", "What caused you to not to like -\\1?"],["r"]], #invokes replace method
	r'(.*)[Ll]et us (.*)' : [["Why do you want to {0}", "What is making you want to {0}?"],[]],
	r'(.*)[Hh]omework(.*)': [["What class are you taking?", "Are your classes hard?", "Which university/school do you attend?"],[]],
	r'(.*)[Hh]appy(.*)' : [["Why are you happy?", "What made you happy?", "Oh, do you have an exciting news?"],[]],
	r'(.*)[Gg]ood(.*)' : [["Glad to hear", "Always love good feelings", "Always good to be good :)", "Oh yeah! Good!"],[]],
    r'(.*)[Bb]ad(.*)' : [["Why are you feeling bad?", "Did something happened that made you feel like this?"],[]],
	r'(.*)[Ss]ad(.*)' : [["Why are you sad?", "What made you sad?", "Did something happened that caused you to be sad?"],[]],
	r'(.*)[Ss]ick(.*)' : [["Are you getting enough sleep?", "Bowl of soup is the best home remedy!", "Call the doctor if it gets worse"],[]],
	r'(.*)[Ss]tresse?d?(.*)' : [["What is causing you stress?", "Deep breathing relieves stress", "It will be over soon. Just breathe :)"],[]],
	r'(.*)([Pp]upp(y|ies))': [["The fur buddies are the best buddies", "Ah! So precious!"],[]],
    r'(.*)([Ll]onely|[Aa]lone)(.*)': [["Why do you feel Lonely", "What makes you think you are alone "],[]],
    r'(.*)([Ll]oved?)(.*)': [["Why do you feel this way", "What makes you think like this "],[]],
    r'(.*)[Ss]orry (.*)':[[" No apology is needed.","Why do you feel to say sorry?"],[]],
    r'(.*)[Aa]lone (.*)':[[" Why do you think you are alone?.","You can share with me"],[]],
    r'(.*)[Ff]amily(.*)': [["Tell me more about your family.","Why does it makes you feel this way?"],[]],
    r'(.*)[Ff]ather(.*)': [["How is your relationship with your father?","Tell me more about your relation"],[]],
    r'(.*)[Mm]o(ther|m)(.*)': [["How is your relationship with your mom?","Tell me more about your relation"],[]],
    r'(.*)[Ss]isters?(.*)': [["How is your relationship with your sister?","Tell me more about your relation"],[]],
    r'(.*)[Bb]rothers?(.*)': [["How is your relationship with your brother?","Tell me more about your relation"],[]],
    r'(.*)[Ff]rinds?(.*)': [["How is your relationship with your friends?","Tell me about them"],[]],
	r'(.*)[Bb]ecause of (.*)':[["Do you want to talk more about that"],[]],
    r'(.*)[Aa]lways (.*)':[["Can you think of a specific example?"],[]],
    r'(.*)[Ff]avorites?(.*)' : [["speaking of favorites... I'd like to learn more about you"],[]],
    r'(.*)[Ss]uffering(.*)' : [["How can I help you?", "Do you need any help?"],[]],
    r'(.*)[Yy]es(.*)': [["Thats positive!", " You seem confident about it"],[]],
    r'(.*)[Hh]ow(.*)': [["What do you think?", "Why do you ask?"],[]],
    r'(.*)[Nn]ot?(.*)': [["Are you sure", " I guess, it needs time", "There should be a reason behind this"],[]],
    r'(.*)[Hh]ome(.*)':[["Its a safe place, right", "Home is warm"],[]],
    r'(.*)[Cc]omplicated(.*)': [["What does that mean","Why do you think that","Tell me more about it"],[]],
    r'(.*)[Yy]es(.*)': [["Thats positive!", " You seem confident about it"],[]],
    r'(.*)[Nn]ot?(.*)': [[" I understand", " I guess, it needs time", "There should be a reason behind this"],[]],
    r'(.*)[Hh]ome(.*)': [["Its a safe place, right", "Home is warm"],[]],
    r'(.*)[Cc]omplicated(.*)': [["What does that mean","Why do you think that","Tell me more about it"],[]],
    r'(.*)([Pp]upp(y|ies))': [["The fur buddies are the best buddies", "Ah! So precious!"],[]],
	r'(.*)([Dd]ogs?)': [["The fur buddies are the best buddies", "Ah! So precious!"],[]],
	r'(.*)([Pp]ets?)': [["It's always good to have pets"],[]],
	r'(.*)([Cc]ats?)': [["The fur buddies are the best buddies", "Ah! So precious!"],[]],
	r'(.*)([Kk]ittens?)': [["The fur buddies are the best buddies", "Ah! So precious!"],[]],
	r'(.*)[Yy]ou are (.*)': [["Why do you think I am {0}?", "Why are you asking if I am {0}?", "Do you think I am {0}?"],[]],
	r'(.*)[Yy]ou(.*)': [["We should be talking about you, not me :)", "Let's focus on talking about you!", "Maybe we should talk about your feelings"],[]],
	r'(.*)' : [["Go on!","Tell me more"],[]]
}



##############################################
# greeting() method
# This method greets the user with a greeting message and asks the user for his/her name
# This method also kicks off the conseling session by asking how they are feeling today
##############################################
def greeting():
	#correct_name is a boolean variable that will be used to determine whether the name of the user matches the pattern.
	#As described later in the code, the name of the user must contains alphabetical values
	correct_name = False 
	name = ""

	#The loop contains the methods to greet and receive input from the user. This loop will continue asking for the user
	while not correct_name:   
		#There is a nested while loop which is designed to keep asking user for their name when they provide an empty response
		#The name variable stores the name of the user that is provided by the user themselves
		while name == "":
			greeting_message = "\n***************************************************\n"
			greeting_message += "Hello! Welcome to student psychology services\n"
			greeting_message += "Please feel free to express yourself\n"
			greeting_message += "Please enter 'quit' if you wish to discontinue at any point\n"
			greeting_message += "***************************************************\n"
			print(greeting_message) #prints the greeting_message that is declared above
			name = input("Hi, My name is Eliza. What is your name?\n>>") #Throughout the program input() methods will be used to receive user's input
			name = str(name.strip()) 
			
			#Checks whether the user enters quit, Quit, quit;, or Quit; The program exits when the user's response matches the word
			quit_pattern = r'[Qq]uit;?'  
			quit = re.match(quit_pattern,name) 

			#if else statement
			#Checks if user entered a blank input for their name. 
			#If the input is blank then it will print out the message stating that the user did not provide their name
			if name == "": 
				print("Please give me your name! :)")
				continue

			#if the user's input is not empty then it checks whether or not the user entered the word quit
			#if the user did not enter the word quit then it will check the input for validation through greeting_validation method
			elif not quit:
				#greeting_validation method checks whether the user's input matches the expected pattern for name
				#the method returns incorrect if it does not matches the pattern
				greeting_name = greeting_validation(name, check_y=True) 
				if greeting_name == "Incorrect":
					correct_name = False
					print("Lets try that again!")
				else:
					correct_name = True

			#if the user enters the word quit then it calls the bye() method which prints a goodbye message to the user
			#and exits out from the program
			else:
				
				bye()
				exit()

	#Then the conseling session is kicked off by asking the user how they are feeling.
	#Keeps asking user the same question about feelings when they enter an empty input
	message = ""
	while message == "":
		#The question concatenates the user's name that was received from the input above
		message = input(f"Hello {greeting_name}, How are you feeling today?\n>>") 
		if message == "":
			print("You have to tell me how you feel! :)")
	return message #returns the input from the user

##############################################
#greeting_validation()
#input: name (string), check_y (boolean)
#Validates if the name of the user is provided in proper pattern
##############################################
def greeting_validation(name, check_y):
	
	#the input of the user is split by spaces
	name_count = name.split()

	#if else statement
	#Counts if the name input has more than one word
	#if it has more than one word then it must match the pattern 'My name is ' followed by user's name.
	#It checks if the name is in alphabetical format
	#if it does not match the pattern then it will return the word 'Incorrect' 
	#if it does not match the pattern then it will keep asking user for the input in the greeting() method 
	#if it matches the pattern then it will return just the user's name
	if (len(name_count) > 1):
		pattern = r'\b[Mm]y name is\b ([A-z].+)'
		x = re.match(pattern,name)
		if x:
			return str(x[1]) 
		else:
			return "Incorrect"
	#if the count if not greater than one then it will check if the input is in alphabetical format
	#Checks if the name is in alphabetical format
	#returns incorrect if it does not matches the pattern
	#the program has the option if this pattern needs to be checked. Hence, check_y parameter determines if this pattern needs to be checked
	else:
		if check_y:
			
			pattern_2 = r'\b([A-z]+)\b'
			y = re.match(pattern_2,name)
			if y:
				return str(y[1])
			else:
				return "Incorrect"


##############################################
#replace_punctuation()
#parameters: user_response
#replaces punctuations in the response provided by the user
#For example: replaces I'm with I am
##############################################
def replace_punctuation(user_response):

	had_pattern = r'[Ii]\'d an?'
	user_response = str(user_response)
	user_response = re.sub(r'[Ii]\'m', "I am", user_response)
	if re.match(had_pattern,user_response):
		user_response = re.sub(r'[Ii]\'d', "I had", user_response)
	else:
		user_response = re.sub(r'[Ii]\'d', r"I would", user_response)
	user_response = re.sub(r'[Ii]\'ve', "I have", user_response)
	user_response = re.sub(r"[Ii]t\'s", "It is", user_response)
	user_response = re.sub(r'[Ll]et\'s', "Let us", user_response)
	user_response = re.sub(r'[Ww]hat\'s', "What is", user_response)
	user_response = re.sub(r'[Dd]on\'t', "do not", user_response)
	#print(user_response)

	return user_response

##############################################
#generate_response()
#parameters: user_response (string)
#This method checks if the user's input matches the pattern that are listed in the possible_response dictionary
##############################################
def generate_response(user_response):

	#check_name method checks if the user enters their name again
	#the detailed description of the method is provided later in the code
	#if the user didn't not enter their name again then it returns the word 'valid'
	#if the user did enter their name again then it returns the message 'Hello <user_name>, How are you feeling today?'
	#the returned message is stored in valid_status variable
	valid_status = check_name(user_response)

	#calls the replace_punctuation method to replace punctuation (description above)
	user_response = replace_punctuation(user_response)
	
	#if valid_status is equal to valid then it loops through the possible_response dictionary to check if the user's input matches the 
	#patterns in the dictionary
	if valid_status == "valid":
		#replace_message = user_response
		#print(f"replace : {replace_message}")
		#for loop is used to loop through possible_response dictionary
		#pattern represents the key where the possible word/sentence patterns are stored
		#reponse represents the list of reponses for the matching corresponding pattern
		for pattern, response in possible_responses.items():
			match = re.match(pattern, user_response) #match method from re module to check whether the user's reponse matches any patterns
			#if there is a match, a random response is choosen from the first list of the multi-dimensional list
			if match:
				#This if else statement determins if replace method needs to be invoked
				#if the length of the second array of the multi-dimensional is greater than the replace method is invoked
				if len(response[1]) > 0 :
					matched_pattern = pattern
					sub_string = random.choice(response[0])
					bot_response = replace(matched_pattern,sub_string,user_response) #replace method invoked
					#Notice: the values in the first lists has a '-'. For example: "Why would you give -\\1 to \\2?"
					#The values are split based on '-'
					bot_reponse_list = bot_response.split("-")
					response_message = bot_reponse_list[0] + evaluate_pronoun(bot_reponse_list[1])
					#response_message = bot_response.format(*[evaluate_pronoun(bot_response)])
				else:
					bot_response = random.choice(response[0]) 
					#when there is a match, it gets the words after the matching pattern is located in the sentence 
					#and sustitues it to the cooresponding reponse that has the symbol {0} 
					s = ""
					for x in match.groups():
						s = s + " " + x

					#evaluate_pronoun method is called to replace the first-person pronoun with second-person pronoun
					response_message = bot_response.format(*[evaluate_pronoun(s)])

				return response_message
	#if the valid_status is not equal to valid then that means the user entered their name again.
	#it will ask the user how they are feeling again.
	else:
		
		reponse_message = valid_status 
		return reponse_message

##############################################
#evaluate_pronoun()
#It converts all the letters to lowercase and splits the words in the sentence by using word_tokenize method
##############################################
def evaluate_pronoun(sentence):

	sentence = sentence.lower()
	tokens = word_tokenize(sentence)
	
	#Loops through all the words and replaces the first-person pronoun with second-person pronoun
	#i is the key and token is the value
	for i, token in enumerate(tokens):
		if token in pronouns:
			tokens[i] = pronouns[token]
	return ' '.join(tokens)

##############################################
#check_name() method
#parameter input
#Checks if the the user entered their name again
##############################################
def check_name(message):
	valid_message = "valid"
	message_1 = message.strip()
	#calls the greeting_validation method with check_y parameter set to false
	#as stated above greeting_validation method returns word 'Incorrect' if it is does not match the pattern
	
	greeting_check = greeting_validation(message, check_y=False)

	#if it does not return 'Incorrect' in this case then it means that the user's input does not represent user's name
	#if it does return 'Incorrect' then the user did input their name
	if greeting_check != None and greeting_check != "Incorrect":
		
		valid_message = f"Hello {message}, How are you feeling today?"
		return valid_message
	return valid_message

##############################################
#bye()
#output's goodbye message for user
#picks a random word from the possible_bye_messages
##############################################
def bye():

	possible_bye_messages = ["It was pleasure talking to you.", "Bye have a nice day.", "See you soon, take care."]
	bye_message = random.choice(possible_bye_messages)
	print(bye_message)

##############################################
#main() method
#main operator of the program
##############################################

def main():

	greeting_message = greeting() #calls greeting method
	last_response = greeting_message
	message = greeting_message

	matching_resonse = False
	last_question = None

	quit_pattern = r'[Qq]uit;?'
	quit = re.match(quit_pattern,message) #checks if the user's input matches the word quit and it stops the program

	#it will keep asking user questions until the user enter the word quit
	while not quit:
		#checks if the user entered a blank input
		if message == "":
			print("You have to tell me something! :)")
			message = input(f"{response_question}\n>>")
			continue
		else:

			if matching_resonse:
				response_question = last_question
			else:
				response_question = generate_response(str(message))#calls the generate_response method declared above
				#print(f"response_question {response_question}")

			message = input(f"{response_question}\n>>") #input function is used to get user's input and stored in message variable
			#print(f"message {message}")

			#checks if the user is repeating themselves
			if last_response == message :
				print("You can't repeat yourself! :)\nPlease response to the response below....")
				last_question = response_question
				matching_resonse = True
			else:
				matching_resonse = False

			#stores every user's input into last_response variable and it is compared with subsequent response to see if they are the same
			last_response = message  
		quit = re.match(quit_pattern,message) #checks if the user's input matches the word quit and it stops the program
	bye()

main()
