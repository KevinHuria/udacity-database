import psycopg2
# Establish database connection and create a cursor object that will be used to execute SQL commands
connection =psycopg2.connect(host="localhost", database= "test", port ="5432", user ="postgres", password="Empire*2")

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table3(
      id INTEGER PRIMARY KEY,
      completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table3(id, completed) VALUES(1, TRUE);')
#commit all the transactions
connection.commit()
# manually close the connection
connection.close()
cursor.close()