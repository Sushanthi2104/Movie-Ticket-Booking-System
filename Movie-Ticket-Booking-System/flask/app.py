# app.py (Flask-based updated model)

from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'movie_secret'

def get_movies():
    con = sqlite3.connect('database/movie.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()
    con.close()
    return movies

@app.route('/')
def index():
    movies = get_movies()
    return render_template('index.html', movies=movies)

@app.route('/book/<int:movie_id>', methods=['GET', 'POST'])
def book(movie_id):
    if request.method == 'POST':
        user = request.form['name']
        # Store booking info
        return f"Ticket booked for {user}!"
    return render_template('booking.html', movie_id=movie_id)

if __name__ == '__main__':
    app.run(debug=True)
