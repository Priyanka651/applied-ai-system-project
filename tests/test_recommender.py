from src.recommender import (
    Song,
    UserProfile,
    Recommender,
    score_song,
    recommend_songs,
    get_confidence,
)


def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def make_song_dicts():
    return [
        {
            "id": 1,
            "title": "Test Pop Track",
            "artist": "Test Artist",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "valence": 0.9,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
        {
            "id": 2,
            "title": "Chill Lofi Loop",
            "artist": "Test Artist",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
            "tempo_bpm": 80,
            "valence": 0.6,
            "danceability": 0.5,
            "acousticness": 0.9,
        },
    ]


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_score_song_returns_score_and_reasons():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    song = make_song_dicts()[0]

    score, reasons = score_song(user_prefs, song)

    assert isinstance(score, float)
    assert isinstance(reasons, list)
    assert score > 0
    assert len(reasons) > 0


def test_recommend_songs_returns_top_k_results():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    songs = make_song_dicts()

    results = recommend_songs(user_prefs, songs, k=1)

    assert len(results) == 1
    assert results[0][0]["title"] == "Test Pop Track"


def test_recommend_songs_handles_empty_song_list():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    results = recommend_songs(user_prefs, [], k=5)

    assert results == []


def test_recommend_songs_handles_invalid_k():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    songs = make_song_dicts()

    results = recommend_songs(user_prefs, songs, k=0)

    assert results == []


def test_get_confidence_high():
    assert get_confidence(3.5) == "High"


def test_get_confidence_medium():
    assert get_confidence(2.5) == "Medium"


def test_get_confidence_low():
    assert get_confidence(1.2) == "Low"