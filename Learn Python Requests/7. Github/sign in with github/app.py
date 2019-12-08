import requests
from flask import Flask, request 

CLIENT_ID = 'fcfd82530779ccf596eb'
CLIENT_SECRET = '53247cc235f74ab4b4841a3c9e7c31cf03d03490'

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="https://github.com/login/oauth/authorize?client_id={}">Login with Github</a>'.format(CLIENT_ID)

@app.route('/authorize')
def authorize():
    code = request.args.get('code')
    return '<h1>SUCCESS!!! THE CODE IS: {}</h1>'.format(code)

if __name__ == '__main__':
    app.run(debug=True)