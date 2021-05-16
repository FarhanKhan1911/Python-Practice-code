'''
Experiment No.8: Write a Program to illustrate Python-MySQL database connectivity.

@author: KHAN FARHAN NADEEM (19CO27)
'''

import MySQLdb 

#Theory about MySQL and MySQL-Connector-Python
'''
*Install MySQL Driver
Python needs a MySQL driver to access the MySQL database.

*Test MySQL Connector
To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content:

demo_mysql_test.py:
import mysql.connector

*Create Connection
Start by creating a connection to the database.
Use the username and password from your MySQL database
If the above code was executed with no errors, "MySQL Connector" is installed and ready to be used.

*Insert Into Table
To fill a table in MySQL, use the "INSERT INTO" statement.

*Update Table
You can update existing records in a table by using the "UPDATE" statement

*Delete Record
You can delete records from an existing table by using the "DELETE FROM" statement

'''
from prettytable import PrettyTable as pt

class StudentDb:
    def __init__(self):
        self.createDb()

    def createDb(self):
        self.db1 = MySQLdb.connect(host='localhost',user='root',password='toor')
        self.cur = self.db1.cursor()
        self.cur.execute('''CREATE SCHEMA IF NOT EXISTS `sblc_exp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  ''')
        self.db = MySQLdb.connect(host='localhost',user='root',password='toor',db='sblc_exp')
        self.cur = self.db.cursor()

        self.createTable()
    def createTable(self):
        query = '''
            CREATE TABLE IF NOT EXISTS student (
                idstudent INT NOT NULL AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(100) NOT NULL,last_name VARCHAR(100) NOT NULL,father_name VARCHAR(100) NOT NULL,mother_name VARCHAR(100) NOT NULL,roll_number VARCHAR(50) UNIQUE NOT NULL,mobile_number VARCHAR(15) UNIQUE NOT NULL,address TEXT NOT NULL,dept VARCHAR(40) NOT NULL,year VARCHAR(10) NOT NULL
                )
        '''
        self.cur.execute(query)
        self.db.commit()


    def insertData(self,datalist):
        query = '''
            INSERT INTO student (first_name,last_name,father_name,mother_name,roll_number,mobile_number,address,dept,year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''

        self.cur.execute(query,(datalist[0],datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],datalist[6],datalist[7],datalist[8]))
        self.db.commit()

        print('data entered')

    def update(self,rollnumber,datalist):
        query = '''UPDATE student set first_name = %s,last_name = %s,father_name = %s,mother_name = %s,roll_number = %s,mobile_number = %s,address = %s,dept = %s, year = %s where roll_number = %s'''

        self.cur.execute(query,(datalist[0],datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],datalist[6],datalist[7],datalist[8],rollnumber))
        self.db.commit()

    def delete(self,rollnumber):
        query = '''
            DELETE from student where roll_number = %s
        '''
        self.cur.execute(query,(rollnumber,))
        self.db.commit()

    def check_roll_number_exists(self,rollnumber):
        self.cur.execute(''' SELECT * from student WHERE roll_number=%s''',(rollnumber,))
        data = self.cur.fetchone()
        if data == None :
            return True
        return False

    def display(self):
        self.cur.execute('''SELECT * FROM student''')
        data = self.cur.fetchall()
        table = pt(['id','First Name','Last Name','Father Name','Mother Name','Roll Number','Mobile Number','Address','Department','Year'])
        for i in data:
            table.add_row(i)
        print(table)



stddb = StudentDb()

def insert_data():
    datalist = []
    print("Enter Student data : ")
    datalist.append(input("Enter Student First Name : "))
    datalist.append(input("Enter Student Last Name : "))
    datalist.append(input("Enter Student Father Name : "))
    datalist.append(input("Enter Student Mother Name : "))
    datalist.append(input("Enter Student Roll Number : "))
    datalist.append(int(input("Enter Student Mobile Number : ")))
    datalist.append(input("Enter Student Address : "))
    datalist.append(input("Enter Student Department : "))
    datalist.append(input("Enter Student Year : "))

    if stddb.check_roll_number_exists(datalist[4]):
        stddb.insertData(datalist)
    else:
        print(f"Student with roll number {datalist[4]} exists")

def update():
    rollnumber = input("Enter the roll number of student to update")

    if stddb.check_roll_number_exists(rollnumber):
        print("Data doesn't exists")
    else:
        datalist = []
        print("Enter Student Updated data : ")
        datalist.append(input("Enter Student Updated First Name : "))
        datalist.append(input("Enter Student Updated Last Name : "))
        datalist.append(input("Enter Student Updated Father Name : "))
        datalist.append(input("Enter Student Updated Mother Name : "))
        datalist.append(input("Enter Student Updated Roll Number : "))
        datalist.append(input("Enter Student Updated Mobile Number : "))
        datalist.append(input("Enter Student Updated Address : "))
        datalist.append(input("Enter Student Updated Department : "))
        datalist.append(input("Enter Student Updated Year : "))

        stddb.update(rollnumber,datalist)

def delete():
    rollnumber = input("Enter the roll number of student to update")

    if stddb.check_roll_number_exists(rollnumber):
        print("Data doesn't exists")
    else:
        stddb.delete(rollnumber)


def main():
    print("Program to demonstrate CRUD")
    while True:
        print("1. Insert student data")
        print("2. Update student data")
        print("3. Delete student data")
        print("4. Display student data")
        print("5. Exit")

        cmd = int(input("Enter the command number"))

        if cmd == 1:
            insert_data()
        elif cmd == 2:
            update()
        elif cmd == 3:
            delete()
        elif cmd == 4:
            stddb.display()
        elif cmd == 5:
            exit()
main()

'''
Conclusion
MySQL Connector/Python enables Python programs to access MySQL databases, using an API that is compliant with the Python Database API Specification 
The MySQL connector is a library for, well, connecting JDBC to the MySQL database.
This is necessary because each make of database server has its own specific protocol for transporting requests to, and results from, the server to application programs

'''