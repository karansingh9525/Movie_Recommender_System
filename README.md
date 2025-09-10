# 🎬 Movie Recommender System
Link: https://movie-recommender-system-fzlpwu2qsg6je3pmvskxsk.streamlit.app/

A powerful content-based movie recommender system built using Python and Streamlit. It suggests movies similar to the one you enter, displaying posters, IMDb links, and YouTube trailers for an enhanced user experience.

---

## 🚀 Features

- 🔍 **Search-Based Recommendation**: Enter a movie name to get top 5 similar movies.
- 🖼️ **Movie Posters**: Each recommendation displays the official poster.
- 🎞️ **IMDb Integration**: Clickable titles redirect to IMDb pages for more details.
- ▶️ **Trailer Support**: Embedded YouTube trailers for a quick preview.
- ☁️ **Model Loading from Google Drive**: Loads a large similarity model hosted externally.

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend**: Python  
- **Modeling**: Cosine similarity on movie feature vectors  
- **API Used**: [OMDb API](http://www.omdbapi.com/) for movie metadata  
- **Hosting**: Streamlit Cloud (or alternative free deployment platforms)

---

## 📂 Project Structure

├── app.py # Main Streamlit app
├── movie_list.pkl # Contains movie titles and metadata
├── similarity.pkl # Precomputed similarity matrix (loaded from Google Drive)
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## 💡 How It Works

1. User enters a movie title.  
2. The app finds the closest match and retrieves the top 5 most similar movies using cosine similarity.  
3. Poster images are fetched using the OMDb API.  
4. The results include:  
   - Poster  
   - Movie name  
   - IMDb redirection  
   - YouTube trailer link  

---

## 🌐 Deployment

The app can be deployed for free on:  
- **Streamlit Community Cloud**  
- **Render**  
- **Railway**  

> Note: The `similarity.pkl` file exceeds 100MB, so it is hosted on Google Drive and downloaded at runtime using `gdown`.
---

## 🔒 Environment Variables

For security, use a `.env` file to store your API keys:

OMDB_API_KEY=your_api_key_here

Then load them in Python using:

```python
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OMDB_API_KEY")

🙌 Acknowledgments
OMDb API

Streamlit

Dataset from Kaggle (TMDB 5000 Movie Dataset)

📧 Contact
Abhinandan Sharma
Feel free to reach out via LinkedIn or raise an issue in this repo!
Linkedin: https://www.linkedin.com/in/abhinandan-sharma-b1b9b5283/

---

Let me know if you’d like to add a [live demo link](f) or [setup instructions](f) to the README as 
