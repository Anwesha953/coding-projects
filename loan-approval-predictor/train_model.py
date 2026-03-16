import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Get current folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
csv_path = os.path.join(BASE_DIR, "loan_data.csv")
model_path = os.path.join(BASE_DIR, "model.pkl")
columns_path = os.path.join(BASE_DIR, "columns.pkl")

# Load dataset
df = pd.read_csv(csv_path)

# Features and target
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

# One-hot encode categorical columns
X_encoded = pd.get_dummies(X)

# Save training columns
training_columns = X_encoded.columns.tolist()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred, labels=["Approved", "Not Approved"])
report = classification_report(y_test, y_pred)

print("\nModel Evaluation Results")
print("=" * 40)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print("Rows = Actual, Columns = Predicted")
print("Labels order: [Approved, Not Approved]")
print(cm)

print("\nClassification Report:")
print(report)

# Save model
with open(model_path, "wb") as f:
    pickle.dump(model, f)

# Save training columns
with open(columns_path, "wb") as f:
    pickle.dump(training_columns, f)

print("\nModel and columns saved successfully!")