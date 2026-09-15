import streamlit as st

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance AI")

st.caption("AI-powered student performance prediction and personalized recommendations")
st.divider()

st.write(
    "Enter student details below to predict the final academic score."
)

st.subheader("📋 Student Details")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=15.0,
        value=4.0,
        step=0.5
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=80,
        step=1
    )

    previous_score = st.number_input(
        "Previous Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )

with col2:
    assignments = st.number_input(
        "Assignments Completed",
        min_value=0,
        max_value=10,
        value=8,
        step=1
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=12.0,
        value=7.0,
        step=0.5
    )

import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/student_performance_model.pkl")

st.subheader("🤖 AI Prediction")

st.write("")

if st.button("🔮 Predict Final Score", use_container_width=True):

    # Create input data
    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_score": [previous_score],
        "assignments": [assignments],
        "sleep_hours": [sleep_hours]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success("Prediction generated successfully! 🎉")

    st.metric(
        label="🎯 Predicted Final Score",
        value=f"{prediction:.2f} / 100"
    )

    # Determine performance level
    if prediction >= 85:
        performance = "Excellent 🏆"
    elif prediction >= 70:
        performance = "Good 👍"
    elif prediction >= 50:
        performance = "Average 📚"
    else:
        performance = "Needs Improvement ⚠️"

    # Determine risk level
    if prediction >= 70:
        risk = "Low Risk 🟢"
    elif prediction >= 50:
        risk = "Medium Risk 🟡"
    else:
        risk = "High Risk 🔴"

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"🏆 Performance Level\n\n{performance}")

    with col2:
        st.warning(f"⚠️ Risk Level\n\n{risk}")

    # Generate recommendations
    recommendations = []

    if study_hours < 4:
        recommendations.append("📚 Try to increase your study time.")

    if attendance < 75:
        recommendations.append("🏫 Improve your class attendance.")

    if previous_score < 60:
        recommendations.append("📝 Focus on improving your previous academic performance.")

    if assignments < 7:
        recommendations.append("📋 Complete more assignments regularly.")

    if sleep_hours < 6:
        recommendations.append("😴 Maintain at least 6 hours of sleep.")

    if not recommendations:
        recommendations.append("🌟 Keep up the good work and maintain your current habits!")

    st.subheader("💡 Recommendations")

    st.caption("Personalized suggestions based on the student's academic and lifestyle inputs.")

    for recommendation in recommendations:
        st.write(recommendation)

    st.divider()

st.subheader("ℹ️ About This AI Model")

st.write(
    "This application uses a Random Forest Regressor machine learning model "
    "to predict a student's final academic score based on study habits, "
    "attendance, previous performance, assignment completion, and sleep hours."
)

st.write(
    "The model was trained using a student performance dataset and evaluated "
    "using Mean Absolute Error (MAE) and R² Score."
)

st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("Mean Absolute Error (MAE)", "1.43")

with col2:
    st.metric("R² Score", "0.94")

st.divider()

st.caption("🎓 Student Performance AI | Built with Python, Scikit-learn & Streamlit")