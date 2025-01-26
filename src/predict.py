
import joblib
import pandas as pd

def predict_staffing_needs(input_data):
    model = joblib.load('models/model.pkl')
    predictions = model.predict(input_data)
    return predictions
