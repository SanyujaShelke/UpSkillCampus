from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

# Function to generate a random string for the short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Create a function to get a new SQLite connection
def get_db_connection():
    conn = sqlite3.connect('urls.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to handle the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['original_url']
    short_url = generate_short_url()

    # Insert the URL into the database using a new connection
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO urls (original_url, short_url) VALUES (?, ?)''',
                   (original_url, short_url))
    conn.commit()
    conn.close()

    return render_template('shortened.html', original_url=original_url, short_url=short_url)

# Route to redirect to the original URL
@app.route('/<short_url>')
def redirect_to_original(short_url):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT original_url FROM urls WHERE short_url = ?''', (short_url,))
    result = cursor.fetchone()
    conn.close()
    if result:
        original_url = result['original_url']
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
