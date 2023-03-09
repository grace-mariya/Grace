from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['library']
books_collection = db['books']
users_collection = db['users']

# Routes
@app.route('/')
def library():    
    return render_template('library.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = users_collection.find_one({'email': email, 'password': password})
        if user:
            return redirect('/index')
        else:
            return redirect('/signup')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users_collection.insert_one({'email': email, 'password': password})
        return redirect('/index')
    return render_template('signup.html')

@app.route('/index')
def index():
    books = books_collection.find()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        book_year = request.form['year']
        publisher = request.form['publisher']
        book = {
            'title': title,
            'author': author,
            'year': book_year,
            'publisher': publisher
        }
        books_collection.insert_one(book)
        return redirect('/index')
    return render_template('add_book.html')

@app.route('/edit_book/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = books_collection.find_one({'_id': ObjectId(book_id)})
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        book_year = request.form['year']
        publisher = request.form['publisher']
        books_collection.update_one(
            {'_id': ObjectId(book_id)},
            {'$set': {'title': title, 'author': author, 'year': book_year, 'publisher': publisher}}
        )
        return redirect('/index')
    return render_template('edit_book.html', book=book)

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    books_collection.delete_one({'_id': ObjectId(book_id)})
    return redirect('/index')

if __name__ == '__main__':
    app.run(debug=True)
