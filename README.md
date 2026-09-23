# Machine-Learning-Model-To-Predict-IMDB-Scores
End-to-end movie data project: collecting data from TMDB API, exploratory analysis, and an ML model that predicts IMDb ratings based on genre, budget, runtime and more.

## Phase 1: Data Collection & Enrichment

### Overview
Built a data collection pipeline that pulls movie data from the TMDB API and enriches it with detailed information for analysis.

### What was done
- Connected to the TMDB API using Python
- Fetched 1,000 movies with core attributes (title, genres, ratings, popularity)
- Enriched each movie with detailed fields: budget, revenue, runtime, production countries and spoken languages
- Mapped genre IDs to readable genre names
- Saved structured data locally for analysis

### Dataset
| Field | Details |
|---|---|
| Source | TMDB API (themoviedb.org) |
| Size | 1,000 movies |
| Key columns | title, genres, budget, revenue, runtime, vote_average, vote_count, popularity, release_date |

### Files
| File | Description |
|---|---|
| `src/fetch_movies.py` | Fetches 1,000 movies from TMDB discover endpoint |
| `src/fetch_genres.py` | Fetches genre ID to name mapping |
| `src/fetch_movie_details.py` | Enriches each movie with detailed fields |

### Tools & Libraries
Python, Requests, Pandas, Python-dotenv

### How to run
1. Get a free API key from [themoviedb.org](https://www.themoviedb.org)
2. Create a `.env` file and add: `TMDB_API_KEY=your_key_here`
3. Run scripts in order:
python src/fetch_movies.py
python src/fetch_genres.py
python src/fetch_movie_details.py
