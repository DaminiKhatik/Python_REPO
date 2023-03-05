import psycopg2
# Establish a connection to the database. # Replace parameter values with database credentials.
conn = psycopg2.connect(database="testpython",                     
                        user="postgres",                       
                        host="localhost",                     
                        password="abc123",                      
                        port="5432")
# Create a cursor. The cursor allows you to execute database 
cur = conn.cursor()
# Create a table. Initialise the table name, the column names and data type. 
cur.execute("""CREATE TABLE FRUITS (id  INT ,
            fruit_name  TEXT,
            color TEXT,
            price REAL)""") 
#Inserting data into the table
cur.execute("""INSERT INTO FRUITS (id, fruit_name, color, price) VALUES (1, 'Apples', 'green', 1.00)""")
cur.execute("""INSERT INTO FRUITS (id, fruit_name, color, price) VALUES (1, 'Bananas', 'yellow', 0.80)""")

conn.commit()
conn.close()
