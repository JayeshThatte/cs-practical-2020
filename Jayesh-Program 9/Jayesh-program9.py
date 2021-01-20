"""
Program 9
Create a binary file with roll number,name and marks in 5 subjects.
Input a roll number and update the marks.
Create another new file with the sorted list
based on total in  descending order.
Display the resultant file. 
"""

import pickle


def bubbleSort(lst):
	for i in range(len(lst)): 
  
		for j in range(0, len(lst)-i-1): 
  
			if sum(lst[j][2]) < sum(lst[j+1][2]) : 
				lst[j], lst[j+1] = lst[j+1], lst[j]


def createfile(path:str='Jayesh-program9.bin'):
	data = []

	n = int(input('Number of students : '))

	for i in range(n):
		roll = int(input(f'  Enter roll number of student {i+1} : '))
		name = input('  Enter the name of student : ')

		marks = []
		for j in range(5):
			mark = float(input(f'    Enter mark in subject {j+1} : '))
			marks.append(mark)

		data.append([roll,name,marks])

	with open(path,'wb') as fl:
		pickle.dump(data, fl)


def finder(path:str='Jayesh-program9.bin'):

	tofindroll = int(input('roll no to find : '))
	with open(path,'rb') as fl:
		Students = pickle.load(fl)
		rolls = []

		for student in Students:
			rolls.append(student[0])
		
	data = []
	for student in Students:
		
		Roll = student[0]
		Name = student[1]
		Marks = student[2]

		if tofindroll == Roll:
			print(f'Name : {Name} \t Roll : {Roll} \t Marks : {Marks}')
			Marks = []
			for j in range(5):
				mark = float(input(f'Enter mark in subject {j+1} : '))
				Marks.append(mark)

		if tofindroll not in rolls:
			print('Error ! No such roll exists')
			break

		data.append([Roll,Name,Marks])
	 
	with open(path,'wb') as fl:
		pickle.dump(data,fl)

	return data
 

def sorted(data:list,oldpath:str='Jayesh-program9.bin',newpath:str='Jayesh-program9sorted.bin'):

	with open(oldpath,'rb') as fl:
		data = pickle.load(fl)
		bubbleSort(data)
	with open(newpath,'wb') as fl:
		pickle.dump(data, fl)
		print(data)
		

createfile()
data = finder()
sorted(data)
	
