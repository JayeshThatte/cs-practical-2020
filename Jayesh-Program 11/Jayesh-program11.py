"""
Program 11
Write a function that reads a text file “story.txt” 
and store alternate words in another file 
after reversing the word. 
Display the content of story.txt and the newly created file.

"""

def story1():
	print('Old File :')
	with open(r'Jayesh-story.txt','r') as target:
		lines = target.readlines()
		words_sep = []
		for line in lines:
			words = [word[-1::-1] for word in line.split(sep=' ')]
			words_sep+= words
		target.seek(0)
		print(target.read())
		words_sep = words_sep[::2]
		return words_sep


def story2(words):
	print('New File :')
	with open(r'Jayesh-alternatestory.txt','w+') as target:
		target.writelines([word+' ' for word in words])
		target.seek(0)
		newfile = target.read()

		print(newfile)   

words = story1()

story2(words)