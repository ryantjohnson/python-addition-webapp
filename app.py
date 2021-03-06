#!/usr/bin/env python

from flask import Flask, render_template
from flask import request


app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name="Ryan"):
	context = {"name":name}
	return render_template("index.html",**context)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
	context = {'num1':num1, 'num2':num2}
	return render_template("add.html", **context)

@app.route("/multiply/<int:num1>/<int:num2>")
@app.route("/multiply/<float:num1>/<int:num2>")
@app.route("/multiply/<int:num1>/<float:num2>")
@app.route("/multiply/<float:num1>/<float:num2>")
def multiply(num1, num2):
	context = {'num1':num1, 'num2':num2}
	return render_template("multiply.html", **context)

@app.route('/subtract/<int:num1>/<int:num2>')
@app.route('/subtract/<float:num1>/<int:num2>')
@app.route('/subtract/<int:num1>/<float:num2>')
@app.route('/subtract/<float:num1>/<float:num2>')
def subtract(num1, num2):
	context = {'num1':num1, 'num2':num2}
	return render_template("subtract.html", **context)

if __name__ == "__main__":
	app.run(debug=True, port=5000)