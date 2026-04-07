"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
from recommender import load_songs, recommend_songs

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "songs.csv")


def main() -> None:
    songs = load_songs(DATA_PATH)

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_prefs = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.40,
        "likes_acoustic": True
    }
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS")
    print("=" * 40)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
