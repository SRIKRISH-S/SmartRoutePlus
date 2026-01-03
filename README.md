# 🚚 SmartRoutePlus  
## AI-Based Delivery Delay & Cost Optimization System

SmartRoutePlus is an end-to-end **machine learning–based logistics optimization system** developed for the **FedEx SMART Hackathon** conducted as part of **Shaastra 2026**.  
The project focuses on predicting **delivery delays** and **delivery costs** using data-driven intelligence to support smarter and more efficient logistics operations.

---

## 📌 Problem Statement
Logistics companies such as **:contentReference[oaicite:0]{index=0}** face critical operational challenges including:
- Unpredictable delivery delays  
- Rising fuel and transportation costs  
- Traffic congestion and adverse weather conditions  
- Inefficient route planning and prioritization  

Most existing systems are **reactive**, responding only after delays occur, which results in increased cost and customer dissatisfaction.

---

## 💡 Proposed Solution
SmartRoutePlus introduces a **predictive and proactive approach** to logistics management by:
- Predicting delivery delays in advance  
- Estimating delivery costs using multiple influencing factors  
- Providing an interactive dashboard for scenario simulation  

This allows logistics managers to make **data-driven decisions** before deliveries are executed.

---

## 🧠 System Workflow
1. User inputs logistics parameters (distance, traffic, weather, etc.)
2. Data is preprocessed and categorical features are encoded
3. A machine learning regression model is applied
4. The system predicts:
   - ⏱️ Delivery delay (in minutes)
   - 💰 Estimated delivery cost (in ₹)
5. Results are displayed via a simple and interactive web interface

---

## 📊 Dataset Description
The dataset used in this project is **synthetically generated** to closely resemble real-world logistics scenarios.

### Input Features
- `distance_km` – Delivery distance in kilometers  
- `traffic_level` – Low / Medium / High  
- `weather` – Clear / Rain / Fog  
- `package_weight` – Package weight in kilograms  
- `delivery_slot` – Morning / Afternoon / Evening  
- `fuel_cost` – Fuel cost per kilometer  

### Target Variables
- `delay_minutes` – Delivery delay  
- `delivery_cost` – Estimated delivery cost  

> ⚠️ Note: Real logistics datasets are proprietary. Hence, realistic assumptions were used to simulate data while maintaining industry relevance.

---

## 🤖 Machine Learning Model
- **Model Type:** Supervised Regression  
- **Algorithm Used:** Random Forest Regressor  

### Why Random Forest?
- Handles non-linear relationships effectively  
- Robust to noise and overfitting  
- Interpretable and widely used in industry  

### Evaluation Metric
- Mean Absolute Error (MAE)

---

## 🖥️ User Interface
The project includes a **Streamlit-based web application** that enables users to:
- Enter delivery-related parameters  
- Instantly view predicted delay and cost  
- Experiment with multiple logistics scenarios  

This UI demonstrates how the model can be used in a real operational environment.

---

## 🛠️ Technology Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Model Serialization:** Joblib  
- **Frontend/UI:** Streamlit  

---

## 📂 Project Structure
