import streamlit as st
from chatbot import get_response

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Student Assistant | Palak Saxena",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

/* ---------- MAIN PAGE ---------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(76, 100, 180, 0.20), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(30, 120, 180, 0.18), transparent 30%),
        linear-gradient(135deg, #0b1020 0%, #111827 50%, #0b1220 100%);
    color: white;
}

/* Remove extra top spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0d1528 0%,
        #111a30 50%,
        #0b1222 100%
    );
    border-right: 1px solid rgba(255,255,255,0.08);
}

.sidebar-title {
    font-size: 24px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.sidebar-subtitle {
    color: #aab4c8;
    font-size: 13px;
    line-height: 1.6;
}

.sidebar-section {
    margin-top: 28px;
    margin-bottom: 12px;
    font-size: 17px;
    font-weight: 700;
    color: white;
}

.sidebar-item {
    padding: 9px 0;
    color: #d7deea;
    font-size: 14px;
}

.creator-box {
    margin-top: 30px;
    padding: 18px;
    border-radius: 16px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
}

.creator-name {
    font-size: 17px;
    font-weight: 800;
    color: white;
    margin-top: 7px;
}

.creator-role {
    font-size: 12px;
    color: #aab4c8;
    margin-top: 5px;
}

/* ---------- HERO ---------- */

.hero {
    width: 100%;
    padding: 42px 30px;
    border-radius: 24px;
    text-align: center;
    background:
        linear-gradient(
            135deg,
            rgba(79, 70, 229, 0.32),
            rgba(14, 116, 144, 0.30)
        );
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.30),
        inset 0 1px 0 rgba(255,255,255,0.05);
    margin-bottom: 28px;
}

.hero-logo {
    width: 82px;
    height: 82px;
    margin: 0 auto 18px auto;
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 43px;
    background: linear-gradient(135deg, #6366f1, #06b6d4);
    box-shadow: 0 12px 30px rgba(0,0,0,0.30);
}

.hero-title {
    font-size: 42px;
    font-weight: 850;
    letter-spacing: -1px;
    color: white;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 17px;
    color: #c7d2e5;
    margin-bottom: 15px;
}

.creator {
    font-size: 13px;
    color: #aebbd0;
}

/* ---------- FEATURE CARDS ---------- */

.feature-card {
    min-height: 175px;
    padding: 25px 22px;
    border-radius: 20px;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.09);
    box-shadow: 0 12px 30px rgba(0,0,0,0.18);
    transition: 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: rgba(99,102,241,0.55);
}

.feature-icon {
    font-size: 32px;
    margin-bottom: 12px;
}

.feature-title {
    color: white;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 8px;
}

.feature-text {
    color: #aeb9cb;
    font-size: 13px;
    line-height: 1.6;
}

/* ---------- SECTION ---------- */

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: white;
    margin-top: 15px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #aab5c8;
    font-size: 14px;
    margin-bottom: 20px;
}

/* ---------- CONTENT CARDS ---------- */

.content-card {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 18px;
}

.about-card {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    line-height: 1.7;
    color: #c5cfde;
}

/* ---------- ROADMAP ---------- */

.roadmap-card {
    padding: 22px;
    border-radius: 18px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 14px;
}

.roadmap-number {
    font-size: 13px;
    color: #8b9cff;
    font-weight: 700;
}

.roadmap-title {
    font-size: 19px;
    font-weight: 800;
    color: white;
    margin-top: 5px;
}

.roadmap-text {
    color: #adb8ca;
    font-size: 14px;
    margin-top: 7px;
    line-height: 1.6;
}

/* ---------- CHAT ---------- */

.chat-box {
    padding: 18px;
    border-radius: 16px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 12px;
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #7f8ba1;
    font-size: 12px;
    padding-top: 35px;
    padding-bottom: 10px;
}

/* ---------- BUTTONS ---------- */

.stButton > button,
.stLinkButton > a {
    border-radius: 10px !important;
    font-weight: 700 !important;
}

/* ---------- TABS ---------- */

button[data-baseweb="tab"] {
    color: #aeb9cc !important;
    font-weight: 700 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: white !important;
}

/* ---------- MOBILE ---------- */

