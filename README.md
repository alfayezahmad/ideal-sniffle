# PM2.5 Air Quality Forecasting (Lucknow)
> **Proof-of-Concept:** Predictive Modeling and Diagnostic Analysis of Urban Air Quality.

This repository contains a machine learning pipeline engineered to forecast daily **PM2.5** (particulate matter ≤ 2.5 µm) concentrations in Lucknow, India. The project focuses on feature engineering (Temporal Lags) and model comparison to provide actionable public health recommendations.



---

### Project Architecture
The pipeline follows a structured data science workflow:
1.  **Data Ingestion:** Processing daily pollutant datasets (CPCB standards) with forward/backward fill persistence for gap handling.
2.  **Feature Engineering:**
    - **Lags:** `pm25_lag1` and `pm25_lag7` to capture daily and weekly cycles.
    - **Rolling Window:** 7-day moving averages to smooth volatility.
3.  **Modeling:** Comparative analysis between **Linear Regression** (Baseline) and **Random Forest Regressor** (Non-linear ensemble).

---

### Mathematical Evaluation
We utilize four formal definitions to evaluate model fidelity and feature construction:

1. **Mean Absolute Error (MAE):** Represents the average magnitude of errors without considering their direction.
   $$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

2. **Root Mean Square Error (RMSE):** Penalizes larger forecasting errors, critical for detecting dangerous pollution spikes.
   $$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

3. **Coefficient of Determination ($R^2$):** Measures the proportion of variance in PM2.5 levels explained by features.
   $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

4. **Rolling Feature Calculation:** Capturing the short-term trend ($t$) over a window ($k=7$ days).
   $$\mu_t = \frac{1}{k} \sum_{i=0}^{k-1} x_{t-i}$$

---

### Key Insights
- **Performance:** **Random Forest** outperformed Linear Regression by effectively capturing the sharp non-linear peaks in PM2.5 levels.
- **Feature Importance:** Time-based features (Rolling Means) and CO/SO2 concentrations were identified as the highest predictors of localized spikes.

---

### Recommendations Framework
The system classifies forecasts into EPA-aligned categories to generate automated health advisories:

| Category | PM2.5 Range (µg/m³) | Recommendation |
| :--- | :--- | :--- |
| **Good** | 0 – 12.0 | Air quality is satisfactory. Enjoy outdoor activities freely. |
| **Moderate** | 12.1 – 35.4 | Acceptable air quality. Sensitive individuals should limit prolonged exertion. |
| **Unhealthy for Sensitive Groups** | 35.5 – 55.4 | Sensitive groups should reduce outdoor activity. Consider wearing a mask. |
| **Unhealthy** | 55.5 – 150.4 | Everyone may experience health effects. Limit outdoor activities. Use purifiers. |
| **Very Unhealthy** | 150.5 – 250.4 | Health alert: serious effects possible. Avoid outdoor activity. Keep windows closed. |
| **Hazardous** | > 250.4 | Emergency conditions. Stay indoors with filtered air. Follow local advisories. |

---

### Installation
```bash
git clone https://github.com/alfayezahmad/ideal-sniffle.git
cd Lucknow-PM2.5-Forecast
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

### License

Distributed under the MIT License. Author: Alfayez Ahmad | Copyright: © 2025
