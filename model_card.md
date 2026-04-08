# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.  
**VibeMatch 1.0**

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

This model suggests 5 songs from a catalog of 28 songs based on a user's preferred genre, mood, and energy level. One assumption it makes is that users only listen to the genres listed in the catalog and name mood. It also assumes users only have one music taste. It is for classroom exploration only, not for real users.

---

## 3. How the Model Works

Explain your scoring approach in simple language.

Prompts:

- What features of each song are used (genre, energy, mood, etc.)
- What user preferences are considered
- How does the model turn those into a score
- What changes did you make from the starter logic

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Each song in the catalog has a set of descriptive tags: its genre (like lofi, rock, or pop), its mood (like chill, intense, or sad), an energy level on a scale from 0 to 1, and an acousticness score that measures how much it sounds like live or unplugged instruments rather than electronic production. When a user sets up their profile, they tell the model four things: their favorite genre, their favorite mood, a target energy level, and whether they like acoustic-sounding music. To recommend songs, the system goes through every song in the catalog and gives it a point score based on how well it matches those preferences. A genre match is worth the most with two full points because genre is treated as the strongest signal of taste. A mood match adds one point. The energy level contributes up to one point, where a song with energy exactly matching the target gets the full point, and the score shrinks the further away it is. Finally, if the user likes acoustic music and the song has a high acousticness score, it earns a half-point bonus. Every song gets a total score, and the top five are returned as recommendations. The starter logic provided the basic structure: load songs, score them, return the top results. The main additions were defining exactly how each feature contributes to the score (the specific point values), adding the energy similarity calculation so that closeness matters rather than just a yes/no match, and including the acoustic bonus as an optional reward for users who prefer that sound.

---

## 4. Data

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

There are 28 songs in the catalog. I added more songs because it wasn't a diverse catalog. The catalog contains 28 songs spanning 21 different genres and 14 different moods. The genres include a wide range such as lofi, pop, rock, metal, jazz, classical, hip-hop, EDM, folk, blues, country, reggae, latin, R&B, soul, funk, k-pop, trap, synthwave, ambient, and indie pop. The moods range from happy and chill to sad, intense, melancholic, aggressive, and euphoric, among others.

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

The system works best for users whose preferences closely match what the catalog offers. A lofi listener who enjoys chill, acoustic, low-energy music gets three strong genre matches in their top results, and the acoustic bonus meaningfully separates the best fits from the rest. Similarly, a user whose favorite genre and mood co-occur naturally in the dataset like rock/intense or pop/happy will receive a clear, intuitive #1 recommendation that scores well across all four components at once.

The scoring also handles energy proximity gracefully for most users. Rather than treating energy as a yes/no match, the sliding scale rewards songs that are close even if not exact, which means users rarely get results that feel jarring in tempo or intensity. The explanation string attached to each recommendation is another strength because it tells the user exactly why each song was chosen, which makes the system transparent and easy to reason about.

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users

The most significant limitation is genre dominance. Because a genre match is worth two points out of a maximum of 4.5, it accounts for 44% of the total score on its own. This means a song with the right genre but the wrong mood will almost always outrank a song from a different genre that matches on every other dimension. Users are effectively locked into their genre, and the system discourages discovery across genre lines even when a cross-genre song would feel like a better fit.

The catalog itself introduces bias through unequal representation. Lofi has three songs, pop and a handful of others have two, and most genres have only one. A rock or metal user receives one strong genre match and then sees their recommendations fill with high-energy songs from completely unrelated genres. Lofi users consistently get better results simply because more lofi songs exist.

The acoustic bonus also creates an invisible divide. All twelve songs eligible for the bonus have energy below 0.50, so any user who prefers high-energy music and sets `likes_acoustic: True` will never receive that bonus because their effective maximum score is 4.0 while low-energy users can reach 4.5. The system never flags this conflict.

Finally, the model has no way to penalize bad fits. Setting `likes_acoustic: False` does not push acoustic songs down, it simply withholds the bonus. A user who dislikes acoustic music can still receive folk, classical, and ambient songs ranked highly if their energy happens to be close to the target. There is also no handling for invalid or out-of-range inputs: a target_energy above 1.0 produces negative energy scores that silently corrupt rankings, and genre or mood strings with different capitalization will never match anything in the catalog.

---

## 7. Evaluation

How you checked whether the recommender behaved as expected.

Prompts:

- Which user profiles you tested
- What you looked for in the recommendations
- What surprised you
- Any simple tests or comparisons you ran

No need for numeric metrics unless you created some.

I wrote about 10 user profiles, 3 being users with different music tastes, and 7 cover many edge cases to attempt to find weaknesses. For the standard profiles (chill lofi, high-energy pop, intense rock), the results matched my intuition. Users whose genre and mood existed in the catalog received clearly relevant recommendations, and the top song usually made sense as the best fit.

What surprised me most was how much the genre weight (worth 44% of the max score) dominates results. A lofi song with the wrong mood consistently outranked a non-lofi song with the right mood, which means users are effectively locked into their genre even when better cross-genre matches exist. I also discovered that `likes_acoustic: False` doesn't actually penalize acoustic songs, it just withholds the bonus. So users who dislike acoustic music can still receive folk and classical songs ranked near the top.

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

I definitely want to include a comment for cases when a user profile includes a genre that isn't in a catalog. The comment should let them know there wasn't a genre match for more context on the recommendations they received. Adding input validation is a good idea as well. Having the `target_energy` strictly set up to the 0–1 range would prevent negative energy scores, and normalizing genre and mood strings to lowercase before comparison would eliminate the silent case-sensitivity failures discovered during testing.

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps

Building this recommender made it clear how much design decisions that seem small like assigning genre a weight of 2.0 can have outsized consequences on who the system serves well and who it quietly fails. I'm impressed how accurate it was for the user profiles that had features that were already included in the catalog. Before I starting working on this assignment, I was thinking if we were going to use an AI model to make the recommendations so it was fun seeing how setting up the weights and the calculations of the scores came to life.