@media (max-width: 768px) {

    .hero-title {
        font-size: 30px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    .hero {
        padding: 30px 18px;
    }

}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🤖 AI Student Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'Your personal AI-powered learning companion '
        'for BCA and Artificial Intelligence students.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-section">✨ Features</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">🤖 AI Chatbot</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">📚 Study Planner</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">📝 Interactive Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">🎯 Career Roadmap</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div class="creator-box">
            <div style="font-size:25px;">👩‍💻</div>
            <div style="color:#ffffff;font-weight:800;margin-top:5px;">
                Created By
            </div>
            <div class="creator-name">
                Palak Saxena
            </div>
            <div class="creator-role">
                BCA Artificial Intelligence Student
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.link_button(
        "⭐ GitHub Project",
        "https://github.com/palak7002/ai-student-assistant",
        use_container_width=True
    )

    st.link_button(
        "💻 GitHub Profile",
        "https://github.com/palak7002",
        use_container_width=True
    )

    st.write("")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">

    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Chatbot</div>
            <div class="feature-text">
                Ask questions about Python, AI, ML, DSA, SQL,
                internships and projects.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Study Planner</div>
            <div class="feature-text">
                Create a simple personalized study plan
                for your learning goals.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">📝</div>
            <div class="feature-title">Interactive Quiz</div>
            <div class="feature-text">
                Test your knowledge with quick AI and
                programming questions.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Career Roadmap</div>
            <div class="feature-text">
                Explore a practical roadmap for starting
                your technology career.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------

chat_tab, planner_tab, quiz_tab, career_tab, about_tab = st.tabs(
    [
        "🤖 AI Chatbot",
        "📚 Study Planner",
        "📝 Quiz",
        "🎯 Career Roadmap",
        "ℹ️ About"
    ]
)


# =========================================================
# AI CHATBOT
# =========================================================

with chat_tab:

    st.markdown(
        '<div class="section-title">🤖 AI Student Chatbot</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Ask questions and get helpful responses for your studies and career.'
        '</div>',
        unsafe_allow_html=True
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input(
        "Ask me something about AI, Python, DSA, SQL, internships..."
    )

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        with st.chat_message("user"):
            st.write(user_input)

        try:
            response = get_response(user_input)
        except Exception:
            response = (
                "Sorry, I couldn't process that question right now. "
                "Please try asking about Python, AI, ML, DSA, SQL, "
                "internships, projects or BCA."
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            st.write(response)


# =========================================================
# STUDY PLANNER
# =========================================================

with planner_tab:

    st.markdown(
        '<div class="section-title">📚 Personalized Study Planner</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Create a simple daily plan according to your available study time.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        subject = st.selectbox(
            "📖 Select Subject",
            [
                "Python",
                "Data Structures & Algorithms",
                "SQL",
                "Artificial Intelligence",
                "Machine Learning",
                "Web Development",
                "MERN Stack"
            ]
        )

    with col2:

        hours = st.slider(
            "⏰ Daily Study Hours",
            min_value=1,
            max_value=8,
            value=3
        )

    if st.button(
        "✨ Generate Study Plan",
        use_container_width=True
    ):

        st.success(
            f"Study plan created for {subject}!"
        )

        if hours == 1:

            plan = [
                ("Concept Learning", "30 minutes"),
                ("Practice", "20 minutes"),
                ("Revision", "10 minutes")
            ]

        elif hours == 2:

            plan = [
                ("Concept Learning", "60 minutes"),
                ("Practice Questions", "40 minutes"),
                ("Revision", "20 minutes")
            ]

        elif hours == 3:

            plan = [
                ("Concept Learning", "90 minutes"),
                ("Coding / Practice", "60 minutes"),
                ("Revision", "30 minutes")
            ]

        else:

            concept_time = int(hours * 60 * 0.40)
            practice_time = int(hours * 60 * 0.40)
            revision_time = int(hours * 60 * 0.20)

            plan = [
                ("Concept Learning", f"{concept_time} minutes"),
                ("Coding / Practice", f"{practice_time} minutes"),
                ("Revision & Notes", f"{revision_time} minutes")
            ]

        for index, (task, duration) in enumerate(plan, start=1):

            st.markdown(
                f"""
                <div class="roadmap-card">
                    <div class="roadmap-number">
                        STEP {index}
                    </div>

                    <div class="roadmap-title">
                        {task}
                    </div>

                    <div class="roadmap-text">
                        Recommended time: <b>{duration}</b>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# QUIZ
# =========================================================

with quiz_tab:

    st.markdown(
        '<div class="section-title">📝 Interactive Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Test your basic knowledge of programming and artificial intelligence.'
        '</div>',
        unsafe_allow_html=True
    )

    questions = [

        {
            "question": "Which language is commonly used for Artificial Intelligence?",
            "options": ["HTML", "Python", "CSS", "XML"],
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
            "question": "Which data structure follows FIFO?",
            "options": [
                "Stack",
                "Queue",
                "Tree",
                "Graph"
            ],
            "answer": "Queue"
        },

        {
            "question": "Which library is commonly used for machine learning in Python?",
            "options": [
                "Scikit-learn",
                "Django",
                "Flask",
                "BeautifulSoup"
            ],
            "answer": "Scikit-learn"
        },

        {
            "question": "What does AI stand for?",
            "options": [
                "Automated Internet",
                "Artificial Intelligence",
                "Advanced Information",
                "Application Interface"
            ],
            "answer": "Artificial Intelligence"
        }

    ]

    answers = {}

    for i, q in enumerate(questions):

        st.markdown(
            f"### Question {i + 1}"
        )

        st.write(q["question"])

        answers[i] = st.radio(
            "Choose an answer:",
            q["options"],
            key=f"question_{i}"
        )

        st.write("")

    if st.button(
        "✅ Submit Quiz",
        use_container_width=True
    ):

        score = 0

        for i, q in enumerate(questions):

            if answers.get(i) == q["answer"]:
                score += 1

        percentage = int(
            (score / len(questions)) * 100
        )

        st.success(
            f"Your score: {score}/{len(questions)} ({percentage}%)"
        )

        if percentage == 100:

            st.balloons()

            st.info(
                "Excellent! You answered all questions correctly."
            )

        elif percentage >= 60:

            st.info(
                "Good job! Keep practicing to improve further."
            )

        else:

            st.warning(
                "Keep learning and try the quiz again."
            )


# =========================================================
# CAREER ROADMAP
# =========================================================

with career_tab:

    st.markdown(
        '<div class="section-title">🎯 AI & Technology Career Roadmap</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A beginner-friendly path for BCA and AI students.'
        '</div>',
        unsafe_allow_html=True
    )

    roadmap = [

        (
            "01",
            "Programming Fundamentals",
            "Learn Python, variables, loops, functions, OOP and basic problem solving."
        ),

        (
            "02",
            "Data Structures & Algorithms",
            "Study arrays, strings, linked lists, stacks, queues, trees, graphs and sorting."
        ),

        (
            "03",
            "Database & SQL",
            "Learn SQL queries, joins, filtering, grouping, subqueries and database concepts."
        ),

        (
            "04",
            "Artificial Intelligence",
            "Understand AI fundamentals, search techniques, intelligent systems and applications."
        ),

        (
            "05",
            "Machine Learning",
            "Learn supervised and unsupervised learning, model evaluation and basic ML projects."
        ),

        (
            "06",
            "Projects",
            "Build practical projects and publish them on GitHub to demonstrate your skills."
        ),

        (
            "07",
            "Internships",
            "Create an ATS-friendly resume, portfolio and apply for relevant internship opportunities."
        ),

        (
            "08",
            "Career Preparation",
            "Practice coding questions, technical interviews, communication and project explanations."
        )

    ]

    for number, title, description in roadmap:

        st.markdown(
            f"""
            <div class="roadmap-card">

                <div class="roadmap-number">
                    ROADMAP {number}
                </div>

                <div class="roadmap-title">
                    {title}
                </div>

                <div class="roadmap-text">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# ABOUT
# =========================================================

with about_tab:

    st.markdown(
        '<div class="section-title">ℹ️ About This Project</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Learn more about the AI Student Assistant.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="about-card">

        <h2 style="color:white;">🤖 AI Student Assistant</h2>

        <p>
        AI Student Assistant is a student-focused learning application
        designed to help BCA and Artificial Intelligence students
        learn technical subjects, practice concepts and plan their
        career journey.
        </p>

        <p>
        The application combines an AI-style chatbot with study
        planning, interactive quizzes and a technology career roadmap
        in one simple interface.
        </p>

        <h3 style="color:white;">🚀 Key Features</h3>

        <ul>
            <li>AI-powered student chatbot</li>
            <li>Personalized study planner</li>
            <li>Interactive programming quiz</li>
            <li>AI and technology career roadmap</li>
            <li>Professional responsive interface</li>
            <li>GitHub project integration</li>
        </ul>

        <h3 style="color:white;">🛠️ Technologies Used</h3>

        <ul>
            <li>Python</li>
            <li>Streamlit</li>
            <li>Scikit-learn</li>
            <li>Natural Language Processing</li>
            <li>TF-IDF</li>
            <li>Cosine Similarity</li>
            <li>JSON</li>
        </ul>

        <h3 style="color:white;">👩‍💻 Developer</h3>

        <p>
        <b style="color:white;">Palak Saxena</b><br>
        BCA Artificial Intelligence Student<br>
        Expected Graduation: 2028
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "⭐ View GitHub Project",
            "https://github.com/palak7002/ai-student-assistant",
            use_container_width=True
        )

    with col2:

        st.link_button(
            "💻 Visit GitHub Profile",
            "https://github.com/palak7002",
            use_container_width=True
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Built with ❤️ using Python, NLP & Streamlit
        <br>
        © 2026 Palak Saxena • AI Student Assistant
    </div>
    """,
    unsafe_allow_html=True
)
