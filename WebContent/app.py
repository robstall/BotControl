#!/usr/bin/env python

import logging
import json
from flask import Flask, render_template, jsonify, request

from controller import SpyBot

LOG_FILENAME = '/tmp/app.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

app = Flask(__name__)
bot = SpyBot()

@app.route('/')
def index():
    return render_template('main.html')
    
@app.route('/servo', methods=['POST'])
def servo():
    lspd = request.json['lspd']
    rspd = request.json['rspd']
    bot.move(lspd, rspd)
    return json.dumps({'status':'OK','lspd':lspd,'rspd':rspd})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')