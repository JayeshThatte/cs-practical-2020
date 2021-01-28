"""
Program 4
Write a menu driven Python program to implement push, pop
and display operations in a stack with books details 
using a list data-structure.

"""

STACK = []
Count = 1
OPERATIONS = {}

def push(data:list):

	STACK.append(data)


def pull():

	if len(STACK):
		return STACK.pop()

	return "Underflow"
	

def operations(ch):

	global Count
	op = 'Operations'

	if ch == 1:
		op = 'Push'

	if ch == 2:
		op = 'Pull'
	
	cur_stack = list(STACK) 
	data = {Count:[op,list(cur_stack)]}
	
	OPERATIONS.update(data)
	Count += 1


while True:
	ch = int(input("1. Push :  \n2. Pull :  \n3. Display Operations :  \n"))
	if ch == 1:
		
		name = input('Name of book : ')
		price = float(input('Price of book : '))
		author = input('Author : ')
		data = [name,price,author]
		push(data)
		
	if ch == 2:
		
		data = pull()
		print(data)

	if ch == 3:
		print(OPERATIONS)

	operations(ch)
	
	ch = input('Add another book ? y/n : ').lower()
	if ch not in ['yes','y']:
		break