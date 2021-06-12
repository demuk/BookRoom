from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def home():
	title = 'Home'
	return render_template('home.html', title=title)


@app.route('/login', methods=['GET','POST'])
def login():
	title = 'Login'
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for("home"))
	return render_template('login.html', title=title, form=form)


@app.route('/signup')
def signup():
	title = 'SignUp'
	return render_template('signup.html', title=title)