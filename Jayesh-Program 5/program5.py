op = ['+','-','*','/','(',')','^']
precedence={'^':3,'*':2,'/':2,'+':1,'-':1}

def infixtopostix(exp):
	stack = []
	output = ''
	for ch in exp:
		if ch not in op:
			output = output + ch
		elif ch == '(':
			stack.append('(')
		elif ch == ')':
			while stack and stack[-1] != '(':
				output += stack.pop()
			stack.pop()
		else:
			while stack and stack[-1] != '(' and precedence[ch] <= precedence[stack[-1]]:
				output += stack.pop()
			stack.append(ch)
	while stack:
		output += stack.pop()
	return output

expression = input('Infix expression : ')
print('postfix expression : ',infixtopostix(expression))