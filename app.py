import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b247c4714e334a1d61f95aa3f9b49c03&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    i = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[i])), reverse=True, key=lambda x: x[1])
    recommend_movie_name = []
    poster = []
    for i in distances[1:6]:
        id = movies.iloc[i[0]].id
        poster.append(fetch_poster(id))
        recommend_movie_name.append(movies.iloc[i[0]].title)
    return recommend_movie_name,poster

st.title('Movie Recommendation System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommned'):
    names,posters = recommend(selected_movie)
    cols = st.columns(5)
    for col,name,poster in zip(cols,names,posters):
        with col:
            st.write(name)
            st.image(poster)
