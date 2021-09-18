from flask import Flask

app = Flask(__name__)

@app.route('/upload', method=['POST'])
def upload():
    pass