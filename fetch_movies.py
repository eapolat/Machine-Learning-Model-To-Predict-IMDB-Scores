import requests
import pandas as pd
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies(page):
    """Fetch one page of popular movies from TMDB."""
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "vote_count.gte": 100,
        "page": page
    }
    response = requests.get(url,params=params)

    if response.status_code == 200:
        return response.json()["results"]
    else:
        print(f"Error on page {page}: {response.status_code}")
        return []
    
def fench_all_movies(num_pages=50):
    """Fetch multiple pages and combine into a DataFrame."""
    all_movies = []
    
    for page in range(1, num_pages+1):
        print(f"Fetching page {page}/{num_pages}...")
        movies = fetch_movies(page)
        all_movies.extend(movies)
        time.sleep(0.3)  # Be polite to the API, don't spam requests

    df = pd.DataFrame(all_movies)
    return df

if __name__ == "__main__":
    print("Starting TMDB data fetch...")
    df = fench_all_movies(num_pages=50)
    print(f"\nFetched {len(df)} movies!")
    print("\nColumns available:")
    print(df.columns.tolist())
    print("\nFirst few rows:")
    print(df.head())

    df.to_csv("data/movies_raw.csv", index=False)
    print("\nData saved to data/movies_raw.csv!")


