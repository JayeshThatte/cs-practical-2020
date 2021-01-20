#Jayesh B
"""
Program 8
Create a binary file with name and roll number.
Search for a given roll number and display the name,
if not found display appropriate message."""


import pickle

def writer(filepath:str):
	with open(filepath,"wb") as file:
		n=int(input('Enter number of students:'))
		Students = []
		for i in range(n):
			roll=int(input('Enter roll number:'))
			name=input('Enter name of student:')
			record=[roll,name]
			Students.append(record)

		pickle.dump(Students,file)


def finder(filepath:str):
	tofindroll = int(input('roll no to find'))
	print(filepath)
	with open(filepath, 'rb') as file:
	   Students = pickle.load(file)
	rolls  = []
	for student in Students:

		Name = student[1]
		Roll = student[0]
		rolls.append(Roll)
		if tofindroll == Roll:
			print(f'Name : {Name} \t Roll : {Roll}')
	if tofindroll not in rolls:
		print('Error ! No such roll exists')


writer(r'Jayesh-program8.bin')
finder(r'Jayesh-program8.bin')