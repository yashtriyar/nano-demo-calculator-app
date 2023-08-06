from flask import Flask,jsonify,request
from dataclasses import dataclass
app = Flask(__name__)
@dataclass
class Result:
    result: int

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    d=request.json
    res=Result(d['first']+d['second'])
    return jsonify(res)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    d=request.json
    res=Result(d['first']-d['second'])
    return jsonify(res)
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0',debug=True)
