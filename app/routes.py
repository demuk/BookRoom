from flask import render_template
from app import app


@app.route('/')
def home():
	title = 'Home'
	return render_template('home.html', title=title)


@app.route('/login')
def login():
	title = 'Login'
	return render_template('login.html', title=title)


@app.route('/signup')
def signup():
	title = 'SignUp'
	return render_template('signup.html', title=title)