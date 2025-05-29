import gradio as gr
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Load your trained model and preprocessors
# Update these paths to match your saved model files
MODEL_DIR = "hr_attrition_results_20250529_110042"  # Update with your actual directory

def load_model_components():
    """Load the trained model and preprocessors"""
    try:
        # Load the final model (update filename based on your best model)
        model = joblib.load(f"{MODEL_DIR}/models/final_model_logistic_regression.pkl")
        
        # Load preprocessors - try both encoding types
        try:
            scaler = joblib.load(f"{MODEL_DIR}/models/scaler_label.pkl")
            label_encoders = joblib.load(f"{MODEL_DIR}/models/label_encoders.pkl")
            encoding_type = "label"
        except:
            scaler = joblib.load(f"{MODEL_DIR}/models/scaler_onehot.pkl")
            label_encoders = None
            encoding_type = "onehot"
            
        return model, scaler, label_encoders, encoding_type
    except Exception as e:
        print(f"Error loading model components: {e}")
        return None, None, None, None

# Load model components
model, scaler, label_encoders, encoding_type = load_model_components()

# Define categorical columns (from your original data)
categorical_cols = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 
                   'JobRole', 'MaritalStatus', 'Over18', 'OverTime']

# Define uninformative columns to drop
uninformative_cols = ['EmployeeCount', 'EmployeeId', 'Over18', 'StandardHours']

def preprocess_employee_data(data_dict, encoding_type, scaler, label_encoders):
    """Preprocess employee data for prediction"""
    
    # Convert to DataFrame
    df = pd.DataFrame([data_dict])
    
    # Drop uninformative columns
    df = df.drop(columns=[col for col in uninformative_cols if col in df.columns], errors='ignore')
    
    # Handle categorical encoding
    if encoding_type == "label" and label_encoders:
        for col in categorical_cols:
            if col in df.columns and col in label_encoders:
                # Handle unseen categories by using the most frequent category
                try:
                    df[col] = label_encoders[col].transform(df[col])
                except ValueError:
                    # If unseen category, use mode (most frequent) from training
                    mode_encoded = 0  # Default fallback
                    df[col] = mode_encoded
        
        # Ensure all columns are numeric
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df.fillna(0, inplace=True)
        
    elif encoding_type == "onehot":
        # One-hot encode categorical columns
        df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
        
        # Get expected columns from scaler (this is a simplified approach)
        # In production, you should save the column names from training
        expected_cols = list(range(scaler.scale_.shape[0]))  # Rough estimate
        
        # Ensure we have the right number of columns
        while len(df_encoded.columns) < len(expected_cols):
            df_encoded[f'dummy_col_{len(df_encoded.columns)}'] = 0
            
        df = df_encoded.iloc[:, :len(expected_cols)]
    
    # Scale the features
    X_scaled = scaler.transform(df)
    
    return X_scaled

