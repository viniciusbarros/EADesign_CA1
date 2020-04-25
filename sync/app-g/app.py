from flask import Flask
app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/')
def index():
    return 'working fine'

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')