# Movie Recommendation System Built Using ML and Streamlit

This project demonstrates the development of a simple movie recommendation system using two well-known and popular CSV files: movies and credits.

The notebooks provide a brief preprocessing step to adapt the main columns from the data frames for use in the recommendation system. The PorterStemmer has also been utilized to standardize the text data. After preprocessing, two PKL files have been exported to save the data frame with the basic information about the movies (movie_id, title, and tags), and the vector used to calculate cosine similarity. These files are then exported for further use.

The data used in this project was downloaded from:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

After creating an account on The Movie Database (TMDb), you will need to generate an API Key to make requests:
https://www.themoviedb.org/settings/api

For understanding how to retrieve images from the API, refer to:
https://developer.themoviedb.org/docs/image-basics

**Basic Structure**
```
recommendation-system/
├── artifacts/
├── data/
├── env/
├── images/
├── notebooks/
├── src/
├── .env
├── .gitignore
├── app.py
├── LICENSE
├── Procfile
├── README.md
├── requirements.txt
├── setup.py
└── setup.sh
```