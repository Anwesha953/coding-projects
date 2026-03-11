import streamlit as st
from textblob import TextBlob

st.title("AI Sentiment Analyzer")

text = st.text_area("Enter text to analyze sentiment")

if st.button("Analyze Sentiment"):

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("Positive Sentiment 😊")
    elif polarity < 0:
        st.error("Negative Sentiment 😠")
    else:
        st.info("Neutral Sentiment 😐")

    st.write("Polarity Score:", polarity)