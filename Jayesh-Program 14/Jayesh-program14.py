"""
Program 14
Write a Python program to write a Python list of lists to a csv file.
After writing the CSV file read the CSV file and display the content. 
List consists itemnumber, itemname, price, brand of all item
available in the shop.

"""
import csv
csv_columns=['itemnumber', 'itemname', 'price', 'brand']

with open('Jayesh-itemdict.csv','w',newline='') as fl:
	itemdata = []

	while True:
		ch = input('Add  item ? y/n : ').lower()
		if ch not in ['y','yes']:
			break

		itemnumber = int(input(f'id of item {count} : '))
		itemname = input(f'Name of item {count} : ')
		price = int(input(f'Price of item {count} : '))
		brand = input(f'brand of item {count} : ')
		
		tempdata = [itemnumber, itemname, price, brand]
		itemdata.append(tempdata)

	writer = csv.writer(fl)
	writer.writerow(csv_columns)

	for data in itemdata:
		writer.writerow(data)

with open('Jayesh-itemdict.csv','r',newline='') as fl:
	reader = csv.reader(fl)
	for row in reader:
		print(row)