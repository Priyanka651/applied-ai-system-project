from src.recommender import load_songs, recommend_songs


def get_user_input():
    print("\n🎧 Enter your music preferences:")

    genre = input("Enter genre (e.g., pop, rock, lofi): ").strip().lower()
    if not genre:
        print("⚠️ Genre was empty. Using default genre: pop")
        genre = "pop"

    mood = input("Enter mood (e.g., happy, chill, sad): ").strip().lower()
    if not mood:
        print("⚠️ Mood was empty. Using default mood: happy")
        mood = "happy"

    try:
        energy = float(input("Enter energy (0 to 1): "))
    except ValueError:
        print("❌ Invalid energy input. Using default value 0.5")
        energy = 0.5

    if energy < 0 or energy > 1:
        print("⚠️ Energy must be between 0 and 1. Setting to 0.5")
        energy = 0.5

    return {"genre": genre, "mood": mood, "energy": energy}


def run_reliability_tests(songs) -> None:
    print("\n==============================")
    print("Reliability Testing")
    print("==============================\n")

    test_profiles = {
        "Test 1 - High Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Test 2 - Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3},
        "Test 3 - Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
        "Test 4 - Edge Case": {"genre": "pop", "mood": "sad", "energy": 0.95},
    }

    passed = 0
    total = len(test_profiles)

    for test_name, profile in test_profiles.items():
        try:
            results = recommend_songs(profile, songs, k=3)

            if not results:
                print(f"{test_name}: FAIL - No recommendations returned")
                continue

            top_song, top_score, top_explanation, top_confidence = results[0]

            if not top_explanation.strip():
                print(f"{test_name}: FAIL - Missing explanation")
                continue

            print(f"{test_name}: PASS")
            passed += 1

        except Exception as e:
            print(f"{test_name}: FAIL - Error: {e}")

    print(f"\nReliability Summary: {passed} out of {total} tests passed.\n")


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = get_user_input()

    print("\n==============================")
    print("Your Recommendations")
    print("==============================\n")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    if not recommendations:
        print("No recommendations available.")
        return

    for song, score, explanation, confidence in recommendations:
        print(f"{song['title']} - Score: {score:.2f} - Confidence: {confidence}")
        print(f"Because: {explanation}")
        print()

    run_reliability_tests(songs)


if __name__ == "__main__":
    main()