import requests
from flask import Flask, request 

CLIENT_ID = 'fcfd82530779ccf596eb'
CLIENT_SECRET = '53247cc235f74ab4b4841a3c9e7c31cf03d03490'

app = Flask(__name__)

@app.route('/authorize')
def authorize():
    return ''

if __name__ == '__main__':
    app.run(debug=True)