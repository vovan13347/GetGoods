import requests
import json
from flask import Flask, render_template
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

USERS_URL = config.get('API', 'URL')

response = requests.get(USERS_URL)
if response.status_code == 200:
    goods = response.json()
else:
    print(f"Failed to fetch data: {response.status_code}")


getgoods = Flask(__name__)

@getgoods.route('/')
@getgoods.route('/index')
def index():
    #user = {'username': 'Vova'}
    return render_template('index.html',  goods=goods)


if __name__ == '__main__':
    getgoods.run(host='0.0.0.0', port=5000)
