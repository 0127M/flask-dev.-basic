from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello</h1>"

@app.route('/home', methods=['POST','GET'])
def home():
    return "welcome to home page"

@app.route('/json')
def json():
    return jsonify({"key":"value","key":[10,20,30,40]})


@app.route('/person/<name>', methods=['GET','POST'])
def person(name):
    return "<h1> hi,{}.welcome to person page</h1>".format(name)


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi, {}. you are from {}. you are on the query page</h>'.format(name, location)  


if __name__  == "__main__":
    app.run(debug=True)


@app.route('/theform')
def theform():
    return '''<from mathod = "POST" action="/proce'''