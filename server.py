from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/submit', methods=['GET','POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    return f"Received name: {name}, age: {age}"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)