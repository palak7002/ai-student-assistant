import streamlit as st
from chatbot import get_response


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Student Assistant | Palak Saxena",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.10), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(14,165,233,0.08), transparent 25%),
        linear-gradient(135deg, #0f172a 0%, #111827 50%, #0f172a 100%);
}

/* Header */
.hero {
    padding: 30px 35px;
    border-radius: 24px;
    margin-bottom: 25px;
    background: linear-gradient(
        135deg,
        rgba(99,102,241,0.22),
        rgba(14,165,233,0.12)
    );
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 15px 40px rgba(0,0,0,0.20);
}

.hero-logo {
    width: 65px;
    height: 65px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
    background: linear-gradient(135deg, #6366f1, #06b6d4);
    box-shadow: 0 10px 25px rgba(99,102,241,0.35);
    margin-bottom: 15px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 17px;
    opacity: 0.75;
    margin-bottom: 15px;
}

.creator {
    font-size: 14px;
    opacity: 0.70;
}

/* Cards */
.feature-card {
    padding: 22px;
    min-height: 145px;
    border-radius: 18px;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.10);
    transition: 0.25s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    border-color: rgba(99,102,241,0.45);
    background: rgba(255,255,255,0.08);
}

.feature-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.feature-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 7px;
}

.feature-text {
    font-size: 14px;
    opacity: 0.70;
}

/* Section headings */
.section-title {
    font-size: 27px;
    font-weight: 750;
    margin-top: 15px;
    margin-bottom: 8px;
}

.section-subtitle {
    opacity: 0.68;
    margin-bottom: 20px;
}

/* About */
.about-card {
    padding: 28px;
    border-radius: 20px;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.10);
    line-height: 1.7;
}

/* Roadmap */
.roadmap-card {
    padding: 20px;
    border-radius: 17px;
    margin-bottom: 12px;
    background: rgba(255,255,255,0.045);
    border-left: 4px solid #6366f1;
}

/* Footer */
.footer {
    text-align: center;
    padding: 25px 10px 10px;
    margin-top: 40px;
    opacity: 0.55;
    font-size: 13px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.96);
    border-right: 1px solid rgba(255,255,255,0.08);
}

.sidebar-title {
    font-size: 23px;
    font-weight: 800;
}

.sidebar-text {
    font-size: 13px;
    opacity: 0.65;
    line-height: 1.6;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    font-weight: 600;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 10px 18px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_question" not in st.session_state:
    st.session_state.quiz_question = 0


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🤖 AI Student Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">'
        'Your personal AI-powered learning companion for '
        'BCA and Artificial Intelligence students.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### ✨ Features")

    st.markdown("🤖 **AI Chatbot**")
    st.markdown("📚 **Study Planner**")
    st.markdown("📝 **Interactive Quiz**")
    st.markdown("🎯 **Career Roadmap**")

    st.divider()

    st.markdown("### 👩‍💻 Created By")

    st.markdown("**Palak Saxena**")
    st.caption("BCA Artificial Intelligence Student")

    st.divider()

    st.link_button(
        "🐙 View GitHub Project",
        "https://github.com/palak7002/ai-student-assistant",
        use_container_width=True
    )

    if st.button(
        "🧹 Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# =========================================================
# HERO HEADER
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-logo">
        🤖
    </div>

    <div class="hero-title">
        AI Student Assistant
    </div>

    <div class="hero-subtitle">
        Learn smarter • Practice better • Plan your career
    </div>

    <div class="creator">
        Built with Python, NLP, Scikit-learn & Streamlit
        &nbsp;•&nbsp; Created by <b>Palak Saxena</b>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FEATURE CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Chatbot</div>
        <div class="feature-text">
            Ask questions about Python, AI, ML, DSA, SQL and more.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">Study Planner</div>
        <div class="feature-text">
            Create a simple study plan based on your subjects and time.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <div class="feature-title">Quiz</div>
        <div class="feature-text">
            Test your knowledge with beginner-friendly questions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Career Roadmap</div>
        <div class="feature-text">
            Follow a structured path from programming to internships.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.write("")


# =========================================================
# TABS
# =========================================================

chat_tab, planner_tab, quiz_tab, career_tab, about_tab = st.tabs([
    "🤖 AI Chatbot",
    "📚 Study Planner",
    "📝 Quiz",
    "🎯 Career Roadmap",
    "ℹ️ About"
])


# =========================================================
# TAB 1 — AI CHATBOT
# =========================================================

with chat_tab:

    st.markdown(
        '<div class="section-title">💬 Ask your AI Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Get help with programming, AI, Machine Learning, DSA, SQL, '
        'internships and student projects.'
        '</div>',
        unsafe_allow_html=True
    )

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"],
            avatar="👤" if message["role"] == "user" else "🤖"
        ):
            st.markdown(message["content"])

    user_input = st.chat_input(
        "Ask something like: What is Python?"
    )

    if user_input:

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message(
            "user",
            avatar="👤"
        ):
            st.markdown(user_input)

        response = get_response(user_input)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):
            st.markdown(response)


