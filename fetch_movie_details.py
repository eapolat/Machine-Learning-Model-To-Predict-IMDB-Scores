
import requests
import pandas as pd
import time
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies_details(movie_id):
    """Fetch detailed info for a single movie."""
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "en-US"
        }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching movie{movie_id}:{response.status_code}")
        return None
    
def extract_fields(movie):
    """Pull only the fields we care about from the raw response."""

    return {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "release_date": movie.get("release_date"),
        "runtime": movie.get("runtime"),
        "budget": movie.get("budget"),
        "revenue": movie.get("revenue"),
        "vote_average": movie.get("vote_average"),
        "vote_count": movie.get("vote_count"),
        "popularity": movie.get("popularity"),
        "original_language": movie.get("original_language"),
        "overview": movie.get("overview"),

        "genres": [g["name"] for g in movie.get("genres", [])],
        "production_countries": [c["name"] for c in movie.get("production_countries", [])],
        "spoken_languages": [l["name"] for l in movie.get("spoken_language", [])]
    }

if __name__ == "__main__":

    df = pd.read_csv("data/movies_raw.csv")
    movie_ids = df["id"].tolist()

    print(f"Fetching details for {len(movie_ids)} movies...")
    print("This will take a few minutes, please wait...\n")

    detailed_movies = []
    failed = []

    for i, movie_id in enumerate(movie_ids):
        details = fetch_movies_details(movie_id)

        if details:
            detailed_movies.append(extract_fields(details))
        else: 
            failed.append(movie_id)

        # Progress update every 100 movies
        if (i+1) % 100 == 0:
            print(f"Progress: {i+1}/{len(movie_ids)} movies fetched...")

        time.sleep(0.25) # Respect API rate limits

    # Save results
    df_detailed = pd.DataFrame(detailed_movies)
    df_detailed.to_csv("data/movies_detailed.csv", index=False)

    print(f"\nDone! Fetched details for {len(detailed_movies)} movies!")
    print(f"Failed: {len(failed)} movies.")
    print("\nColumns in detailed dataset:")
    print(df_detailed.columns.to_list())
    print("\nSample Data:")
    print(df_detailed[["title", "runtime", "budget", "revenue", "vote_average", "genres"]].head())

        
    

