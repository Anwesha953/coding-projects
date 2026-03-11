import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎬 Movie Recommendation System")

movies = pd.read_csv("movies.csv")

st.write("### Movie Dataset Preview")
st.dataframe(movies.head())

# Convert genre text to numerical vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(genre_matrix)

movie_list = movies["title"].values

selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend Movies"):

    movie_index = movies[movies["title"] == selected_movie].index[0]

    distances = similarity[movie_index]

    movie_indices = distances.argsort()[-6:-1][::-1]

    st.write("### Recommended Movies")

    for i in movie_indices:
        st.write(movies.iloc[i]["title"])