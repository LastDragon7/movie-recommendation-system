import streamlit as st
import pickle

def recommend(movie):
    i = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[i])), reverse=True, key=lambda x: x[1])
    recommend_movie_name = []
    for i in distances[1:6]:
        id = movies.iloc[i[0]].id
        recommend_movie_name.append(movies.iloc[i[0]].title)
    return recommend_movie_name

st.title('Movie Recommendation System')
movies = pickle.load(open('movie-recommendation-system\movies-recommendation-system\movies.pkl','rb'))
similarity = pickle.load(open('movie-recommendation-system\movies-recommendation-system\similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommned'):
    names = recommend(selected_movie)
    for i in names:
        st.write(i)


