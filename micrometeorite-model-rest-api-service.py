import json
from prediction import prediction
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/micrometeorite-prediction/api/v1/predictionMerkelVoigt', methods=['POST'])
def predict():
    return jsonify({"result": prediction(request.json["file"])}), 200

if __name__ == '__main__':
    app.run(debug=True)