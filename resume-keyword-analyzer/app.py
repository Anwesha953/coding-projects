import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Keyword Analyzer")

resume = st.text_area("Paste Your Resume")

job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Match"):

    text = [resume, job_desc]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    similarity = cosine_similarity(count_matrix)[0][1]

    score = round(similarity * 100, 2)

    st.subheader("Match Score")
    st.write(str(score) + "%")

    if score > 70:
        st.success("Great match for this job!")
    elif score > 40:
        st.warning("Moderate match. Consider adding more keywords.")
    else:
        st.error("Low match. Resume needs improvement.")