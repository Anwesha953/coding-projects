import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get 5 similar movie recommendations based on genre.")

# Load dataset
movies = pd.read_csv("movies.csv")

# Show small preview (optional but good for demo)
with st.expander("Preview Dataset"):
    st.dataframe(movies.head(10))

# Convert genre text into vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

# Calculate similarity matrix
similarity = cosine_similarity(genre_matrix)

# Movie selection
movie_list = movies["title"].values
selected_movie = st.selectbox("Choose a movie", movie_list)

def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_indices = distances.argsort()[-6:-1][::-1]
    return movies.iloc[movie_indices]["title"].tolist()

if st.button("Recommend Movies"):
    recommendations = recommend(selected_movie)

    st.subheader("🎥 Recommended Movies")
    for movie in recommendations:
        st.write("•", movie)