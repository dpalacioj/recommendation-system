import os
import pickle
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_poster(movie_id):
    api_key = os.getenv('TMDB_API_KEY')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path')
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(simularity[index])), reverse=True, key = lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster


st.header("Movies Recommendation System Using Machine Learning")

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
simularity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox('Type or select a movie to get recommendation',
             movie_list)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    cols = st.columns(5)
    for col, name, poster in zip(cols, recommended_movies_name, recommended_movies_poster):
        with col:
            st.text(name)
            st.image(poster)