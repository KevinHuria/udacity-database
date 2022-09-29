#working with psycopg2
import psycopg2
# Establish database connection and create a cursor object that will be used to execute SQL commands
connection =psycopg2.connect(host="localhost", database= "test", port ="5432", user ="postgres", password="Empire*2")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table3;')
cursor.execute('''
    CREATE TABLE table3(
      id INTEGER PRIMARY KEY,
      completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table3(id, completed) VALUES(%s,%s);',(1,True))
cursor.execute('INSERT INTO table3(id, completed) VALUES(%s,%s);', (0, False))
cursor.execute('SELECT * FROM table3')
result = cursor.fetchmany(1)
print(result)
result2=cursor.fetchone()
print(result2)
#commit all the transactions
connection.commit()
# manually close the connection
connection.close()
cursor.close()