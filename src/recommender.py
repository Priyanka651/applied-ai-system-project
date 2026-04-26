import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.0

            energy_diff = abs(song.energy - user.target_energy)
            energy_score = max(0, 1 - energy_diff)
            score += energy_score

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda x: x[1], reverse=True)

        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("genre matches your preference")

        if song.mood == user.favorite_mood:
            reasons.append("mood matches your preference")

        energy_diff = abs(song.energy - user.target_energy)
        reasons.append(f"energy is close to your target ({song.energy:.2f})")

        if user.likes_acoustic and song.acousticness > 0.7:
            reasons.append("it has a strong acoustic feel")

        if reasons:
            return "Recommended because " + ", ".join(reasons) + "."
        return "Recommended because it is a good match."


def load_songs(csv_path: str) -> List[Dict]:
    songs: List[Dict] = []
    print(f"Loading songs from {csv_path}...")

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs


def get_confidence(score: float) -> str:
    if score >= 3.0:
        return "High"
    elif score >= 2.0:
        return "Medium"
    else:
        return "Low"


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if "mood" in user_prefs and song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = max(0, 1 - energy_diff)
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    return score, reasons


def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str, str]]:
    if not songs:
        return []

    if k <= 0:
        return []

    results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " & ".join(reasons)
        confidence = get_confidence(score)
        results.append((song, score, explanation, confidence))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:k]