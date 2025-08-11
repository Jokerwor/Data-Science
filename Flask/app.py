from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/h')
def hey():
    return '<h2>Hey Learners!</h2>'

@app.route('/test')
def test():
    a = 14 - 7
    return "run this {}".format(a)

@app.errorhandler(404)
def page(e):
    return 'Page not found', 404

if __name__ == '__main__' and os.environ.get('FLASK_ENV') != 'production':
    app.run(host='0.0.0.0', debug=True)