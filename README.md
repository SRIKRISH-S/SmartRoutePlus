🚚 SmartRoutePlus
AI-Based Delivery Delay & Cost Optimization System

SmartRoutePlus is a data-driven logistics optimization system developed for the FedEx SMART Hackathon at Shaastra 2026.
It leverages machine learning to predict delivery delays and estimate delivery costs, enabling smarter routing decisions and improved operational efficiency in logistics.

📌 Problem Statement

Logistics companies such as FedEx face persistent challenges including:

Unpredictable delivery delays

Increased fuel and operational costs

Traffic congestion and weather disruptions

Inefficient route prioritization

Existing systems are mostly reactive, addressing problems only after delays occur.

💡 Proposed Solution

SmartRoutePlus introduces a predictive and data-driven approach by:

Predicting delivery delays in advance

Estimating delivery costs based on multiple factors

Providing an interactive dashboard for decision-makers

This enables logistics teams to take proactive actions to reduce delays and optimize costs.

🧠 System Overview

Input logistics parameters (distance, traffic, weather, etc.)

Preprocess data and encode categorical features

Apply a machine learning regression model

Predict:

⏱️ Delivery delay (minutes)

💰 Estimated delivery cost (₹)

Display results through a simple web interface

📊 Dataset Description

The dataset used is synthetically generated, designed to closely resemble real-world logistics scenarios.

Features:

distance_km – Distance of delivery

traffic_level – Low / Medium / High

weather – Clear / Rain / Fog

package_weight – Weight of the package (kg)

delivery_slot – Morning / Afternoon / Evening

fuel_cost – Fuel cost per kilometer

Targets:

delay_minutes – Delivery delay

delivery_cost – Total delivery cost

📌 Note: The dataset is simulated due to the unavailability of proprietary logistics data, while maintaining realistic assumptions.

🤖 Machine Learning Model

Model Used: Random Forest Regressor

Type: Supervised Regression

Why Random Forest?

Handles non-linear relationships

Robust to noise

Interpretable and industry-friendly

Evaluation Metric:

Mean Absolute Error (MAE)

🖥️ User Interface

The application includes a Streamlit-based interactive dashboard that allows users to:

Input delivery parameters

Instantly view predicted delay and cost

Simulate different logistics scenarios

🛠️ Tech Stack

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn

Model Deployment: Joblib

Frontend/UI: Streamlit

📂 Project Structure
SmartRoutePlus/
├── data/
│   └── logistics_data.csv
├── model/
│   └── delay_cost_model.pkl
├── app/
│   └── app.py
├── train_model.py
├── requirements.txt
├── README.md

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install pandas scikit-learn streamlit joblib

2️⃣ Train the Model
python train_model.py

3️⃣ Run the Application
streamlit run app/app.py

📈 Business Impact

📉 Reduction in delivery delays (up to ~20%)

⛽ Optimized fuel usage and operational cost

📊 Better planning through predictive insights

😊 Improved customer satisfaction

🚀 Scalability & Future Enhancements

Integration with real-time GPS tracking

Live traffic and weather APIs

Route optimization algorithms

Enterprise-level deployment
