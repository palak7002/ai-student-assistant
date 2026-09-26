import json
import random
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# LOAD INTENTS
# ==========================================

with open("data/intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)


# ==========================================
# PREPARE TRAINING QUESTIONS
# ==========================================

patterns = []
tags = []

for intent in data["intents"]:

    if intent["tag"] == "unknown":
        continue

    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])


# ==========================================
# TF-IDF NLP MODEL
# ==========================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    sublinear_tf=True
)

pattern_vectors = vectorizer.fit_transform(patterns)


# ==========================================
# CLEAN USER TEXT
# ==========================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


# ==========================================
# FIND BEST INTENT
# ==========================================

def find_best_intent(user_message):

    cleaned_message = clean_text(user_message)

    user_vector = vectorizer.transform(
        [cleaned_message]
    )

    similarities = cosine_similarity(
        user_vector,
        pattern_vectors
    )[0]

    best_index = similarities.argmax()

    best_score = similarities[best_index]

    predicted_tag = tags[best_index]

    matched_question = patterns[best_index]

    return predicted_tag, best_score, matched_question


# ==========================================
# SPECIAL STUDENT FEATURES
# ==========================================

def special_response(message):

    text = clean_text(message)


    # Study plan
    if (
        "study plan" in text
        or "study schedule" in text
        or "how should i study" in text
    ):

        return """
### 📚 Simple BCA AI Study Plan

**Daily — 2 to 3 hours**

🐍 **45 min — Python**
Practice coding and problem solving.

🗄️ **30 min — SQL**
Practice queries and databases.

📊 **45 min — DSA**
Arrays, strings, linked lists and searching.

🧠 **30 min — AI/ML**
Learn concepts and build small projects.

🚀 **30 min — Project**
Work on one practical project.

**Rule:** Learn → Practice → Build → Revise.
"""


    # Internship
    if (
        "internship roadmap" in text
        or "prepare for internship" in text
        or "internship preparation" in text
    ):

        return """
### 💼 Internship Preparation Roadmap

**Step 1:** Learn Python

**Step 2:** Learn SQL

**Step 3:** Learn DSA basics

**Step 4:** Learn basic Machine Learning

**Step 5:** Build 2–3 projects

**Step 6:** Create a GitHub profile

**Step 7:** Create an ATS-friendly resume

**Step 8:** Apply regularly

For an AI student, projects are especially useful because they give you something concrete to discuss during interviews.
"""


    # Project ideas
    if (
        "project ideas" in text
        or "project idea" in text
        or "projects should i make" in text
    ):

        return """
### 🚀 AI Project Ideas

**Beginner**
1. 🤖 AI Student Chatbot
2. 📊 Student Performance Predictor
3. 😊 Sentiment Analysis
4. 🎬 Movie Recommendation System

**Intermediate**
5. 🏠 House Price Prediction
6. 📈 Sales Prediction
7. 📄 Resume Analyzer
8. 📰 Fake News Detection

**Advanced**
9. 🧠 AI Study Assistant
10. 🔍 Image Classification System

Start with one project and make it complete rather than creating many unfinished projects.
"""


    return None


# ==========================================
# MAIN CHATBOT FUNCTION
# ==========================================

def get_response(user_message):

    # Check special features first
    special = special_response(user_message)

    if special:
        return special


    # Find best matching intent
    predicted_tag, score, matched_question = find_best_intent(
        user_message
    )


    # Very low confidence
    if score < 0.20:

        return """
I'm not completely sure what you mean. 🤔

Try asking me about:

🐍 Python  
🧠 AI  
🤖 Machine Learning  
📊 DSA  
🗄️ SQL  
💼 Internships  
🚀 Projects  
📚 Study plans

For example:

**"How should I study DSA?"**
"""


    # Find matching intent
    for intent in data["intents"]:

        if intent["tag"] == predicted_tag:

            return random.choice(
                intent["responses"]
            )


    return "I'm still learning. Try asking me about your studies!"