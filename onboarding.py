import streamlit as st

from profile_manager import save_profile

def show_onboarding():
    st.title("🪶 Welcome to Sparrow")

    st.write(
        "Before we analyze your resume, we'd like to know a little about you."
    )

    st.write("Questionnaire coming soon...")

    st.subheader("1. What best describes you?")

    experience_level = st.radio(
        "",
        [
            "Student",
            "Fresher",
            "Working Professional",
            "Career Switcher",
        ],
        key="experience_level",
    )

    st.subheader("2. What's your highest qualification?")

    qualification = st.selectbox(
        "",
        [
            "High School",
            "Diploma",
            "Bachelor's",
            "Master's",
            "PhD",
        ],
        key="qualification",
    )

    st.subheader("3. Which domain are you interested in?")

    domain = st.selectbox(
        "",
        [
            "Artificial Intelligence",
            "Data Science",
            "Software Development",
            "Cyber Security",
            "Cloud Computing",
            "DevOps",
            "UI/UX",
            "Business",
            "Other",
        ],
        key="domain",
    )

    st.subheader("4. How can Sparrow help you?")

    career_goal = st.selectbox(
        "",
        [
            "Resume Review",
            "ATS Improvement",
            "Career Roadmap",
            "Job Recommendations",
            "Interview Preparation",
            "Skill Gap Analysis",
        ],
        key="career_goal",
    )

    if st.button("Continue →"):
        save_profile(
            qualification=qualification,
            experience_level=experience_level,
            domain=domain,
            target_role="",
            career_goal=career_goal,
        )

        st.success("Welcome to Sparrow! 🪶")

        st.rerun()
            