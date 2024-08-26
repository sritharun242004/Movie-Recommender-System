import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment variable
TMDB_API_KEY = os.getenv("5c9b618a6739a3c302d0fcf82533ac8e")

# Ensure TMDB_API_KEY is loaded
if not TMDB_API_KEY:
    st.error("TMDB_API_KEY not found. Please ensure it is set in the .env file.")
    st.stop()

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    return ""

# Construct file paths relative to the script location
base_dir = os.path.dirname(__file__)
movies_path = os.path.join(base_dir, '..', 'models', 'movies_list.pkl')
similarity_path = os.path.join(base_dir, '..', 'models', 'similarity.pkl')

# Load the movies and similarity data
try:
    with open(movies_path, 'rb') as f:
        movies = pickle.load(f)
    with open(similarity_path, 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

movies_list = movies['title'].values

# Custom CSS for dark mode with lighter red header and button text
st.markdown("""
    <style>
    .stApp {
        background-color: #141414; /* Dark background color */
        color: #ffffff; /* Default text color */
    }
    .stHeader {
        color: #B22222; /* Lighter red color for header */
    }
    .stSelectbox {
        margin-bottom: 20px; /* Space below the dropdown */
    }
    .stButton>button {
        background-color: #B22222; /* Lighter red button background */
        color: #ffffff !important; /* White text color for the button */
        border: 1px solid #B22222; /* Lighter red border */
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #A00000; /* Darker red on hover */
        border: 1px solid #A00000;
    }
    .stText {
        color: #ffffff; /* Ensure text is readable */
    }
    .footer {
        position: fixed;
        right: 0;
        bottom: 0;
        width: 100%;
        background-color: #141414;
        color: white;
        text-align: right;
        padding: 10px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="stHeader">Movie Recommender System</h1>', unsafe_allow_html=True)

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
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.text(movie_name[i])
            st.image(movie_poster[i])

# Adding footer
st.markdown('<div class="footer">© Tharun</div>', unsafe_allow_html=True)