# =========================================================
# TAB 2 — STUDY PLANNER
# =========================================================

with planner_tab:

    st.markdown(
        '<div class="section-title">📚 Smart Study Planner</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Create a simple daily study plan according to your subjects and available time.'
        '</div>',
        unsafe_allow_html=True
    )

    subjects = st.text_input(
        "Subjects",
        placeholder="Example: Python, SQL, DSA, AI"
    )

    col1, col2 = st.columns(2)

    with col1:
        hours = st.number_input(
            "Study hours per day",
            min_value=1,
            max_value=12,
            value=3
        )

    with col2:
        exam_days = st.number_input(
            "Days until exam",
            min_value=1,
            max_value=365,
            value=30
        )

    if st.button(
        "📅 Generate Study Plan",
        use_container_width=True
    ):

        if subjects.strip() == "":
            st.warning("Please enter at least one subject.")

        else:

            subject_list = [
                subject.strip()
                for subject in subjects.split(",")
                if subject.strip()
            ]

            st.success(
                f"Study plan created for {len(subject_list)} subjects!"
            )

            st.info(
                f"You have approximately **{exam_days} days** before your exam."
            )

            time_per_subject = hours / len(subject_list)

            for index, subject in enumerate(
                subject_list,
                start=1
            ):

                st.markdown(
                    f"""
                    <div class="roadmap-card">
                        <h3>{index}. {subject}</h3>
                        <p>⏱️ Suggested time:
                        <b>{time_per_subject:.1f} hours</b></p>
                        <p>📖 Learn → Practice → Revise</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.success(
                "💡 Tip: Keep the final 20–25% of your study time for revision."
            )


# =========================================================
# TAB 3 — QUIZ
# =========================================================

with quiz_tab:

    st.markdown(
        '<div class="section-title">📝 Test Your Knowledge</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Test your understanding of AI and programming fundamentals.'
        '</div>',
        unsafe_allow_html=True
    )

    quiz_questions = [

        {
            "question": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automated Internet",
                "Advanced Internet",
                "Application Interface"
            ],
            "answer": "Artificial Intelligence"
        },

        {
            "question": "Which language is widely used in AI and Machine Learning?",
            "options": [
                "Python",
                "HTML",
                "CSS",
                "XML"
            ],
            "answer": "Python"
        },

        {
            "question": "What does SQL stand for?",
            "options": [
                "Structured Query Language",
                "Simple Question Language",
                "System Query Logic",
                "Structured Question List"
            ],
            "answer": "Structured Query Language"
        },

        {
            "question": "What does DSA stand for?",
            "options": [
                "Data Structures and Algorithms",
                "Data System Application",
                "Digital Structure Analysis",
                "Database Search Algorithm"
            ],
            "answer": "Data Structures and Algorithms"
        },

        {
            "question": "Which library is commonly used for machine learning in Python?",
            "options": [
                "Scikit-learn",
                "Tkinter",
                "BeautifulSoup",
                "Pygame"
            ],
            "answer": "Scikit-learn"
        }

    ]

    if st.button("🔄 Restart Quiz"):

        st.session_state.quiz_score = 0
        st.session_state.quiz_question = 0
        st.rerun()

    question_index = st.session_state.quiz_question

    if question_index >= len(quiz_questions):

        st.success("🎉 Quiz Completed!")

        st.metric(
            "Your Score",
            f"{st.session_state.quiz_score} / {len(quiz_questions)}"
        )

        percentage = (
            st.session_state.quiz_score
            / len(quiz_questions)
        ) * 100

        st.progress(int(percentage))

        if percentage >= 80:
            st.balloons()
            st.success("Excellent work! Keep practicing.")

        elif percentage >= 50:
            st.info(
                "Good attempt. Revise the topics you found difficult."
            )

        else:
            st.warning(
                "Keep learning and try the quiz again!"
            )

    else:

        current_question = quiz_questions[question_index]

        st.markdown(
            f"### Question {question_index + 1} of {len(quiz_questions)}"
        )

        st.progress(
            question_index / len(quiz_questions)
        )

        st.write(current_question["question"])

        selected_answer = st.radio(
            "Choose your answer:",
            current_question["options"],
            key=f"question_{question_index}"
        )

        if st.button(
            "Submit Answer",
            use_container_width=True
        ):

            if selected_answer == current_question["answer"]:

                st.success("✅ Correct!")

                st.session_state.quiz_score += 1

            else:

                st.error(
                    "❌ Incorrect. "
                    f"Correct answer: {current_question['answer']}"
                )

            st.session_state.quiz_question += 1
            st.rerun()


# =========================================================
# TAB 4 — CAREER ROADMAP
# =========================================================

with career_tab:

    st.markdown(
        '<div class="section-title">🎯 BCA AI Career Roadmap</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A structured learning path for students interested in AI and technology.'
        '</div>',
        unsafe_allow_html=True
    )

    roadmap = [

        (
            "1️⃣ Programming",
            "Learn Python fundamentals, functions, OOP and problem solving."
        ),

        (
            "2️⃣ DSA",
            "Learn arrays, strings, linked lists, stacks, queues, trees and searching."
        ),

        (
            "3️⃣ SQL",
            "Learn databases, SELECT, JOIN, GROUP BY, subqueries and database basics."
        ),

        (
            "4️⃣ Data Analysis",
            "Learn NumPy, Pandas, Matplotlib and exploratory data analysis."
        ),

        (
            "5️⃣ Machine Learning",
            "Learn regression, classification, clustering and model evaluation."
        ),

        (
            "6️⃣ Projects",
            "Build 2–4 practical projects and document them on GitHub."
        ),

        (
            "7️⃣ Resume",
            "Create an ATS-friendly resume with skills, projects and certificates."
        ),

        (
            "8️⃣ Internship",
            "Apply regularly and prepare to explain your projects clearly."
        )

    ]

    for title, description in roadmap:

        st.markdown(
            f"""
            <div class="roadmap-card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# TAB 5 — ABOUT
# =========================================================

with about_tab:

    st.markdown(
        '<div class="section-title">ℹ️ About This Project</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="about-card">

    <h2>🤖 AI Student Assistant</h2>

    <p>
    AI Student Assistant is an AI-powered learning companion designed
    for students who are learning programming, Artificial Intelligence
    and technology.
    </p>

    <p>
    The application uses <b>Python, Natural Language Processing,
    TF-IDF, Cosine Similarity, Scikit-learn and Streamlit</b>
    to understand student questions and provide relevant responses.
    </p>

    <h3>✨ What can it do?</h3>

    <p>
    • Answer student questions<br>
    • Help with Python, AI, ML, DSA and SQL<br>
    • Generate a simple study plan<br>
    • Test programming and AI knowledge<br>
    • Provide a BCA AI career roadmap
    </p>

    <h3>🛠️ Technologies</h3>

    <p>
    Python • NLP • Scikit-learn • TF-IDF • Cosine Similarity •
    JSON • Streamlit
    </p>

    <h3>👩‍💻 Developer</h3>

    <p>
    <b>Palak Saxena</b><br>
    BCA Artificial Intelligence Student
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "🐙 View GitHub Repository",
            "https://github.com/palak7002/ai-student-assistant",
            use_container_width=True
        )

    with col2:
        st.link_button(
            "💻 View My GitHub Profile",
            "https://github.com/palak7002",
            use_container_width=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Built with ❤️ using Python & Streamlit
    <br>
    © 2026 Palak Saxena • AI Student Assistant
</div>
""", unsafe_allow_html=True)
