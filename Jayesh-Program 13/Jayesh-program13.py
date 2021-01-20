#Jayesh B
"""
Program 13
Write a program that creates a csv file with details department id,
department name, manager id and branch_location.
Read the content of the file created and display
department name and manager-id of all departments stored in csv file.

"""
import csv
csv_columns=['department id', 'department name', 'manager-id','branch_location']
with open('Jayesh-itemdict.csv','w',newline='') as fl:
	itemdata = []

	while True:
		ch = input('Add  book ? y/n : ').lower()
		if ch not in ['y','yes']:
			break

		departmentid = int(input(f'departmentid id {count} : '))
		departmentname = input(f'departmentname {count} : ')
		managerid = int(input(f'manager-id {count} : '))
		branch_location = input(f'branch_location {count} : ')
		
		data = {'department id':departmentid,\
				'department name':departmentname,\
				'manager-id':managerid,\
				'branch_location':branch_location}

		itemdata.append(data)

	writer=csv.DictWriter(fl,fieldnames=csv_columns)
	writer.writeheader()

	for data in itemdata:
		writer.writerow(data)

	print("The file was succesfully created ! ")

with open('Jayesh-itemdict.csv','r',newline='') as file:
	reader = csv.DictReader(file,fieldnames=csv_columns)

	for row in reader:
		print(row['department name'],row['manager-id'])
