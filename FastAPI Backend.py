from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import pandas as pd
from datetime import datetime

from src.models.demand_predictor import DemandPredictor
from src.models.schedule_optimizer import ScheduleOptimizer

app = FastAPI(title="Healthcare Workforce Analytics API")

class PredictionRequest(BaseModel):
    start_date: datetime
    end_date: datetime
    department_id: int

class ScheduleRequest(BaseModel):
    department_id: int
    staff: List[Dict]
    start_date: datetime
    end_date: datetime

@app.post("/api/v1/predict-demand")
async def predict_demand(request: PredictionRequest):
    try:
        predictor = DemandPredictor(config={})
        
        # Load historical data
        historical_data = pd.DataFrame()  # Implementation needed
        
        # Make predictions
        predictions = predictor.predict(historical_data)
        
        return {
            "predictions": predictions.tolist(),
            "metadata": {
                "department_id": request.department_id,
                "start_date": request.start_date,
                "end_date": request.end_date
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/optimize-schedule")
async def optimize_schedule(request: ScheduleRequest):
    try:
        optimizer = ScheduleOptimizer(config={})
        
        # Get demand predictions
        predictor = DemandPredictor(config={})
        demand = pd.DataFrame()  # Implementation needed
        
        # Generate schedule
        schedule = optimizer.create_schedule(
            staff=request.staff,
            demand=demand,
            constraints={}
        )
        
        return {
            "schedule": schedule.to_dict(orient='records'),
            "metadata": {
                "department_id": request.department_id,
                "start_date": request.start_date,
                "end_date": request.end_date
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
