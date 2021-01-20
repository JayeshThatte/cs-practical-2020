"""
Program 1
Write an user-defined function to display randomly chosen few letters
of a word from list of words stored in a list. Word and letters are 
chosen in random. Ask the user to guess the word. 
Motivate with proper message and award points to the user
and display the same. Write a program to implement 
the above said.

"""

import random
point = 0

def cal_score(words:list,word:str):
	global point

	randomword = random.choice(words)
	print(randomword)

	if word == randomword:
			print("word is matched !. ",word)
			point += 1
			return point

	return 0


words = eval(input("enter the list of words : "))

while True:
		
	word = input("input a word : ")
	score = cal_score(words, word)
	print("your score : ",score)

	ch=input("do u want to continue Y or N").lower()
	if ch not in ['y','yes']:
		break