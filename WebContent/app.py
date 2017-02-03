import json
import controller as bot
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
    
@app.route('/servo', methods=['POST'])
def servo():
    #spdL = request.form['spdL']
    spdR = 1 #request.form['spdR']
    #request.get_json(force=True)
    return json.dumps({'status':'OK','spdR':spdR})

if __name__ == '__main__':
    bot.setup()
    app.run(debug=True, host='0.0.0.0')