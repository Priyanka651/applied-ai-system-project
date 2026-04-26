# 🎧 Model Card: Applied AI Music Recommender System

---

## 1. Model Name

VibeMatch 2.0

---

## 2. Intended Use

This model recommends 3–5 songs based on a user’s preferences such as genre, mood, and energy level.

It is designed for:
- Learning how recommendation systems work
- Demonstrating explainable AI behavior
- Exploring how simple scoring logic can simulate real-world recommendations

It assumes:
- Users have consistent music preferences
- Song features like genre and energy represent a user's "vibe"

This system is intended for educational and demonstration purposes, not for real-world production use.

---

## 3. Non-Intended Use

This model should NOT be used for:
- Real-world music streaming platforms
- Personalized recommendations at scale
- High-stakes decision-making

It does not:
- Understand lyrics or emotional context deeply
- Learn from user behavior over time
- Adapt dynamically to new data

---

## 4. How the Model Works

The recommender system uses a content-based filtering approach.

Each song includes features such as:
- genre
- mood
- energy

The user provides a preference profile:
- preferred genre
- preferred mood
- target energy level

The system assigns a score to each song:
- +2.0 points if genre matches
- +1.0 point if mood matches
- additional score based on how close the song’s energy is to the user’s preference

Songs are then:
- ranked from highest to lowest score
- top recommendations are returned
- each recommendation includes an explanation and confidence level (High, Medium, Low)

---

## 5. Data

The dataset contains 18 songs with various genres and moods including:
- pop, rock, lofi, jazz, classical, electronic, and more

Each song includes:
- energy
- tempo_bpm
- valence
- danceability
- acousticness

Limitations:
- small dataset size
- limited genre diversity
- no lyrics or cultural context included

---

## 6. Strengths

The system works well for users with clear preferences.

Examples:
- High energy pop → energetic songs
- Chill lofi → calm, low-energy tracks

Strengths include:
- simple and transparent logic
- explainable recommendations
- confidence scoring for outputs
- safe handling of invalid inputs (guardrails)

---

## 7. Limitations and Bias

The model has several limitations:

- Strong bias toward genre and energy due to scoring weights
- May repeatedly recommend similar songs (low diversity)
- Struggles with conflicting preferences (e.g., high energy + sad mood)
- Does not consider lyrics, artist popularity, or user history

This can lead to a "filter bubble" effect.

---

## 8. Evaluation

The system was evaluated using multiple test profiles:

- High Energy Pop
- Chill Lofi
- Intense Rock
- Edge Case (High Energy + Sad)

### Observations:
- Works well for clear and consistent preferences
- Produces reasonable recommendations for common cases
- Struggles with conflicting inputs

### Reliability Testing:
- 4 out of 4 profile-based tests passed
- System returned valid recommendations in all cases
- No crashes occurred during invalid input scenarios

### Automated Testing:
- 9 unit tests passed successfully
- Covered scoring, ranking, edge cases, and confidence logic

---

## 9. Guardrails and Safety

The system includes basic guardrails:

- Invalid energy values are corrected (0–1 range)
- Empty genre or mood inputs are replaced with defaults
- Invalid inputs do not crash the system

This ensures stable and safe behavior.

---

## 10. Potential Misuse

This system could be misused if users:
- rely too heavily on automated recommendations
- assume recommendations are complete or unbiased

To reduce misuse:
- the system includes explanations
- limitations are clearly documented

Future improvements could include:
- diversity controls
- randomization to avoid repetition

---

## 11. Future Improvements

If extended further, the system could include:

- larger and more diverse dataset
- additional features like lyrics or user history
- better balance between scoring factors
- diversity-aware recommendation logic
- adaptive or learning-based models

---

## 12. AI Collaboration Reflection

AI tools were used to assist in:
- designing scoring logic
- structuring the recommender system
- generating test cases
- improving code readability

### Helpful AI Suggestion:
AI suggested modularizing scoring and recommendation logic, which made testing easier.

### Flawed AI Suggestion:
Some AI-generated code initially did not handle edge cases (like invalid inputs), which required manual correction.

This shows that AI assistance is helpful but still requires human validation.

---

## 13. Personal Reflection

This project helped me understand how recommendation systems transform structured data into meaningful predictions.

I learned that:
- simple algorithms can produce useful recommendations
- small changes in scoring can significantly affect results
- explainability and testing are critical for trustworthy AI systems

This project changed my perspective on how platforms like Spotify generate recommendations using data-driven logic.