import streamlit as st
import pickle
import requests
import time
import os
import gdown
file_id = "1r1-KJi39zayHZFdqZPopZqrbFGLawFO-"
url = f'https://drive.google.com/uc?id={file_id}'
similarity_file = "similarity.pkl"
if not os.path.exists("similarity.pkl"):
    gdown.download(url, 'similarity.pkl', quiet=False)
with open(similarity_file, 'rb') as f:
    simi = pickle.load(f)

# Load data
movies_list = pickle.load(open('movie_list.pkl', 'rb'))
movies = [str(title).strip() for title in movies_list['title'].tolist()]

# OMDb API Key
API_KEY = '7e69353e'


def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    data = requests.get(url).json()
    return data.get("Poster") if data.get("Response") == "True" else None


def recommend(movie):
    idx = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(simi[idx])), reverse=True, key=lambda x: x[1])[1:6]
    rec_titles, rec_posters = [], []
    for i in distances:
        title = movies_list.iloc[i[0]].title
        rec_titles.append(title)
        rec_posters.append(fetch_poster(title))
    return rec_titles, rec_posters


st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎥",
    layout="wide"
)

st.markdown(
    """
    <style>
    .title-text {
        font-size: 2.6rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .movie-title {
        font-size: 1rem;
        font-weight: 600;
        color: #2c3e50;
        text-align: center;
        margin-top: 0.5rem;
    }
    .movie-poster {
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #7f8c8d;
        margin-top: 3rem;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton > button {
        background: linear-gradient(to right, #3498db, #2980b9);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background: linear-gradient(to right, #2980b9, #3498db);
        transform: translateY(-1px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<h1 class="title-text">🎬 Movie Recommender System 🎥</h1>', unsafe_allow_html=True)

# Centered selectbox
select_col = st.columns([1, 2, 1])[1]
with select_col:
    sel_movie = st.selectbox(
        "Select a movie you like:",
        movies,
        index=0,
        key="movie_select"
    )

# Spacer and centered button below the selectbox
st.write("")  # spacing
button_col = st.columns([2, 1, 2])[1]
with button_col:
    recommend_btn = st.button("Get Recommendations")

st.markdown("---")

# Show results
if recommend_btn:
    with st.spinner("Finding the perfect recommendations..."):
        time.sleep(1.2)
        names, posters = recommend(sel_movie)

    st.subheader(f"Movies similar to: *{sel_movie}*")
    st.write("")
    cols = st.columns(5)
    for idx, (name, poster) in enumerate(zip(names, posters)):
        with cols[idx]:
            if poster and poster != "N/A":
                imdb_id = requests.get(f"http://www.omdbapi.com/?t={name}&apikey={API_KEY}").json().get("imdbID")
                if imdb_id:
                    imdb_url = f"https://www.imdb.com/title/{imdb_id}"
                    youtube_url = f"https://www.youtube.com/results?search_query={name} official trailer"
st.markdown(
    f"""
    <div class="movie-card" style="text-align:center">
        <a href="{imdb_url}" target="_blank">
            <img src="{poster}" class="movie-poster" alt="{name}">
        </a>
        <p class="movie-title">{name}</p>
        <a href="{youtube_url}" target="_blank" 
           style="color: #e74c3c; font-size: 0.9rem; font-weight: 600;">
           🎞 Watch Trailer
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



            else:
                st.markdown(
                    f"""
                    <div style="width:100%; height:300px; background:#ecf0f1;
                        display:flex; align-items:center; justify-content:center;
                        border-radius:8px; margin-bottom:10px;">
                        <span style="color:#7f8c8d;">Poster not available</span>
                    </div>
                    <div class="movie-title">{name}</div>
                    """,
                    unsafe_allow_html=True
                )

# Footer
st.markdown(
    """
    <div class="footer">
        Made with ❤️ by Abhinandan | Powered by OMDb API
        <br>
        <small>Movie data provided by OMDb API</small>
    </div>
    """,
    unsafe_allow_html=True
)
