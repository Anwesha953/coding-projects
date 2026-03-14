import streamlit as st
import pickle

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📰 Fake News Detector")
st.write("Enter a news headline or short article to check if it looks REAL or FAKE.")

# User input
news_text = st.text_area("Enter news text here:")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Convert input text
        transformed_text = vectorizer.transform([news_text])

        # Predict
        prediction = model.predict(transformed_text)[0]

        # Show result
        if prediction == "FAKE":
            st.error("🚨 This news looks FAKE.")
        else:
            st.success("✅ This news looks REAL.")