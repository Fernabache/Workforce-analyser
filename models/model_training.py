
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data):
    X = data.drop(columns=['staff_needed'])
    y = data['staff_needed']
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, 'models/model.pkl')
