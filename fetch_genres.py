import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def fetch_genres():
    """Fetch the full list of TMDB genre IDs and their names."""
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }
    response=requests.get(url, params=params)
    genres=response.json()["genres"]
    
    genre_dict = {g["id"]:g["name"] for g in genres}
    return genre_dict

if __name__ == "__main__":
    genres= fetch_genres()
    print("Genre mapping fetched!")
    print(genres)

    with open("data/genres.json", "w") as f:
        json.dump(genres,f, indent=2)
    print("\nSaved to data/genres.json!")

