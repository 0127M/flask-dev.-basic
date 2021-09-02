from typing import List
from flask import Flask, render_template 


app = Flask(__name__)


@app.route('/')
def index():
    person = "Now you are going to learn how we can add"
    # persons = [20,30,40,50]
    # di = {"name":"nitin"}
    # fruits = ["mango","banana","orange"]
    return render_template('basic2.html',person=person)#if you want to pass any veriable in tamplate and u hv to call in html file 


@app.route('/person/<name>')
def person(name):
    return render_template('person.html', name=name)



if __name__  == "__main__":
    app.run(debug=True)


