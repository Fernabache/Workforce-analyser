import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from typing import Tuple, Dict

class DemandPredictor:
    def __init__(self, config: Dict):
        self.model = RandomForestRegressor(
            n_estimators=config.get('n_estimators', 100),
            random_state=42
        )
        self.scaler = StandardScaler()
        
    def prepare_features(self, data: pd.DataFrame) -> np.ndarray:
        features = data[['admission_count', 'day_of_week', 'is_holiday', 
                        'season', 'department_id']]
        return self.scaler.fit_transform(features)
        
    def train(self, data: pd.DataFrame) -> None:
        X = self.prepare_features(data)
        y = data['required_staff']
        self.model.fit(X, y)
        
    def predict(self, data: pd.DataFrame) -> np.ndarray:
        X = self.prepare_features(data)
        return self.model.predict(X)
        
    def evaluate(self, data: pd.DataFrame) -> Dict[str, float]:
        predictions = self.predict(data)
        actuals = data['required_staff']
        
        mse = np.mean((predictions - actuals) ** 2)
        mae = np.mean(np.abs(predictions - actuals))
        
        return {
            'mse': mse,
            'mae': mae,
            'rmse': np.sqrt(mse)
        }
