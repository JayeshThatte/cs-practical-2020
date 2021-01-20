#Jayesh B
"""
Program 20

Write a python program to display the high score
among girls and among boys in class 12.
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


def orderby(cursor):
	global userlogin
	order = input(" topper girls/boys ? m/f : ")

	if order.lower() in ['girls','f']:
		gender = 'f'
		
	else:
		gender = 'm'
		

	QUERY = f""" SELECT * FROM student
				 WHERE gender = '{gender}'
				 ORDER BY total_mark DESC;"""

	
	cursor.execute(QUERY)
	data = cursor.fetchone()
	print(data)

	
initial(cur)
orderby(cur)