# 🎓 Student Performance AI

AI-powered web application that predicts a student's final academic score based on study habits, attendance, previous performance, assignment completion, and sleep hours.

## 🌐 Live Demo

👉 [Try the Student Performance AI](https://student-performance-ai-jfowttdhpxhjephmacegvw.streamlit.app/)

## 🚀 Features

- 🎯 Predicts final student score
- 🏆 Classifies performance level
- ⚠️ Identifies academic risk level
- 💡 Provides personalized recommendations
- 🤖 Uses a Random Forest machine learning model
- 🌐 Interactive Streamlit web interface

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Git & GitHub

## 📊 Machine Learning Model

The application uses a **Random Forest Regressor** to predict the student's final score.

### Input Features

- Study Hours
- Attendance
- Previous Score
- Assignments Completed
- Sleep Hours

### Model Evaluation

- Mean Absolute Error (MAE): **1.43**
- R² Score: **0.94**

> Note: This project uses a small educational dataset and is intended as a demonstration/portfolio project.

## 📁 Project Structure

```text
student-performance-ai/
├── data/
│   └── student_data.csv
├── models/
│   └── student_performance_model.pkl
├── notebooks/
├── venv/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore