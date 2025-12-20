"""
Project: Lucknow PM2.5 Forecasting (Proof-of-Concept)
Author: Alfayez Ahmad
Copyright: (c) 2025
License: MIT
"""

import os
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --- CONFIGURATION & LOGGING ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AirQualityForecaster:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.model_rf = None
        self.scaler = StandardScaler()

    def load_and_clean(self) -> pd.DataFrame:
        """Loads data and handles missing values via persistence filling."""
        logger.info(f"Loading data from {self.file_path}")
        df = pd.read_csv(self.file_path, parse_dates=["date"])
        df = df.sort_values("date").reset_index(drop=True)
        
        # Fill gaps and engineer features
        df = df.ffill().bfill()
        df["pm25_lag1"] = df["pm25"].shift(1)
        df["pm25_lag7"] = df["pm25"].shift(7)
        df["pm25_rolling7"] = df["pm25"].rolling(window=7, min_periods=1).mean()
        
        self.df = df.dropna().copy()
        return self.df

    def evaluate_metrics(self, y_true: np.ndarray, y_pred: np.ndarray, model_name: str) -> Dict:
        """Calculates formal regression metrics."""
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        r2 = r2_score(y_true, y_pred)
        
        logger.info(f"[{model_name}] R²: {r2:.3f} | MAE: {mae:.2f}")
        return {"MAE": mae, "RMSE": rmse, "R2": r2}

    def get_health_advice(self, pm25: float) -> Tuple[str, List[str]]:
        """Categorizes pollution levels and provides clinical recommendations."""
        if pm25 <= 12.0:
            return "Good", ["Satisfactory air quality.", "Enjoy outdoors."]
        elif pm25 <= 35.4:
            return "Moderate", ["Limit prolonged outdoor exertion."]
        elif pm25 <= 150.4:
            return "Unhealthy", ["Limit outdoor activities.", "Use air purifiers."]
        elif pm25 <= 250.4:
            return "Very Unhealthy", ["Avoid outdoor activity.", "Keep windows closed."]
        return "Hazardous", ["Emergency conditions.", "Stay indoors with filtered air."]

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    path = os.path.join(desktop, "ML Lucknow.csv")
    
    forecaster = AirQualityForecaster(path)
    data = forecaster.load_and_clean()

    # Features and Target
    feature_cols = [c for c in data.columns if c not in ["date", "pm25"]]
    X, y = data[feature_cols], data["pm25"]

    # Split (80/20 Time-based)
    split = int(len(data) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # Train Random Forest
    rf = RandomForestRegressor(n_estimators=300, random_state=42)
    rf.fit(X_train, y_train)
    preds = rf.predict(X_test)

    # Output Results
    metrics = forecaster.evaluate_metrics(y_test, preds, "Random Forest")
    next_day_val = preds[-1]
    category, recs = forecaster.get_health_advice(next_day_val)

    print(f"\n🚀 Next-Day Forecast: {next_day_val:.2f} µg/m³")
    print(f"Status: {category}")
    for r in recs: print(f" - {r}")
