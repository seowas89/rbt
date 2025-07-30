# rbt_practice_exam_app.py
import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="RBT Practice Exam - Master Your Certification",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .header {
        color: #2e86c1;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .subheader {
        color: #138d75;
        border-bottom: 2px solid #f1c40f;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
    }
    .feature-card {
        background-color: #eaf2f8;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .exam-card {
        background-color: #fef9e7;
        border-left: 4px solid #f1c40f;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .btn-primary {
        background-color: #2e86c1 !important;
        color: white !important;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #7f8c8d;
        font-size: 0.9rem;
    }
    .keyword-link {
        color: #2e86c1;
        font-weight: bold;
        text-decoration: none;
    }
    .keyword-link:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'current_exam' not in st.session_state:
    st.session_state.current_exam = None
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

# Sample exam data
EXAMS = {
    "RBT Practice Exam 1": [
        {
            "question": "Which of the following is a primary responsibility of an RBT?",
            "options": [
                "Designing behavior intervention plans",
                "Conducting functional behavior assessments",
                "Implementing behavior intervention plans",
                "Supervising other behavior technicians"
            ],
            "correct": 2,
            "explanation": "RBTs primarily implement behavior intervention plans designed by BCBAs. They don't design plans or supervise others."
        },
        {
            "question": "What is continuous measurement in ABA?",
            "options": [
                "Recording behavior at specific time intervals",
                "Recording every occurrence of behavior",
                "Estimating behavior occurrence",
                "Measuring behavior duration only"
            ],
            "correct": 1,
            "explanation": "Continuous measurement involves recording every instance of a behavior as it occurs."
        }
    ],
    "RBT Practice Exam 2": [
        {
            "question": "When should a behavior intervention plan be modified?",
            "options": [
                "After 6 months regardless of progress",
                "When data shows insufficient progress",
                "Only when requested by parents",
                "Never - plans should be followed exactly"
            ],
            "correct": 1,
            "explanation": "BIPs should be modified based on data analysis showing insufficient progress toward goals."
        }
    ]
}

