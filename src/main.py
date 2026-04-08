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
    # Define at least three distinct user preference dictionaries (e.g., "High-Energy Pop," "Chill Lofi," "Deep Intense Rock").
    user_prefs2 = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False
    }
    user_prefs3 = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9,
        "likes_acoustic": False
    }
    recommendations = recommend_songs(user_prefs, songs, k=5)

    # print("\n" + "=" * 40)
    # print("  TOP RECOMMENDATIONS FOR USER 1")
    # print("=" * 40)

    # for i, (song, score, explanation) in enumerate(recommendations, start=1):
    #     print(f"\n#{i}  {song['title']} by {song['artist']}")
    #     print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
    #     print(f"    Score: {score:.2f} / 4.50")
    #     print(f"    Why:   {explanation}")

    # print("\n" + "=" * 40)

    # print("  TOP RECOMMENDATIONS FOR USER 2")
    # print("=" * 40)

    # recommendations2 = recommend_songs(user_prefs2, songs, k=5)
    # for i, (song, score, explanation) in enumerate(recommendations2, start=1):
    #     print(f"\n#{i}  {song['title']} by {song['artist']}")
    #     print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
    #     print(f"    Score: {score:.2f} / 4.50")
    #     print(f"    Why:   {explanation}")

    # print("\n" + "=" * 40)
    # print("  TOP RECOMMENDATIONS FOR USER 3")
    # print("=" * 40)
    # recommendations3 = recommend_songs(user_prefs3, songs, k=5)
    # for i, (song, score, explanation) in enumerate(recommendations3, start=1):
    #     print(f"\n#{i}  {song['title']} by {song['artist']}")
    #     print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
    #     print(f"    Score: {score:.2f} / 4.50")
    #     print(f"    Why:   {explanation}")


    # Add edge cases
    user_adversarial_1 = {
        "favorite_genre": "blues",
        "favorite_mood": "sad",
        "target_energy": 0.95,   # wants high energy...
        "likes_acoustic": False  # ...but sad songs are all low energy (0.22–0.44)
    }

    user_adversarial_2 = {
        "favorite_genre": "bossa nova",  # no songs have this genre
        "favorite_mood": "chill",
        "target_energy": 0.4,
        "likes_acoustic": True
    }

    user_adversarial_3 = {
        "favorite_genre": "edm",
        "favorite_mood": "euphoric",
        "target_energy": 0.94,
        "likes_acoustic": True   # EDM acousticness is 0.03 — never gets +0.5
    }

    user_adversarial_4 = {
        "favorite_genre": "lofi",
        "favorite_mood": "aggressive",  # no lofi song has mood=aggressive
        "target_energy": 0.5,
        "likes_acoustic": False
    }

    user_adversarial_5 = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 1.5,   # outside valid range [0.0, 1.0]
        "likes_acoustic": False
    }

    user_adversarial_6 = {
        "favorite_genre": "Pop",    # capital P — won't match "pop" in CSV
        "favorite_mood": "Happy",   # capital H — won't match "happy"
        "target_energy": 0.8,
        "likes_acoustic": False
    }

    user_adversarial_7 = {
        "favorite_genre": "folk",        # Glass and Rain: folk ✓
        "favorite_mood": "melancholic",  # Glass and Rain: melancholic ✓
        "target_energy": 0.25,           # Glass and Rain: energy=0.25 → +1.0 ✓
        "likes_acoustic": True           # Glass and Rain: acousticness=0.95 → +0.5 ✓
    }

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS FOR ADVERSARIAL USER 1")
    print("=" * 40)
    recommendations_adv1 = recommend_songs(user_adversarial_1, songs, k=5)
    for i, (song, score, explanation) in enumerate(recommendations_adv1, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS FOR ADVERSARIAL USER 2")
    print("=" * 40)
    recommendations_adv2 = recommend_songs(user_adversarial_2, songs, k=5)
    for i, (song, score, explanation) in enumerate(recommendations_adv2, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS FOR ADVERSARIAL USER 3")
    print("=" * 40)
    recommendations_adv3 = recommend_songs(user_adversarial_3, songs, k=5)
    for i, (song, score, explanation) in enumerate(recommendations_adv3, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS FOR ADVERSARIAL USER 4")
    print("=" * 40)
    recommendations_adv4 = recommend_songs(user_adversarial_4, songs, k=5)
    for i, (song, score, explanation) in enumerate(recommendations_adv4, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS FOR ADVERSARIAL USER 5")
    print("=" * 40)
    recommendations_adv5 = recommend_songs(user_adversarial_5, songs, k=5)
    for i, (song, score, explanation) in enumerate(recommendations_adv5, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS FOR ADVERSARIAL USER 6")
    print("=" * 40)
    recommendations_adv6 = recommend_songs(user_adversarial_6, songs, k=5)
    for i, (song, score, explanation) in enumerate(recommendations_adv6, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS FOR ADVERSARIAL USER 7")
    print("=" * 40)
    recommendations_adv7 = recommend_songs(user_adversarial_7, songs, k=5)
    for i, (song, score, explanation) in enumerate(recommendations_adv7, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:   {explanation}")


if __name__ == "__main__":
    main()
