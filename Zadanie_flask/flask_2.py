from flask import Flask
from flask import request, redirect
from flask import render_template


app = Flask(__name__)


@app.route('/me')
def me():
	return render_template('index.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
       return render_template("contact.html")
    elif request.method == 'POST':
        print(request.form)
        return redirect("/")
