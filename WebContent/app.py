import json
import controller as bot
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
    
@app.route('/servo', methods=['POST'])
def servo():
    bot.drive(1, 1)
    return json.dumps({'status':'OK'});

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')