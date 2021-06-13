from app.models import User
from flask import render_template, redirect, flash, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/home')
@login_required
def home():
	title = 'Home'
	return render_template('home.html', title=title)


@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	title = 'Login'
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for("home"))
		login_user(user, remember = form.remember_me.data)#
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('home')
		return redirect(next_page)
	return render_template('login.html', title=title, form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	title = 'SignUp'
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, Welcome to the club!')
		return redirect(url_for('login'))
	return render_template('signup.html', title=title,form=form)