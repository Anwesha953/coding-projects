import streamlit as st
import pickle

import os
import pickle

base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "model.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer_path = os.path.join(base_dir, "vectorizer.pkl")
vectorizer = pickle.load(open(vectorizer_path, "rb"))

st.title("Spam Message Classifier")

message = st.text_input("Enter a message")

if st.button("Check"):
    data = vectorizer.transform([message])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("This message is Spam")
    else:
        st.success("This message is Not Spam")