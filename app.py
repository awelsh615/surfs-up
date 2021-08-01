# import dependency
from flask import Flask

# create a Flask instance called "app"
app = Flask(__name__)

# Define the root
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/')
def hello():
    return "Does this work?"



