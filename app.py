from flask import Flask, request, jsonify, render_template
from scraper import scraper
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(11)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    posts = scraper()
    return render_template('posts.html', posts=posts)
