"""
Program 18
Write a Python program to display data in 
ascending / descending order using order by clause. 
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
	order = input("ascending / descending ? a/d")
	sort = ''
	

	if order.lower() in ['ascending','a']:
		sort = "ASC"
	else:
		sort = "DESC"

	QUERY = f""" SELECT * FROM student
				 ORDER BY total_mark {sort};"""

	print(QUERY)
	cursor.execute(QUERY)
	data = cursor.fetchall()

	for entry in data:
		print(entry)

	
initial(cur)
orderby(cur)