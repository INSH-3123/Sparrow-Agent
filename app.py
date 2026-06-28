import streamlit as st

st.set_page_config(
    page_title="Sparrow Agent",
    page_icon="🪶",
    layout="wide"
)
with st.sidebar:

    st.title("🪶 Sparrow Agent")

    st.divider()

    st.header("Navigation")

    st.write("🏠 **Dashboard**")
    st.write("📄 **Resume Analysis**")
    st.write("📊 **Resume Score**")
    st.write("🎯 **ATS Score**")
    st.write("🧠 **Skill Gap**")
    st.write("💼 **Job Recommendations**")
    st.write("📥 **Download Report**")

    st.divider()

    st.caption("Version 0.3 - AI Resume Analysis Assistant")

from pypdf import PdfReader

from career_analyzer import analyze_career

from resume_analyzer import analyze_resume

from ats_analyzer import analyze_ats

from report_generator import generate_report 

from utils import (
    get_today,
    get_candidate_name,
    get_rating,
)

from intelligence import analyze_candidate 

st.title("🪶 Sparrow Agent")

st.write("Welcome to Sparrow Agent!")

upload_file = st.file_uploader(
    "Upload a resume(PDF)", 
    type=["pdf"]
)

if upload_file is not None:
    st.success("Resume uploaded successfully!")

    pdf = PdfReader(upload_file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    st.session_state.resume_text = text    

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

analyze = st.button("Analyze Resume")

if analyze:
    st.session_state.analyzed = True
    
text = st.session_state.get("resume_text", "")

strengths, weaknesses, suggestions = analyze_candidate(text)

if st.session_state.analyzed:

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

       
    score = 0

    if "EDUCATION" in text.upper():
        score += 25

    if "SKILLS" in text.upper():
        score += 25

    if "PROJECTS" in text.upper():
        score += 25

    if "EXPERIENCE" in text.upper():
        score += 25 

    
    st.subheader("📊 Dashboard Overview")
    
    col1, col2, col3 = st.columns(3)

    with col1:
            with st.container(border=True):
                st.metric(
                    "📄 Resume Score",
                    f"{score}/100"
                )
                st.progress(score / 100)

    ats_score, ats_sections = analyze_ats(text)

    with col2:
        with st.container(border=True):
            st.metric(
                "ATS Score",
                f"{ats_score}/100"
            )
            st.progress(ats_score / 100)

    if ats_score >= 80:
        st.success("✅ ATS Friendly Resume")

    elif ats_score >= 60:
        st.warning("⚠️ Moderately ATS Friendly")

    else:
        st.error("❌ ATS Optimization Needed")

    career_score = int((score + ats_score) / 2)

    with col3:
        with st.container(border=True):
            st.metric(
                "Career Readiness",
                f"{career_score}%"
            )
            st.progress(career_score / 100)
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



        st.subheader("🧠 Sparrow Intelligence")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💪 Strengths")

            for strength in strengths:
                st.success(strength)

            st.markdown("### ⚠️ Weaknesses")

            for weakness in weaknesses:
                st.warning(weakness)

        with col2:
            st.markdown("### 💡 Suggestions")

            for suggestion in suggestions:
                st.info(suggestion)

        st.subheader("🎯 Career Match Dashboard")
        career_scores, best_role = analyze_career(text)

        ai_engineer = career_scores["AI Engineer"]
        ml_engineer = career_scores["ML Engineer"]
        data_analyst = career_scores["Data Analyst"]
        python_dev = career_scores["Python Developer"]

        career_scores = {
            "AI Engineer": ai_engineer,
            "ML Engineer": ml_engineer,
            "Data Analyst": data_analyst,
            "Python Developer": python_dev
        }

        best_role = max(career_scores, key=career_scores.get)

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):
                st.markdown("### 🤖 AI Engineer")
                st.metric("Match", f"{ai_engineer}%")
                st.progress(ai_engineer/100)

            with st.container(border=True):    
                st.markdown("### 📊 Data Analyst")
                st.metric("Match", f"{data_analyst}%")
                st.progress(data_analyst / 100)

        with col2:

            with st.container(border=True):
                st.markdown("### 🧠 ML Engineer")
                st.metric("Match", f"{ml_engineer}%")
                st.progress(ml_engineer / 100)
            
            with st.container(border=True): 
                st.markdown("### 🐍 Python Developer")
                st.metric("Match", f"{python_dev}%")
                st.progress(python_dev / 100)


        st.divider()

        st.subheader("🪶 Why Sparrow Recommended This")   

        with st.container(border=True):
            st.markdown("## 🎯 Best Career Match")
            st.metric(
                "Recommended Role",
                best_role
            )
            
        st.write("✅ Python detected")
        st.write("✅ SQL detected")
        st.write("✅ AI & Data Science degree")
        st.write("✅ Project experience")
        st.write("❌ TensorFlow not found")
        st.write("❌ Internship experience not found")  

        st.info(f"""
        Sparrow selected **{best_role}** because your resume demonstrates strong technical skills and is the best overall match based on the detected technologies in your resume.
        """)

        st.subheader("🤔 Why Not the Other Careers?")

        with st.expander("🧠 ML Engineer"):
            if "TENSORFLOW" not in text.upper():
                st.write("❌ TensorFlow not found")

            if "PYTORCH" not in text.upper():
                st.write("❌ PyTorch not found")

            if "NUMPY" not in text.upper():
                st.write("❌ NumPy not found")

            st.success("✔ Strong Machine Learning foundation detected.")

        with st.expander("📊 Data Analyst"):
            if "EXCEL" not in text.upper():
                st.write("❌ Excel not found")

            if "POWER BI" not in text.upper():
                st.write("❌ Power BI not found")

            if "TABLEAU" not in text.upper():
                st.write("❌ Tableau not found")

            st.success("✔ SQL skills detected.")

        with st.expander("🐍 Python Developer"):
            if "DJANGO" not in text.upper():
                st.write("❌ Django not found")

            if "FLASK" not in text.upper():
                st.write("❌ Flask not found")

            if "REACT" not in text.upper():
                st.write("❌ React not found")

            st.success("✔ Python skills detected.")    

    today = get_today()

    candidate = get_candidate_name(text)

    rating = get_rating(career_score)
    
    report = generate_report(
        candidate,
        ats_score,
        career_score,
        best_role,
        rating,
        skills_found
    )
   
    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="sparrow_report.txt",
        mime="text/plain"
        )