"""
Program 2
Write an user-defined function to add 'ing' at the end of a given string 
(length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged. 
Write set of statements to implement the above said.

"""

def english(word:str):

	if len(word) >= 3:
		
		if word[-3:].lower() == 'ing' :
			word += 'ly'
			return word

		else:
			word += 'ing'
			return word

	return word

	
word = input('Please enter english word.  : ')

print(english(word))