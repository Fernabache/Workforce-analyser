
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    # Handle missing values
    data.fillna(0, inplace=True)
    
    # Normalize data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    return scaled_data
