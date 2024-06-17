import streamlit as st
import pickle
import gdown
import os

# Function to download files from Google Drive
def download_files():
    url_movies = 'https://drive.google.com/file/d/1PgyfKRXUXBUQ3sGXJMMVnWoeAtAkmQA5/view?usp=drive_link'
    url_similarity = 'https://drive.google.com/file/d/1uIPbBw58MRGOWPMN73lr97kuYYj9L63o/view?usp=drive_link'
    output_movies = 'movies.pkl'
    output_similarity = 'similarity.pkl'
    
    if not os.path.exists(output_movies):
        gdown.download(url_movies, output_movies, quiet=False)
        
    if not os.path.exists(output_similarity):
        gdown.download(url_similarity, output_similarity, quiet=False)

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