def predict_attrition(age, business_travel, daily_rate, department, distance_from_job,
                     education, education_field, environment_satisfaction, gender,
                     hourly_rate, job_involvement, job_level, job_role, job_satisfaction,
                     marital_status, monthly_income, monthly_rate, num_companies_worked,
                     overtime, percent_salary_hike, performance_rating, relationship_satisfaction,
                     stock_option_level, total_working_years, training_times_last_year,
                     work_life_balance, years_at_company, years_in_current_role,
                     years_since_last_promotion, years_with_curr_manager):
    
    if model is None:
        return "❌ Model not loaded. Please check model files.", 0.0, ""
    
    # Create employee data dictionary
    employee_data = {
        'Age': age,
        'BusinessTravel': business_travel,
        'DailyRate': daily_rate,
        'Department': department,
        'DistanceFromJob': distance_from_job,
        'Education': education,
        'EducationField': education_field,
        'EnvironmentSatisfaction': environment_satisfaction,
        'Gender': gender,
        'HourlyRate': hourly_rate,
        'JobInvolvement': job_involvement,
        'JobLevel': job_level,
        'JobRole': job_role,
        'JobSatisfaction': job_satisfaction,
        'MaritalStatus': marital_status,
        'MonthlyIncome': monthly_income,
        'MonthlyRate': monthly_rate,
        'NumCompaniesWorked': num_companies_worked,
        'OverTime': overtime,
        'PercentSalaryHike': percent_salary_hike,
        'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction,
        'StockOptionLevel': stock_option_level,
        'TotalWorkingYears': total_working_years,
        'TrainingTimesLastYear': training_times_last_year,
        'WorkLifeBalance': work_life_balance,
        'YearsAtCompany': years_at_company,
        'YearsInCurrentRole': years_in_current_role,
        'YearsSinceLastPromotion': years_since_last_promotion,
        'YearsWithCurrManager': years_with_curr_manager
    }
    
    try:
        # Preprocess the data
        X_processed = preprocess_employee_data(employee_data, encoding_type, scaler, label_encoders)
        
        # Make prediction
        prediction = model.predict(X_processed)[0]
        probability = model.predict_proba(X_processed)[0][1] if hasattr(model, 'predict_proba') else 0.5
        
        # Create result message
        if prediction == 1:
            result = "🚨 **HIGH RISK** - Employee likely to leave"
            color = "red"
        else:
            result = "✅ **LOW RISK** - Employee likely to stay"
            color = "green"
        
        # Risk level based on probability
        if probability >= 0.7:
            risk_level = "Very High Risk"
        elif probability >= 0.5:
            risk_level = "High Risk"
        elif probability >= 0.3:
            risk_level = "Moderate Risk"
        else:
            risk_level = "Low Risk"
        
        # Recommendations
        recommendations = ""
        if probability >= 0.5:
            recommendations = """
            **📋 Recommended Actions:**
            • Schedule immediate retention discussion
            • Review compensation and benefits
            • Assess job satisfaction and workload
            • Consider career development opportunities
            • Improve work-life balance initiatives
            """
        else:
            recommendations = """
            **📋 Recommended Actions:**
            • Continue regular check-ins
            • Maintain current engagement strategies
            • Monitor for any changes in satisfaction
            """
        
        return result, probability, f"**Risk Level:** {risk_level}\n{recommendations}"
        
    except Exception as e:
        return f"❌ Error making prediction: {str(e)}", 0.0, ""

