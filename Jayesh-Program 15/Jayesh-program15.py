"""
Program 15
Write a Python program to write a Python dictionary to a csv file.
After writing the CSV file read the CSV file and display the content. 
Keys in dictionary are bookid, booktitle,author, price, and published year.

"""
import csv
csv_columns=['bookid','booktitle','author','price','published year']

with open('Jayesh-itemdict.csv','w',newline='') as fl:
	itemdata = []

	while True:
		ch = input('Add  book ? y/n : ').lower()
		if ch not in ['y','yes']:
			break

		bookid = int(input(f'Book id of book {count} : '))
		booktitle = input(f'Name of book {count} : ')
		author = input(f'Author of book {count} : ')
		price = int(input(f'Price of book {count} : '))
		year = int(input(f'published year of book {count} : '))

		data = {'bookid':bookid,\
				'booktitle':booktitle,\
				'author':author,\
				'price':price,\
				'published year':year}

		itemdata.append(data)

		
	writer=csv.DictWriter(fl,fieldnames=csv_columns)
	writer.writeheader()

	for data in itemdata:
		writer.writerow(data)

	print("the files succesfully created ")

with open('Jayesh-itemdict.csv','r',newline='') as file:
	reader = csv.reader(file)

	for row in reader:
		print(row)