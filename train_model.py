import pandas as pd

# Load the dataset
data = pd.read_csv("data/student_data.csv")

# Display the first 5 rows
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# Separate features and target

X = data[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments",
        "sleep_hours"
    ]
]

y = data["final_score"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:")
print(X_train.shape)

print("\nTesting data:")
print(X_test.shape)

from sklearn.ensemble import RandomForestRegressor

# Create the Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("\nModel training completed successfully!")

# Make predictions on the test data
y_pred = model.predict(X_test)

print("\nActual Scores:")
print(y_test.values)

print("\nPredicted Scores:")
print(y_pred)

from sklearn.metrics import mean_absolute_error, r2_score

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

import joblib

# Save the trained model
joblib.dump(model, "models/student_performance_model.pkl")

print("\nModel saved successfully!")