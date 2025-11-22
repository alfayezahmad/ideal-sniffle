# 🌍 PM2.5 Forecasting in Lucknow

This repository contains a proof‑of‑concept notebook for forecasting **PM2.5 air pollution levels in Lucknow, India** using machine learning models.  
The project demonstrates how to preprocess air quality data, engineer lag features, train regression models, evaluate performance, and generate actionable next‑day forecasts with health recommendations.

---

## 📑 Project Overview

Air pollution is a critical public health issue in many cities. PM2.5 (particulate matter ≤ 2.5 µm) is especially harmful due to its ability to penetrate deep into the lungs.  
This notebook builds a simple forecasting pipeline to:

- Load and clean daily PM2.5 data.
- Create lag and rolling features to capture temporal patterns.
- Train **Linear Regression** and **Random Forest** models.
- Evaluate models with multiple metrics and visualizations.
- Forecast the **next day’s PM2.5 concentration**.
- Classify air quality into categories and provide **health recommendations**.

---

## ⚙️ Workflow

1. **Data Preparation**
   - Load CSV file (`ML Lucknow.csv`) containing daily pollutant data.
   - Handle missing values with forward/backward fill.
   - Generate lag features (`lag1`, `lag7`, rolling mean).

2. **Model Training**
   - Linear Regression (scaled features).
   - Random Forest Regressor (tree‑based, no scaling required).

3. **Evaluation**
   - Metrics: MAE, RMSE, R², MAPE.
   - Visualizations:
     - Actual vs Predicted plots
     - Scatter plots
     - Residual histograms
     - Residuals over time
     - QQ plots
     - Feature importance (Random Forest)

4. **Forecasting**
   - Train a lag‑only Random Forest for next‑day prediction.
   - Classify forecast into AQI‑style categories:
     - Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, Hazardous
   - Provide tailored recommendations for each category.

---

## 📊 Example Output
```Forecast date: 2025-11-22
Predicted PM2.5: 180.0 µg/m³
Pollution category: Unhealthy
Recommendations:

-  Everyone may begin to experience health effects.
-  Limit outdoor activities.
-  Use air purifiers indoors.
```

---

## 🧾 Recommendation Table

| Pollution Category                | PM2.5 Range (µg/m³) | Recommendations                                                                 |
|-----------------------------------|---------------------|---------------------------------------------------------------------------------|
| Good                              | 0 – 12              | Air quality is satisfactory. Enjoy outdoor activities freely.                   |
| Moderate                          | 12.1 – 35.4         | Acceptable air quality. Sensitive individuals should limit prolonged exertion.  |
| Unhealthy for Sensitive Groups    | 35.5 – 55.4         | Sensitive groups should reduce outdoor activity. Consider wearing a mask.       |
| Unhealthy                         | 55.5 – 150.4        | Everyone may experience health effects. Limit outdoor activities. Use purifiers.|
| Very Unhealthy                    | 150.5 – 250.4       | Health alert: serious effects possible. Avoid outdoor activity. Keep windows closed. |
| Hazardous                         | > 250.4             | Emergency conditions. Stay indoors with filtered air. Follow local advisories.  |
---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## 🙌 Acknowledgements

-  Data source: Local air quality monitoring datasets (Lucknow) by CPCB.
-  Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit‑Learn.
-  AetherAI Team: [Alfayez Ahmad](https://github.com/alfayezahmad)
