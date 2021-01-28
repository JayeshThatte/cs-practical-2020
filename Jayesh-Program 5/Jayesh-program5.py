"""
Program 5
Write a program to convert an arithmetic expression 
which is in infix notation into postfix notation using stack.
Accept the arithmetic expression as input and
display the resultant expression in postfix notation
"""

infix = input('Infix : ').replace(' ','')
postfix = ''
precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
items = []
size = -1
	
def push(value):
	global items,size
	items.append(value)
	size+=1


def pop():
	global items,size
	if size == -1:
	   return 0
	
	size-=1
	return items.pop()


def seek():
	global items,size
	if size == -1:
	   return False

	return items[size]

def isOperand(i):
	return i.isalnum()


def infixtopostfix (expr):
	global items,size

	postfix=""
	print('postfix expression after every iteration is: ')
	print('Stack' '\t','postfix')
	print(expr)

	for i in expr:
		if(len(expr)%2==0):
			print("Incorrect infix expr")
			return False

		elif(isOperand(i)):
			postfix +=i

		elif(i in '+-*/^'):
			while(len(items)and precedence[i]<=precedence[seek()]):
				postfix+=pop()
			push(i)

		elif i == '(':
		   push(i)
		   
		elif i == ')':
			o=pop()
			while o!='(':
			   postfix +=o
			   o=pop()

	while len(items):
		if(seek()=='('):
		   pop()
		else:
		   postfix+=pop()
	return postfix

result=infixtopostfix(infix)

if (result!=False):
	print("the postfix expr of :\n",infix,"\n is \n",result)