# Create Gradio interface
def create_interface():
    with gr.Blocks(title="HR Attrition Prediction System", theme=gr.themes.Soft()) as demo:
        
        gr.Markdown("""
        # 🎯 HR Employee Attrition Prediction System
        
        This tool predicts the likelihood of employee attrition based on various factors.
        Fill in the employee information below to get a prediction and risk assessment.
        """)
        
        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown("### 📊 Employee Information")
                
                # Personal Information
                with gr.Group():
                    gr.Markdown("**Personal Details**")
                    with gr.Row():
                        age = gr.Slider(18, 65, value=30, label="Age")
                        gender = gr.Dropdown(["Male", "Female"], label="Gender", value="Male")
                    
                    with gr.Row():
                        marital_status = gr.Dropdown(["Single", "Married", "Divorced"], 
                                                   label="Marital Status", value="Single")
                        distance_from_job = gr.Slider(1, 30, value=5, label="Distance from Job (km)")
                
                # Job Information
                with gr.Group():
                    gr.Markdown("**Job Details**")
                    department = gr.Dropdown(["Sales", "Research & Development", "Human Resources"],
                                           label="Department", value="Sales")
                    job_role = gr.Dropdown([
                        "Sales Executive", "Research Scientist", "Laboratory Technician",
                        "Manufacturing Director", "Healthcare Representative", "Manager",
                        "Sales Representative", "Research Director", "Human Resources"
                    ], label="Job Role", value="Sales Executive")
                    
                    with gr.Row():
                        job_level = gr.Slider(1, 5, value=2, label="Job Level")
                        education = gr.Slider(1, 5, value=3, label="Education Level")
                    
                    education_field = gr.Dropdown([
                        "Life Sciences", "Medical", "Marketing", "Technical Degree",
                        "Human Resources", "Other"
                    ], label="Education Field", value="Life Sciences")
                
                # Work Experience
                with gr.Group():
                    gr.Markdown("**Experience**")
                    with gr.Row():
                        total_working_years = gr.Slider(0, 40, value=5, label="Total Working Years")
                        years_at_company = gr.Slider(0, 40, value=3, label="Years at Company")
                    
                    with gr.Row():
                        years_in_current_role = gr.Slider(0, 20, value=2, label="Years in Current Role")
                        years_since_last_promotion = gr.Slider(0, 20, value=1, label="Years Since Last Promotion")
                    
                    with gr.Row():
                        years_with_curr_manager = gr.Slider(0, 20, value=2, label="Years with Current Manager")
                        num_companies_worked = gr.Slider(0, 10, value=2, label="Number of Companies Worked")
                
                # Compensation
                with gr.Group():
                    gr.Markdown("**Compensation**")
                    with gr.Row():
                        monthly_income = gr.Slider(1000, 20000, value=5000, label="Monthly Income ($)")
                        hourly_rate = gr.Slider(30, 100, value=65, label="Hourly Rate ($)")
                    
                    with gr.Row():
                        daily_rate = gr.Slider(100, 1500, value=800, label="Daily Rate ($)")
                        monthly_rate = gr.Slider(2000, 27000, value=15000, label="Monthly Rate ($)")
                    
                    with gr.Row():
                        percent_salary_hike = gr.Slider(10, 25, value=15, label="Percent Salary Hike (%)")
                        stock_option_level = gr.Slider(0, 3, value=1, label="Stock Option Level")
                
                # Work Conditions
                with gr.Group():
                    gr.Markdown("**Work Conditions**")
                    business_travel = gr.Dropdown(["Non-Travel", "Travel_Rarely", "Travel_Frequently"],
                                                label="Business Travel", value="Travel_Rarely")
                    overtime = gr.Dropdown(["Yes", "No"], label="Overtime", value="No")
                    
                    with gr.Row():
                        work_life_balance = gr.Slider(1, 4, value=3, label="Work Life Balance (1-4)")
                        training_times_last_year = gr.Slider(0, 6, value=2, label="Training Times Last Year")
                
                # Satisfaction Ratings
                with gr.Group():
                    gr.Markdown("**Satisfaction Ratings (1-4 scale)**")
                    with gr.Row():
                        job_satisfaction = gr.Slider(1, 4, value=3, label="Job Satisfaction")
                        environment_satisfaction = gr.Slider(1, 4, value=3, label="Environment Satisfaction")
                    
                    with gr.Row():
                        relationship_satisfaction = gr.Slider(1, 4, value=3, label="Relationship Satisfaction")
                        job_involvement = gr.Slider(1, 4, value=3, label="Job Involvement")
                    
                    performance_rating = gr.Slider(3, 4, value=3, label="Performance Rating")
                
                predict_btn = gr.Button("🔮 Predict Attrition Risk", variant="primary", size="lg")
            
            with gr.Column(scale=1):
                gr.Markdown("### 📈 Prediction Results")
                
                prediction_output = gr.Markdown(value="Click **Predict** to see results")
                probability_output = gr.Number(label="Attrition Probability", precision=3)
                recommendations_output = gr.Markdown(value="")
        
        # Connect the prediction function
        predict_btn.click(
            fn=predict_attrition,
            inputs=[
                age, business_travel, daily_rate, department, distance_from_job,
                education, education_field, environment_satisfaction, gender,
                hourly_rate, job_involvement, job_level, job_role, job_satisfaction,
                marital_status, monthly_income, monthly_rate, num_companies_worked,
                overtime, percent_salary_hike, performance_rating, relationship_satisfaction,
                stock_option_level, total_working_years, training_times_last_year,
                work_life_balance, years_at_company, years_in_current_role,
                years_since_last_promotion, years_with_curr_manager
            ],
            outputs=[prediction_output, probability_output, recommendations_output]
        )
        
        gr.Markdown("""
        ---
        **Note:** This prediction system is based on historical data and should be used as a decision-support tool. 
        Always combine predictions with human judgment and consider individual circumstances.
        """)
    
    return demo

# Launch the application
if __name__ == "__main__":
    # Check if model is loaded
    if model is None:
        print("⚠️  WARNING: Model not loaded. Please update MODEL_DIR path in the script.")
        print("The interface will still launch but predictions may not work.")
    
    demo = create_interface()
    
    # Launch with sharing enabled for external access
    demo.launch(
        server_name="0.0.0.0",  # Allow external access
        server_port=7860,       # Default Gradio port
        share=True,             # Create public link
        show_error=True         # Show detailed errors
    )