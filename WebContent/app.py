import json
import controller as bot
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
    
@app.route('/servo', methods=['POST'])
def servo():
    #print "content_type: ", request.content_type
    #print "request.json: ", request.json
    desc = request.json['desc']
    return json.dumps({'status':'OK', 'desc':desc})

if __name__ == '__main__':
    bot.setup()
    app.run(debug=True, host='0.0.0.0')