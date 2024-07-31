import streamlit as st
import pickle
import requests
import os

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=5c9b618a6739a3c302d0fcf82533ac8e&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Construct file paths relative to the script location
base_dir = os.path.dirname(__file__)
movies_path = os.path.join(base_dir, '..', 'models', 'movies_list.pkl')
similarity_path = os.path.join(base_dir, '..', 'models', 'similarity.pkl')

# Load the movies and similarity data
movies = pickle.load(open(movies_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))
movies_list = movies['title'].values

# Custom CSS for dark mode, text color, and spacing
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .stHeader {
        color: #ff0000; /* Red color for header */
    }
    .stSelectbox {
        margin-bottom: 20px; /* Add space below the dropdown */
    }
    .stButton>button {
        background-color: #6200ee;
        color: #ffffff;
        border: none;
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #3700b3;
    }
    .css-1v3fvcr {
        color: #e0e0e0;
    }
    .css-1y4f0z7 {
        color: #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

st.header("Movie Recommender System")

selectvalue = st.selectbox("Select movie from dropdown", movies_list, key="select_movie")

# Adding space between the dropdown and the button
st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
