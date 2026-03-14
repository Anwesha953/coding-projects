import streamlit as st
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.write("DEBUG - app.py folder:", BASE_DIR)
st.write("DEBUG - files in this folder:", os.listdir(BASE_DIR))

model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

st.write("DEBUG - model path:", model_path)
st.write("DEBUG - model exists:", os.path.exists(model_path))
st.write("DEBUG - vectorizer exists:", os.path.exists(vectorizer_path))

# Load saved model and vectorizer
model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

st.title("📰 Fake News Detector")
st.write("Enter a news headline or short article to check if it looks REAL or FAKE.")

news_text = st.text_area("Enter news text here:")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        transformed_text = vectorizer.transform([news_text])
        prediction = model.predict(transformed_text)[0]

        if prediction == "FAKE":
            st.error("🚨 This news looks FAKE.")
        else:
            st.success("✅ This news looks REAL.")