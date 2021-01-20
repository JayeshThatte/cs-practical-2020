#Jayesh B
"""
Program 6

Read a text file line by line
and display each word separated by a #. 
"""

with open(r'Jayesh-program6.txt','r') as fl:
	lines = fl.readlines()
	WORDS = []
	for line in lines:
		words = line.split(sep='#')
		for word in words:
			print(word.strip())
