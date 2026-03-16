import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Get current folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
csv_path = os.path.join(BASE_DIR, "fake_or_real_news.csv")
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

# Load dataset
df = pd.read_csv(csv_path)

# Features and labels
X = df["text"]
y = df["label"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train model
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(X_train_vectorized, y_train)

# Predictions
y_pred = model.predict(X_test_vectorized)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred, labels=["FAKE", "REAL"])
report = classification_report(y_test, y_pred)

print("\nModel Evaluation Results")
print("=" * 40)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print("Rows = Actual, Columns = Predicted")
print("Labels order: [FAKE, REAL]")
print(cm)

print("\nClassification Report:")
print(report)

# Save model and vectorizer
with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(vectorizer_path, "wb") as f:
    pickle.dump(vectorizer, f)

print("\nModel and vectorizer saved successfully!")