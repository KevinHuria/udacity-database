from unicodedata import category
from flask import Flask, render_template, request, url_for, redirect
import psycopg2

app = Flask(__name__)


def get_db_connection():
    connection = psycopg2.connect(
        host="localhost", database="test", port="5432", user="postgres", password="Empire*2")
    return connection


@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books;')
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', books=books)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, category, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, category, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')
