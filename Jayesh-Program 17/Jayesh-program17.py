"""
Program 17
Write a Python program to update a specific column value of student 
table and select all rows before and after updating the data.

"""

import mysql.connector
userlogin = mysql.connector.connect(
				host="localhost",
				user="root",
				password="1234")

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

try:
	if userlogin.is_connected():
		cursor=userlogin.cursor()
		initial(cursor)
		name = input('Name of the student : ')
		mark = float(input('Mark of student'))
		cursor.execute("select * from student")
		rec=cursor.fetchall()
		for x in rec:
			print(x) 
			
		cursor.execute(f"update student set total_mark={mark} where name='{name}'")
		userlogin.commit()
		cursor.execute("select * from student")
		rec=cursor.fetchall()
		
		for x in rec:
			print(x) 
		
except Exception as e:
	print("Error while connecting to mysql",e)