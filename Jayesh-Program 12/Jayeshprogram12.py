#Jayesh B
"""
Program 12
Write a program that takes a sample of ten phishing e-mails 
(or any text file) and find most commonly occurring word(s) 
"""


def mails(*args):
	uniquewords = set()
	for mail in args:
		
		with open(mail,'r') as target:
			data = []
			lines = target.readlines()
			for line in lines:
				data+=[i for i in line.strip('\n').strip('.').split(sep=' ')]
		
		unique = set(data)
		uniquewords.update(unique)
		
	
	data = []
	for mail in args:
		
		with open(mail,'r') as target:
			
			lines = target.readlines()
			for line in lines:
				data+=[i for i in line.strip('\n').strip('.').split(sep=' ')]
	
	for unique_word in uniquewords:
		print(f'{unique_word} : {data.count(unique_word)}')


mails(r'Jayesh-mail1.txt',r'Jayesh-mail2.txt',r'Jayesh-mail3.txt',r'Jayesh-mail4.txt'\
	  ,r'Jayesh-mail5.txt',r'Jayesh-mail6.txt',r'Jayesh-mail7.txt',r'Jayesh-mail8.txt'\
	  ,r'Jayesh-mail9.txt',r'Jayesh-mail10.txt')
