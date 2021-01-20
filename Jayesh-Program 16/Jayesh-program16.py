"""
Program 16
Write a Python program to create a table student 
(admission number, name, class, total mark and gender) 
and insert some records in that table. 
Finally selects all rows from the table and display the records.
Table student must be stored in school database. 
"""


import mysql.connector

userlogin = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

cur = userlogin.cursor()

def initial(cursor):
	global userlogin

	CREATE_DB = """CREATE DATABASE IF NOT EXISTS school;"""
	USE_DB = """USE school;"""
	TABLE = "CREATE TABLE IF NOT EXISTS student(admission_number INT,\
												name VARCHAR(255),\
												Class INT,\
												total_mark FLOAT,\
												gender CHAR(1));"

	cursor.execute(CREATE_DB)
	cursor.execute(USE_DB)
	cursor.execute(TABLE)
	userlogin.commit()

def addentry(cursor):
	global userlogin
	
	count = 1
	while True:

		admission_number = int(input(f'Admission number of student {count} : '))
		name = input(f'Name of student {count} : ')
		class_no = int(input(f'Class of student {count} : '))
		marks = float(input(f'Mark of student {count} : '))
		gender = input(f'Gender of the student {count} : ')

		QUERY = f"""INSERT INTO student(admission_number,name,class,total_mark,gender)
					VALUES ({admission_number},'{name}',{class_no},{marks},'{gender}');"""
		
		cursor.execute(QUERY)
		userlogin.commit()
		ch = input('Add another student ? : (y/n)').lower()
		if ch == 'n':
			break
		count += 1        
		
		
def display(cursor):
	QUERY = """ SELECT * FROM student;"""
	cursor.execute(QUERY)
	data = cursor.fetchall()
	for entry in data:
		print(entry)


initial(cur)
addentry(cur)
display(cur)