#Sqlite3 - Not require separate server process
# importing sqlite3 module
import sqlite3

connection = sqlite3.connect('hotel_data.db')

connection.execute(''' CREATE TABLE hotel
		(FIND INT PRIMARY KEY	 NOT NULL,
		FNAME		 TEXT NOT NULL,
		COST		 INT	 NOT NULL,
		WEIGHT	 INT);
		''')

# the above table
connection.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )")
connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )")
connection.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )")


print("All data in food table\n")
cursor = connection.execute("SELECT * from hotel ")

# Getting the values from the database and Error handling

for row in cursor:
	print(row)

