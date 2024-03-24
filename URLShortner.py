from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def create_connection():
    conn = sqlite3.connect('url_shortener.db')
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS urls
                      (id INTEGER PRIMARY KEY, original_url TEXT, short_code TEXT)''')
    conn.commit()
    conn.close()

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))
        conn.commit()
        conn.close()
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT original_url FROM urls WHERE short_code=?", (short_code,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return redirect(result[0])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