# Main content
def show_homepage():
    st.markdown(
        '<h1 class="header">'
        '<a href="https://practicerbtexam.com/" class="keyword-link">RBT Practice Exam</a> Mastery'
        '</h1>', 
        unsafe_allow_html=True
    )
    
    st.markdown("""
    <div style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem;">
        <b>Looking for the most effective <a href="https://practicerbtexam.com/" class="keyword-link">RBT practice exam</a> tools to pass your certification with confidence?</b>
        <p>You're in the right place! Our expertly crafted free <a href="https://practicerbtexam.com/" class="keyword-link">RBT practice exams</a> simulate the official test and are designed to help you master every domain of the Registered Behavior Technician exam.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features section
    st.markdown('<h2 class="subheader">Why Our RBT Mock Exam Tools Stand Out</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📝 Realistic Practice</h3>
            <p>Practice with authentic RBT-style questions across multiple mock exams that mirror the actual certification test.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🔍 Detailed Explanations</h3>
            <p>Understand why each answer is correct or incorrect with comprehensive explanations for every question.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ Instant Feedback</h3>
            <p>Identify your strengths and target weak areas for improvement immediately after each exam attempt.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Exams listing
    st.markdown('<h2 class="subheader">Available Practice Exams</h2>', unsafe_allow_html=True)
    
    exams = [
        "RBT Practice Exam 1",
        "RBT Practice Exam 2",
        "RBT Practice Exam 3",
        "RBT Practice Exam 4",
        "RBT Practice Exam Mock Test"
    ]
    
    for exam in exams:
        with st.container():
            st.markdown(f"""
            <div class="exam-card">
                <h3>{exam}</h3>
                <p>Comprehensive test covering all RBT domains: Measurement, Assessment, Skill Acquisition, Behavior Reduction, Documentation, and Professional Conduct.</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Start Exam", key=f"start_{exam}"):
                st.session_state.current_exam = exam
                st.session_state.current_question = 0
                st.session_state.answers = {}
                st.session_state.show_results = False
                st.experimental_rerun()
    
    # Domain coverage
    st.markdown('<h2 class="subheader">Complete RBT Task List Coverage</h2>', unsafe_allow_html=True)
    domains = [
        ("📏 Measurement", "Frequency, duration, latency, interresponse time"),
        ("📊 Assessment", "Data collection methods and interpretation"),
        ("🎯 Skill Acquisition", "Discrete trial teaching, naturalistic teaching"),
        ("📉 Behavior Reduction", "Antecedent interventions, consequence strategies"),
        ("📝 Documentation", "Data recording and reporting"),
        ("👔 Professional Conduct", "Ethical guidelines and client dignity")
    ]
    
    for i in range(0, len(domains), 2):
        cols = st.columns(2)
        for j in range(2):
            if i+j < len(domains):
                with cols[j]:
                    st.markdown(f"""
                    <div style="background: #f8f9f9; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                        <h4>{domains[i+j][0]}</h4>
                        <p>{domains[i+j][1]}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Footer with link
    st.markdown("""
    <div class="footer">
        <p>© 2023 <a href="https://practicerbtexam.com/" class="keyword-link">Practicerbtexam.com</a> | Trusted by thousands of aspiring RBTs</p>
        <p>Comprehensive preparation resources for the Registered Behavior Technician certification exam</p>
    </div>
    """, unsafe_allow_html=True)

# Exam functionality
def take_exam(exam_name):
    questions = EXAMS[exam_name]
    
    if st.session_state.show_results:
        show_results(questions, exam_name)
        return
    
    st.progress((st.session_state.current_question + 1) / len(questions))
    
    q = questions[st.session_state.current_question]
    
    st.subheader(f"Question {st.session_state.current_question + 1} of {len(questions)}")
    st.markdown(f"**{q['question']}**")
    
    selected = st.radio(
        "Select your answer:",
        q['options'],
        index=st.session_state.answers.get(st.session_state.current_question, None),
        key=f"question_{st.session_state.current_question}"
    )
    
    st.session_state.answers[st.session_state.current_question] = q['options'].index(selected)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.session_state.current_question > 0:
            if st.button("Previous Question"):
                st.session_state.current_question -= 1
                st.experimental_rerun()
    
    with col2:
        if st.session_state.current_question < len(questions) - 1:
            if st.button("Next Question"):
                st.session_state.current_question += 1
                st.experimental_rerun()
        else:
            if st.button("Submit Exam"):
                st.session_state.show_results = True
                st.experimental_rerun()

def show_results(questions, exam_name):
    st.subheader(f"{exam_name} Results")
    score = 0
    for i, q in enumerate(questions):
        user_answer = st.session_state.answers.get(i, -1)
        is_correct = user_answer == q['correct']
        
        if is_correct:
            score += 1
        
        st.markdown(f"""
        <div style="border-left: 4px solid {'#2ecc71' if is_correct else '#e74c3c'}; 
                    padding-left: 1rem; margin-bottom: 1.5rem;">
            <p><b>Question {i+1}:</b> {q['question']}</p>
            <p><b>Your answer:</b> {q['options'][user_answer]}</p>
            <p><b>Correct answer:</b> {q['options'][q['correct']]}</p>
            <p><b>Explanation:</b> {q['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    percentage = (score / len(questions)) * 100
    st.success(f"Your score: {score}/{len(questions)} ({percentage:.1f}%)")
    
    if percentage >= 80:
        st.balloons()
        st.markdown("### 🎉 Congratulations! You're ready for the real exam!")
    else:
        st.markdown("### 📚 Keep practicing! Review the explanations and try again.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Take Another Exam"):
            reset_exam()
    with col2:
        if st.button("Back to Home"):
            reset_exam(home=True)

def reset_exam(home=False):
    st.session_state.current_exam = None
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.show_results = False
    if home:
        st.experimental_rerun()

# App routing
def main():
    if st.session_state.current_exam:
        take_exam(st.session_state.current_exam)
    else:
        show_homepage()

if __name__ == "__main__":
    main()
