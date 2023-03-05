import pymssql

# specify the variables required to connect to the datatabase
SERVER = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'data.db'

conn = pymssql.connect(server = SERVER, user = USER, password = PASSWORD, database = DATABASE)

cur = conn.cursor()

cur.execute("CREATE TABLE Student stu_id(stu_id TEXT, stu_name TEXT)")

cur.execute("INSERT INTO Student VALUES('s1', 'Student A' ),"
                                        "('s2', 'Student B'),"
                                        "('s3', 'Student C')")

cur.commit()

cur.execute("SELECT * FROM Student")
conn.close()
