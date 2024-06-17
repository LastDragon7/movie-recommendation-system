import streamlit as st
import pickle
import gdown
import os
import sys

# Function to download files from Google Drive
def download_files():
    url_movies = 'https://drive.google.com/uc?id=<movies_file_id>'
    url_similarity = 'https://drive.google.com/uc?id=<similarity_file_id>'
    output_movies = 'movies.pkl'
    output_similarity = 'similarity.pkl'
    
    if not os.path.exists(output_movies):
        with open(os.devnull, 'w') as devnull:
            sys.stdout = devnull
            gdown.download(url_movies, output_movies, quiet=True)
            sys.stdout = sys.__stdout__
        
    if not os.path.exists(output_similarity):
        with open(os.devnull, 'w') as devnull:
            sys.stdout = devnull
            gdown.download(url_similarity, output_similarity, quiet=True)
            sys.stdout = sys.__stdout__

# Download the files
download_files()

# Function to recommend movies
def recommend(movie):
    i = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[i])), reverse=True, key=lambda x: x[1])
    recommend_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommend_movie_names

# Title of the app
st.title('Movie Recommendation System')

# Load the downloaded files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Recommendation button
if st.button('Recommend'):
    names = recommend(selected_movie)
    for name in names:
        st.write(name)
