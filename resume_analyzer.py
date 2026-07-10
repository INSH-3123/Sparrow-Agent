import streamlit as st

from ats_score import calculate_ats_score

from career_readiness import calculate_career_readiness

def analyze_resume(text, detected_domain, career_profile):

    st.subheader("Resume Analysis")

    if "EDUCATION" in text.upper():
        st.success("✅ Education section found.")
    else:
        st.error("❌ Education section Missing.")

    if "SKILLS" in text.upper():
        st.success("✅ Skills section found.")
    else:
        st.error("❌ Skills section Missing.")

    if "PROJECTS" in text.upper():
        st.success("✅ Projects section found.")
    else:
        st.error("❌ Projects section Missing.")
    
    if "EXPERIENCE" in text.upper():
        st.success("✅ Experience section found.")
    else:
        st.error("❌ Experience section Missing.") 


    degree = ""
    if "ARTIFICIAL INTELLIGENCE" in text.upper():
        degree = "AI & Data Science Graduate"
        
    skills_found = []

    if "PYTHON" in text.upper():
        skills_found.append("Python")

    if "JAVA" in text.upper():
        skills_found.append("Java")

    if "SQL" in text.upper():
        skills_found.append("SQL")

    if "REACT" in text.upper():
        skills_found.append("React")

        
    summary = f"""
    🎓 Candidate Profile
        This resume belongs to an {degree}.
        💻 Technical Skills:
        {', '.join(skills_found)}
        
        📂 Resume Highlights:
            • Education Section Present
            • Technical Skills Listed
            • Project Experience Included

        📈 Assessment:
        The candidate demonstrates a solid foundation in software development,
        data technologies, and problem-solving skills. The profile shows
        good academic preparation and practical project exposure."""

    st.info(summary)    

    
    from resume_score import calculate_resume_score

    resume_score, breakdown = calculate_resume_score(text)

    ats_score, ats_breakdown = calculate_ats_score(text)

    career_score, career_breakdown = calculate_career_readiness(
        text,
        resume_score,
        ats_score
    )

    st.subheader("📊 Dashboard Overview")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.metric(
                "📄 Resume Score",
                f"{resume_score}/100"
            )
            st.progress(resume_score / 100)
        
    st.subheader("📄 Resume Score Breakdown")

    MAX_SCORES = {
        "Education": 15,
        "Relevant Skills": 20,
        "Projects": 20,
        "Experience": 20,
        "Certifications": 10,
        "Achievements": 5,
        "Portfolio": 5,
        "GitHub": 5,
        "LinkedIn": 5,
        "Formatting": 5,
    }

    for category, score in breakdown.items():
        max_score = MAX_SCORES.get(category, 0)

        st.write(f"**{category}**")
        st.progress(score / max_score if max_score else 0)
        st.caption(f"{score}/{max_score}")

    
    with col2:
        with st.container(border=True):
            st.metric(
                "ATS Score",
                f"{ats_score}/100"
            )
            st.progress(ats_score / 100)

    st.subheader("📑 ATS Score Breakdown")

    MAX_ATS = {
        "Contact": 10,
        "Headings": 10,
        "Skills": 10,
        "Projects": 10,
        "Experience": 10,
        "Certifications": 10,
        "GitHub": 5,
        "LinkedIn": 5,
        "Readability": 10,
        "Formatting": 10
    }

    for category, score in ats_breakdown.items():
        max_score = MAX_ATS.get(category, 0)

        st.write(f"**{category}**")
        st.progress(score / max_score if max_score else 0)
        st.caption(f"{score}/{max_score}")

    if ats_score >= 80:
        st.success("✅ ATS Friendly Resume")

    elif ats_score >= 60:
        st.warning("⚠️ Moderately ATS Friendly")

    else:
        st.error("❌ ATS Optimization Needed")

    with col3:
        with st.container(border=True):
            st.metric(
                "Career Readiness",
                f"{career_score}%"
            )
            st.progress(career_score / 100)

    st.subheader("🚀 Career Readiness Breakdown")

    MAX_CAREER = {
        "Projects": 20,
        "Experience": 20,
        "GitHub": 10,
        "Portfolio": 10,
        "Certifications": 10,
        "Communication": 10,
        "LinkedIn": 5,
        "Resume Quality": 10,
        "ATS Quality": 5,
    }
    
    for category, score in career_breakdown.items():
        max_score = MAX_CAREER.get(category, 0)

        st.write(f"**{category}**")
        st.progress(score / max_score if max_score else 0)
        st.caption(f"{score}/{max_score}")

    st.divider()


    st.subheader("🎯 Skill Gap Analysis")
    required_skills = [
        "PYTHON",
        "SQL",
        "MACHINE LEARNING",
        "DEEP LEARNING",
        "PANDAS",
        "NUMPY"
    ]
    missing_skills = []

    for skill in required_skills:

        if skill not in text.upper():

            missing_skills.append(skill)

    st.write("Required Role: AI Engineer")
    if len(missing_skills) == 0:

        st.success(
            "✅ No major skill gaps detected."
        )

    else:

        st.warning("Missing Skills Detected")

        skill_info = {
            "PANDAS": "Essential for cleaning and analyzing datasets used in AI projects.",
            "NUMPY": "Required for numerical operations in Machine Learning.",
            "MACHINE LEARNING": "Build predictive models and intelligent applications.",
            "DEEP LEARNING": "Develop neural networks for computer vision and NLP.",
            "SQL": "Manage and retrieve data from databases efficiently.",
            "PYTHON": "The primary programming language used in AI development."
        }

        for skill in missing_skills:
            with st.container(border=True):
                st.markdown(f"### ❌ {skill}")
                st.caption(skill_info.get(skill, "Recommended skill for AI roles."))

    st.subheader("💡 Recommendations")
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.analyzed:

            if st.button("🎯 Skill Recommendations"):

                st.subheader("📚 Learning Recommendations")

                for skill in missing_skills:

                    if skill == "PANDAS":
                        st.success(
                            "📊 Pandas → Learn data cleaning, filtering, grouping and data analysis."
                        )

                    elif skill == "NUMPY":
                        st.success(
                            "🔢 NumPy → Learn arrays, matrices and numerical computations."
                        )

                    elif skill == "MACHINE LEARNING":
                        st.success(
                            "🤖 Machine Learning → Learn Scikit-Learn, model training and evaluation."
                        )

                    elif skill == "DEEP LEARNING":
                        st.success(
                            "🧠 Deep Learning → Learn TensorFlow, PyTorch and neural networks."
                        )

                    else:
                        st.info(f"📖 Learn {skill}")
            

    with col2:
        if st.session_state.analyzed:
            
            if st.button("💼 Job Role Recommendations"):

                roles = []

                if "PYTHON" in text.upper():
                    roles.append("🐍 Python Developer")

                if "SQL" in text.upper():
                    roles.append("📊 Data Analyst")

                if "MACHINE LEARNING" in text.upper():
                    roles.append("🤖 AI Engineer")

                if "DEEP LEARNING" in text.upper():
                    roles.append("🧠 ML Intern")

                for role in roles:
                    st.success(role)   

        st.subheader("📝 Resume Improvement Suggestions")

        if "EXPERIENCE" not in text.upper():
            with st.container(border=True):
                st.markdown("### 💼 Add Experience")
                st.caption(
                    "Internships, freelance work, or real-world projects greatly improve recruiter confidence."
                )

        if "CERTIFICATION" not in text.upper():
            with st.container(border=True):
                st.markdown("### 📜 Add Certifications")
                st.caption(
                    "Industry-relevant certifications enhance your qualifications and demonstrate commitment to learning."
                )

        if "LINKEDIN" not in text.upper():
            with st.container(border=True):
                st.markdown("### 🔗 Add LinkedIn Profile")
                st.caption(
                    "A professional LinkedIn profile increases credibility and recruiter visibility."
                )

        if len(missing_skills) > 0:
            with st.container(border=True):
                st.markdown("### 📚 Learning Roadmap")
                st.caption(
                    f"Recommended next technologies: {', '.join(missing_skills)}"
                )
            st.divider()

            st.info(
                """
            ### 🪶 Sparrow's Overall Assessment

            Your resume demonstrates a solid academic foundation with relevant technical skills.

            **Strengths**
            - Good programming foundation
            - ATS-friendly structure
            - Strong AI/Data Science coursework

            **Next Priority**
            Gain practical experience through projects or internships and continue expanding your ML toolkit.
            """
            ) 

            st.divider()
        return (
            resume_score,
            ats_score,
            career_score,
            missing_skills,
            skills_found
        )
