import streamlit as st
import joblib
import pandas as pd


# Page configuration
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)


# Custom UI styling
st.markdown("""
<style>
    .stApp {
    background: #dbeafe !important;
}

[data-testid="stAppViewContainer"] {
    background: #dbeafe !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

    h1 {
        color: #1e293b;
    }

    h2, h3 {
        color: #334155;
    }

    .stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    [data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    """
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <h1>🎓 Student Performance AI</h1>
        <p style="font-size: 18px; color: #6b7280;">
            AI-powered student performance prediction
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# Introduction
st.write(
    "Enter student details below to predict the final academic score."
)


# Student details
st.subheader("📋 Student Details")

st.caption(
    "Enter the student's academic and lifestyle details below."
)


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


# Load trained model
model = joblib.load("models/student_performance_model.pkl")


# Prediction section
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


    # Prediction result
    st.markdown("### 📈 Prediction Result")


    st.metric(
        label="🎯 Predicted Final Score",
        value=f"{prediction:.2f} / 100"
    )


    # Performance level
    if prediction >= 85:
        performance = "Excellent 🏆"
    elif prediction >= 70:
        performance = "Good 👍"
    elif prediction >= 50:
        performance = "Average 📚"
    else:
        performance = "Needs Improvement ⚠️"


    # Risk level
    if prediction >= 70:
        risk = "Low Risk 🟢"
    elif prediction >= 50:
        risk = "Medium Risk 🟡"
    else:
        risk = "High Risk 🔴"


    # Performance and risk cards
    col1, col2 = st.columns(2)


    with col1:
        st.markdown(
            f"""
            <div style="
                background-color: white;
                padding: 20px;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
                text-align: center;
            ">
                <h4>🏆 Performance Level</h4>
                <h3>{performance}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:
        st.markdown(
            f"""
            <div style="
                background-color: white;
                padding: 20px;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
                text-align: center;
            ">
                <h4>⚠️ Risk Level</h4>
                <h3>{risk}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )


    # Recommendations
    recommendations = []


    if study_hours < 4:
        recommendations.append(
            "📚 Try to increase your study time."
        )


    if attendance < 75:
        recommendations.append(
            "🏫 Improve your class attendance."
        )


    if previous_score < 60:
        recommendations.append(
            "📝 Focus on improving your previous academic performance."
        )


    if assignments < 7:
        recommendations.append(
            "📋 Complete more assignments regularly."
        )


    if sleep_hours < 6:
        recommendations.append(
            "😴 Maintain at least 6 hours of sleep."
        )


    if not recommendations:
        recommendations.append(
            "🌟 Keep up the good work and maintain your current habits!"
        )


    # Recommendation section
    st.subheader("💡 Recommendations")


    st.caption(
        "Personalized suggestions based on the student's academic and lifestyle inputs."
    )


    for recommendation in recommendations:
        st.markdown(
            f"""
            <div style="
                background-color: white;
                padding: 14px 18px;
                margin-bottom: 10px;
                border-radius: 10px;
                border-left: 5px solid #2563eb;
                border-top: 1px solid #e5e7eb;
                border-right: 1px solid #e5e7eb;
                border-bottom: 1px solid #e5e7eb;
            ">
                {recommendation}
            </div>
            """,
            unsafe_allow_html=True
        )


    st.divider()


# About section
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


# Model performance
st.subheader("📊 Model Performance")


col1, col2 = st.columns(2)


with col1:
    st.metric(
        "Mean Absolute Error (MAE)",
        "1.43"
    )


with col2:
    st.metric(
        "R² Score",
        "0.94"
    )


st.divider()


# Footer
st.caption(
    "🎓 Student Performance AI | Built with Python, Scikit-learn & Streamlit"
)