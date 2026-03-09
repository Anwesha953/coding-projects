import streamlit as st
import pickle

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

st.title("Spam Message Classifier")

message = st.text_input("Enter a message")

if st.button("Check"):
    data = vectorizer.transform([message])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("This message is Spam")
    else:
        st.success("This message is Not Spam")