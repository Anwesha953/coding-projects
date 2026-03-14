import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Get folder where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Full paths
csv_path = os.path.join(BASE_DIR, "fake_or_real_news.csv")
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

# Load dataset
df = pd.read_csv(csv_path)

# Features and labels
X = df["text"]
y = df["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model files in same folder
pickle.dump(model, open(model_path, "wb"))
pickle.dump(vectorizer, open(vectorizer_path, "wb"))

print("Model and vectorizer saved successfully!")