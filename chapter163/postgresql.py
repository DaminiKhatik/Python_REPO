import psycopg2
con = psycopg2.connect("host=localhost dbname=db1 user=root password=root")
cur = con.cursor()
cur.execute("CREATE TABLE Employee emp_id((id TEXT,first_name TEXT, last_name TEXT);")
cur.execute("INSERT INTO my_table(id, first_name, last_name) VALUES (2, 'Jane', 'Doe');")

con.commit()
cur.execute("SELECT * FROM my_table;") 
results = cur.fetchall()
con.close()
print(results)
