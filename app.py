import streamlit as st
from pypdf import PdfReader

st.title("🪶 Sparrow Agent")

st.write("Welcome to Sparrow Agent!")

upload_file = st.file_uploader(
    "Upload a resume(PDF)", 
    type=["pdf"]
)

if upload_file:
    st.success("Resume uploaded successfully!")

    pdf = PdfReader(upload_file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

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

    st.subheader("📊 Resume Score")

    st.metric(
        label="Overall Score",
        value=f"{score}/100"
    )

    ats_score = 0

    if "EDUCATION" in text.upper():
        ats_score += 20

    if "SKILLS" in text.upper():
        ats_score += 20

    if "PROJECT" in text.upper():
        ats_score += 20

    if "EXPERIENCE" in text.upper():
        ats_score += 20

    if "CERTIFICATION" in text.upper():
        ats_score += 20

    st.subheader("🤖 ATS Compatibility Score")

    st.metric(
        label="ATS Score",
        value=f"{ats_score}/100"
    )

    if ats_score >= 80:
        st.success("✅ ATS Friendly Resume")

    elif ats_score >= 60:
        st.warning("⚠️ Moderately ATS Friendly")

    else:
        st.error("❌ ATS Optimization Needed")

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

        for skill in missing_skills:
            st.write(f"❌ {skill}")

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
        st.warning("⚠ Add internship, freelance, or project experience.")

    if "CERTIFICATION" not in text.upper():
        st.warning("⚠ Add industry-relevant certifications.")

    if "LINKEDIN" not in text.upper():
        st.warning("⚠ Add your LinkedIn profile link.")

    if len(missing_skills) > 0:
        st.warning(
            f"⚠ Consider learning: {', '.join(missing_skills)}"
        )
    if score >= 75:
        st.success(
            "✅ Strong technical foundation detected. Focus on experience and skill expansion."
        )
    report = f"""
    SPARROW AGENT REPORT

    Resume Score: {score}/100

    ATS Score: {ats_score}/100

    Missing Skills:
    {', '.join(missing_skills)}

    Generated by Sparrow Agent
    """
    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="sparrow_report.txt",
        mime="text/plain"
    )