import streamlit as st
from chatbot import get_response


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Student Assistant",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    font-size: 18px;
    opacity: 0.75;
    margin-bottom: 25px;
}

.card {
    padding: 22px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.25);
    background: rgba(128,128,128,0.08);
    margin-bottom: 15px;
}

.card h3 {
    margin-top: 0;
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

    st.title("🤖 AI Student Assistant")

    st.write(
        "Your personal learning companion for "
        "BCA and Artificial Intelligence."
    )

    st.divider()

    st.markdown("### 📌 Features")

    st.write("🤖 AI Chatbot")
    st.write("📚 Study Planner")
    st.write("📝 AI/Programming Quiz")
    st.write("🎯 Career Roadmap")

    st.divider()

    if st.button(
        "🧹 Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 AI Student Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Learn • Practice • Plan • Build'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# TABS
# =========================================================

chat_tab, planner_tab, quiz_tab, career_tab = st.tabs([
    "🤖 AI Chatbot",
    "📚 Study Planner",
    "📝 Quiz",
    "🎯 Career Roadmap"
])


# =========================================================
# TAB 1 — AI CHATBOT
# =========================================================

with chat_tab:

    st.subheader("💬 Ask your AI Student Assistant")

    st.write(
        "Ask questions about Python, AI, Machine Learning, "
        "DSA, SQL, internships or projects."
    )


    # Display previous messages

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"],
            avatar="👤" if message["role"] == "user" else "🤖"
        ):

            st.markdown(message["content"])


    # Chat input

    user_input = st.chat_input(
        "Ask your question..."
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

    st.subheader("📚 Create Your Study Plan")

    st.write(
        "Enter your subjects and available study time "
        "to create a simple daily study plan."
    )


    subjects = st.text_input(
        "Subjects",
        placeholder="Example: Python, SQL, DSA, AI"
    )


    hours = st.number_input(
        "Available study hours per day",
        min_value=1,
        max_value=12,
        value=3
    )


    exam_days = st.number_input(
        "Days until your exam",
        min_value=1,
        max_value=365,
        value=30
    )


    if st.button(
        "📅 Generate Study Plan",
        use_container_width=True
    ):

        if subjects.strip() == "":

            st.warning(
                "Please enter at least one subject."
            )

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
                f"You have approximately "
                f"**{exam_days} days** before your exam."
            )


            time_per_subject = hours / len(subject_list)


            for index, subject in enumerate(
                subject_list,
                start=1
            ):

                st.markdown(
                    f"""
                    <div class="card">

                    <h3>{index}. {subject}</h3>

                    <p>
                    ⏱️ Suggested time:
                    <b>{time_per_subject:.1f} hours</b>
                    </p>

                    <p>
                    📖 Learn → Practice → Revise
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            st.success(
                "💡 Tip: Keep the final 20–25% of your "
                "study time for revision and practice."
            )


# =========================================================
# TAB 3 — QUIZ
# =========================================================

with quiz_tab:

    st.subheader("📝 Test Your Knowledge")

    st.write(
        "Answer these beginner-level AI and programming questions."
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


    # Reset quiz button

    if st.button("🔄 Restart Quiz"):

        st.session_state.quiz_score = 0

        st.session_state.quiz_question = 0

        st.rerun()


    question_index = st.session_state.quiz_question


    # Quiz completed

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


        st.progress(
            int(percentage)
        )


        if percentage >= 80:

            st.balloons()

            st.success(
                "Excellent work! Keep practicing."
            )

        elif percentage >= 50:

            st.info(
                "Good attempt. Revise the topics "
                "you found difficult."
            )

        else:

            st.warning(
                "Keep learning and try the quiz again!"
            )


    else:

        current_question = quiz_questions[
            question_index
        ]


        st.markdown(
            f"### Question {question_index + 1} "
            f"of {len(quiz_questions)}"
        )


        st.write(
            current_question["question"]
        )


        selected_answer = st.radio(
            "Choose your answer:",
            current_question["options"],
            key=f"question_{question_index}"
        )


        if st.button(
            "Submit Answer",
            use_container_width=True
        ):

            if (
                selected_answer
                == current_question["answer"]
            ):

                st.success("✅ Correct!")

                st.session_state.quiz_score += 1

            else:

                st.error(
                    "❌ Incorrect. "
                    f"Correct answer: "
                    f"{current_question['answer']}"
                )


            st.session_state.quiz_question += 1

            st.rerun()


# =========================================================
# TAB 4 — CAREER ROADMAP
# =========================================================

with career_tab:

    st.subheader("🎯 BCA AI Career Roadmap")

    st.write(
        "A simple learning path for a student "
        "interested in AI and technology."
    )


    roadmap = [

        (
            "1️⃣ Programming",
            "Learn Python fundamentals, functions, "
            "OOP and problem solving."
        ),

        (
            "2️⃣ DSA",
            "Learn arrays, strings, linked lists, "
            "stacks, queues, trees and searching."
        ),

        (
            "3️⃣ SQL",
            "Learn databases, SELECT, JOIN, GROUP BY, "
            "subqueries and basic database design."
        ),

        (
            "4️⃣ Data Analysis",
            "Learn NumPy, Pandas, Matplotlib "
            "and exploratory data analysis."
        ),

        (
            "5️⃣ Machine Learning",
            "Learn regression, classification, "
            "clustering and model evaluation."
        ),

        (
            "6️⃣ Projects",
            "Build 2–4 projects and upload them "
            "to GitHub with proper documentation."
        ),

        (
            "7️⃣ Resume",
            "Create an ATS-friendly resume with "
            "skills, projects and certificates."
        ),

        (
            "8️⃣ Internship",
            "Apply regularly and prepare to "
            "explain your projects clearly."
        )

    ]


    for title, description in roadmap:

        st.markdown(
            f"""
            <div class="card">

            <h3>{title}</h3>

            <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )