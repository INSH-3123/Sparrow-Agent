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

if st.button("Analyze Resume"):

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

    st.subheader("💡 Recommendations")

    if "EXPERIENCE" not in text.upper():
        st.warning(
            "Consider adding internships, freelance work, "
            "or project-based experience to strengthen your resume."
    )

    if "CERTIFICATION" not in text.upper():
        st.warning(
            "Adding relevant certifications can improve credibility."
    )

    if score == 100:
        st.success("🎉 Resume structure looks complete!")