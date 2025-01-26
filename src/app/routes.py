
from flask import Flask, request, jsonify
from src.predict import predict_staffing_needs

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    predictions = predict_staffing_needs(data)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
