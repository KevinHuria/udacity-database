# working with psycopg2
import psycopg2
# Establish database connection and create a cursor object that will be used to execute SQL commands
connection = psycopg2.connect(
    host="localhost", database="test", port="5432", user="postgres", password="Empire*2")

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a command: this creates a new table
cursor.execute('DROP TABLE IF EXISTS books;')
cursor.execute('''
    CREATE TABLE books(
      id serial PRIMARY KEY,
      title VARCHAR(120) NOT NULL,
      author varchar(50)NOT NULL,
      category varchar(200) not null,
      review varchar(200) not null,
      date_added date DEFAULT CURRENT_TIMESTAMP
    );
''')

# INSERT DATA INTO BOOKS TABLE
cursor.execute('INSERT INTO books(title, author, category, review)'
      'VALUES(%s, %s, %s, %s)',
      ('Modern Bushido: Living a Life of Excellence',
      'Bohdi Sanders, David Nelson',
      'Sports, Hobbies & Games',
      'Great book!Enjoyed it.')
)

cursor.execute('INSERT INTO books(title, author, category, review)'
               'VALUES(%s, %s, %s, %s)',
               ('Beautiful Disaster: A Novel',
               'Jamie McGuire',
                'Fiction - Womens Fiction',
                'Amazing Book!')
)
#select all from books
cursor.execute('SELECT * FROM books;')
result= cursor.fetchall()
print(result)
# commit all the transactions

connection.commit()
# manually close the connection
connection.close()
cursor.close()
