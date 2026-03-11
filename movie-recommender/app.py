import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Movie Recommendation System")

movies = pd.read_csv("movies.csv")

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genre"])

cosine_sim = cosine_similarity(tfidf_matrix)

movie_list = movies["title"].values

selected_movie = st.selectbox("Select a movie", movie_list)

def recommend(movie):

    index = movies[movies["title"] == movie].index[0]
    scores = list(enumerate(cosine_sim[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    scores = scores[1:6]

    movie_indices = [i[0] for i in scores]

    return movies["title"].iloc[movie_indices]

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)