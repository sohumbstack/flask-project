from app import app

@app.route('/')
def index():
    return "It works!\n"

@app.route('/a')
def a():
    return "On endpoint a"

@app.route('/b')
def b():
    return "On endpoint b"