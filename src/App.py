import streamlit as st
import pickle
import requests
import os

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=5c9b618a6739a3c302d0fcf82533ac8e&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

# Construct file paths relative to the script location
base_dir = os.path.dirname(__file__)
movies_path = os.path.join(base_dir, '..', 'models', 'movies_list.pkl')
similarity_path = os.path.join(base_dir, '..', 'models', 'similarity.pkl')

# Load the movies and similarity data
try:
    movies = pickle.load(open(movies_path, 'rb'))
    similarity = pickle.load(open(similarity_path, 'rb'))
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

movies_list = movies['title'].values

# Custom CSS for dark mode with red and black theme
st.markdown("""
    <style>
    .stApp {
        background-color: #141414; /* Dark background color */
        color: #ffffff; /* Default text color */
    }
    .stHeader {
        color: #ff0000; /* Red color for header */
    }
    .stSelectbox {
        margin-bottom: 20px; /* Space below the dropdown */
    }
    .stButton>button {
        background-color: #ff0000; /* Red button background */
        color: #ffffff; /* White text color for the button */
        border: 1px solid #ff0000; /* Red border */
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #e60000; /* Darker red on hover */
        border: 1px solid #e60000;
    }
    .stText {
        color: #ffffff; /* Ensure text is readable */
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