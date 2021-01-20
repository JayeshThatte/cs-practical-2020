#Jayesh B
"""
Program 7

Read a text file and display the number of
vowels/ consonants/ uppercase/ lowercase characters
in the file. 

"""
with open(r'Jayesh-program7.txt','r') as fl:
	uppercases = [chr(i) for i in range(ord('A'),ord('Z')+1)]
	lowercases = [chr(i) for i in range(ord('a'),ord('z')+1)]
	vowels = ['a','e','i','o','u']
	UPPER_COUNT =LOWER_COUNT = VOWELS_COUNT =  CONSONANTS_COUNT= 0
	
	lines = fl.read()
	for letter in lines:
		if letter in uppercases:
			UPPER_COUNT+=1
		if letter in lowercases:
			LOWER_COUNT +=1
		if letter.lower() in vowels:
			VOWELS_COUNT +=1
		if letter.lower() in lowercases:
			if letter.lower() not in vowels:
				CONSONANTS_COUNT+=1

print('Upper cases :',UPPER_COUNT)
print('Lower cases :',LOWER_COUNT)
print('Vowels  :',VOWELS_COUNT)
print('Consonants  :',CONSONANTS_COUNT)
