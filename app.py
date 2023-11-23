import sqlite3
from flask import Flask
from flask import request
from model.book import Book
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)

@app.route("/about")
def hello_world():
    person = {
        "name":"aiman",
        "age" : 25
    }
    return person

@app.route("/books",methods=['GET', 'POST'])
def handle_books():
    if request.method == "GET":
        conn = sqlite3.connect("./bookstore.db")
        cursor = conn.cursor()
        result = cursor.execute("select * from books")
        book_list = []
        temp_list = result.fetchall()
        for col in temp_list :
             book= Book()
             book.title = col[0]
             book.publisher = col[1]
             book.publish_date = col[2]
             book.author = col[3]
             book_list.append(book.__dict__)
        conn.close()
        return book_list
    elif request.method == "POST":
        data = request.get_json()
        book = Book()
        book.title = data["title"]
        book.publisher = data["publisher"]
        book.publish_date = data["publish_date"]
        book.author = data["author"]
        return book.__dict__
    
@app.route("/books/<title>")
def find_books(title):
     conn = sqlite3.connect("./bookstore.db")
     cursor = conn.cursor()
     result = cursor.execute(f"select * from books where title = '{title}'")
     book_list = []
     temp_list = result.fetchall()
     for col in temp_list :
            book= Book()
            book.title = col[0]
            book.publisher = col[1]
            book.publish_date = col[2]
            book.author = col[3]
            book_list.append(book.__dict__)
     conn.close()
     return book_list 

