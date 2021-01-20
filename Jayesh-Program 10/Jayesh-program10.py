"""
Program 10
Remove all the lines that starts with the character `a' in a file
and write it to another file.
Display the contents of Original and copied file

"""

with open(r'Jayesh-program10.txt','r') as target:

	lines = target.readlines()
	newfllines = []
	for line in lines:
		if line[0].lower() == 'a':
		  newfllines.append(line)
	target.seek(0)
	originalfile = target.read()

	print('Original File : ')
	print(originalfile)


with open(r'Jayesh-program10new.txt','w+') as target:
	
	target.writelines(newfllines)
	target.seek(0)
	newfile = target.read()
	print('New File :')
	print(newfile) 
