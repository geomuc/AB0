from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!ikjhlkjhl'

@app.route('/auth/error')
def hello_fehler():
    return 'so ein mist',403

@app.route('/auth/ok')
def hello_ok():
    return 'alles ok',201


if __name__ == '__main__':
    app.run(debug=True)