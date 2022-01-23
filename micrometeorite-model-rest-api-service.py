import json
from prediction import prediction
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predictionMerkelVoigt', methods=['POST'])
def predict():
    print(request.json)
    return jsonify({"result": prediction(request.json["file"])}), 200

if __name__ == '__main__':
    app.run(debug=True)