from flask import Flask
import request
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    d=request.get_json()
    a=d['first']
    b=d['second']
    return jsonify({'result': a+b}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    d=request.get_json()
    a=d['first']
    b=d['second']
    return jsonify({'result': a-b}), 200
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
