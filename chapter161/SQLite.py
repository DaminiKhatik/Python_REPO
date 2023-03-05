import sqlite3
connection_obj = sqlite3.connect('student_data.db')
cursor_obj = connection_obj.cursor()
table = """ CREATE TABLE student_data (
            Email VARCHAR(255) NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Score INT
        ); """
cursor_obj.execute(table)
 
print("Table is Ready")
connection_obj.close()