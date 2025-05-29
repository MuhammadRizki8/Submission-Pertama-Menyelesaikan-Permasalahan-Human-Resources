
# HR Employee Attrition Prediction Results

This directory contains the complete results of the HR employee attrition prediction analysis.

## Directory Structure:
- `models/`: Trained machine learning models and preprocessors
- `data/`: Processed datasets (if saved)
- `reports/`: Analysis reports and predictions

## Key Files:
- `final_model_logistic_regression.pkl`: Best performing model
- `model_comparison.csv`: Performance comparison of all models
- `final_predictions.csv`: Test set predictions
- `evaluation_report.txt`: Detailed analysis report
- `feature_importance.csv`: Feature importance rankings (if available)

## Best Model: Logistic Regression
- F1-Score: 0.5714
- Accuracy: 0.8726
- ROC-AUC: 0.8205

## Usage:
To load and use the final model:
```python
import joblib
model = joblib.load('models/final_model_logistic_regression.pkl')
predictions = model.predict(X_new)
Generated: 2025-05-29 11:00:42
