# 🤖 AI Student Assistant

An AI-powered student assistant chatbot built using Python, Natural Language Processing and Streamlit.

## 🚀 Features

- 🤖 AI Student Chatbot
- 🧠 NLP-based question matching
- 📚 Study Planner
- 📝 Programming and AI Quiz
- 🎯 BCA AI Career Roadmap
- 💼 Internship guidance
- 🚀 AI project recommendations
- 💬 Interactive chat interface
- 📊 Quiz score tracking

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Cosine Similarity
- JSON
- Natural Language Processing

## 🧠 How It Works

The chatbot uses TF-IDF vectorization to convert questions into numerical representations.

Cosine similarity is then used to compare the user's question with the stored questions in the chatbot knowledge base.

The closest matching question is selected and the corresponding response is returned.

## 📂 Project Structure

```text
ai-student-assistant/
│
├── data/
│   └── intents.json
│
├── app.py
├── chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
