"""
Program 3

Write a function in Python to combine the contents of two equi-sized 
lists A and B into third list by computing their corresponding elements 
with the formula 2*A[i]+3*B[i]; where value i varies from 0 to N-1 
and transfer the resultant content in the third same sized list.
Lists A & B passed as parameters along with their sizes and the 
function returns the resultant array to the calling place for displaying. 

"""

def combine(A:list ,B:list ,lenA:int, lenB:int):
	
	C=[ ]

	for pos in range(len(A)):
		element = 2*A[pos]+3*B[pos]
		C.append(element)
		
	return C


A = list(eval(input('enter elements of list a : ')))
B = list(eval(input('enter elements of list b : ')))
C = combine(A ,B ,len(A) ,len(B))
print(C)