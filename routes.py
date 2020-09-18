from app import app

@app.route('/' methods = ['GET')
def index():
    return "It works!\n"

@server.route('/a', methods = ['GET'])
def a():
    return "On endpoint a"

@server.route('/b', methods = ['GET'])
def b():
    return "On endpoint b"
