from flask import render_template
from . import main

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/today')
def today():
	return render_template('today.html')