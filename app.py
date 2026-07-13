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

from domain_detector import detect_domain

from career_analyzer import analyze_career

from resume_analyzer import analyze_resume

from report_generator import generate_report 

from utils import (
    get_today,
    get_candidate_name,
    get_rating,
)

from intelligence import analyze_candidate 

from career_coach import career_coach

from ai_chat import ask_ai

from career_profiles import CAREER_PROFILES

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
        
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"


    st.session_state.resume_text = text    

    detected_domain, domain_scores, confidence = detect_domain(text)

    career_profile = CAREER_PROFILES.get(detected_domain)

    st.success(f"🎯 Detected Domain: {detected_domain}")

    st.caption(f"Confidence: {confidence}%")

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

    if upload_file is None:
        st.warning("📄 Please upload a resume first.")
        st.stop()

    text = st.session_state.get("resume_text", "")

    if len(text.split()) < 20:

        st.error("📄 No readable text was found in the uploaded resume.")
        st.caption("Sparrow couldn't extract any text from this PDF.")

        st.info(
            """
    Please upload a resume that contains selectable text.

    Possible reasons:
    • The PDF is scanned as an image.
    • The file is empty.
    • The PDF is corrupted.
    • The text could not be extracted.
    """
        )

        st.stop()

    strengths, weaknesses, suggestions = analyze_candidate(text)

    resume_score, ats_score, career_score, missing_skills, skills_found = analyze_resume(
        text,
        detected_domain,
        career_profile
    )


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

    career_scores, best_role = analyze_career(text, detected_domain)

    career_score = career_scores[best_role]

    best_role = max(career_scores, key=career_scores.get)

    roles = career_profile["roles"].keys()

    cols = st.columns(2)

    for i, role in enumerate(roles):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"### 💼 {role}")
                st.metric("Match", f"{career_scores[role]}%")
                st.progress(career_scores[role] / 100)

    st.divider()

    advice = career_coach(text)

    st.subheader("🪶 Why This Career Matches You")   

    with st.container(border=True):
        st.markdown("## 🎯 Best Career Match")
        st.metric(
            "Recommended Role",
            best_role
        )
        
    aliases = {
        "AUTOCAD": [
            "AUTOCAD",
            "AUTO CAD",
            "AUTO-CAD",
            "AUTODESK AUTOCAD"
        ],

        "STAAD": [
            "STAAD",
            "STAAD PRO",
            "STAAD-PRO",
            "STAADPRO",
            "STAAD.PRO"
        ]
    }

    for skill in career_profile["required_skills"]:

        keywords = aliases.get(skill, [skill])

        if any(keyword in text.upper() for keyword in keywords):
            st.write(f"✅ {skill} detected")

        else:
            st.write(f"❌ {skill} not detected")


    st.info(f"""
    Sparrow selected **{best_role}** because your resume demonstrates strong technical skills and is the best overall match based on the detected technologies in your resume.
    """)

        
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

    if "show_report_upload" not in st.session_state:
        st.session_state.show_report_upload = False    

    if st.button(
        "🪶 AI Career Guidance",
        use_container_width=True
    ):
        st.session_state.show_report_upload = True

    if st.session_state.show_report_upload:

        uploaded_report = st.file_uploader(
            "📤 Upload Downloaded Sparrow Report (.txt)",
            type=["txt"]
        )    

        st.caption(
            "Upload the Sparrow report you downloaded to receive personalized AI career guidance."
        )

        if uploaded_report is not None:

            if st.button(
                "✨ Generate AI Career Guidance",
                use_container_width=True
            ):

                uploaded_report_text = uploaded_report.read().decode("utf-8")  

                prompt = f"""
                You are Sparrow AI Career Mentor.

                You are the AI mentor inside Sparrow Agent.

                Your responsibility is to explain Sparrow's analysis, not replace it.

                Treat every score and recommendation generated by Sparrow as factual.

                Do NOT recalculate scores.

                Do NOT contradict Sparrow's analysis.

                Do NOT invent missing information.

                ------------------------------------------------------------

                Candidate Career Domain

                {detected_domain}

                Domain Detection Confidence

                {confidence}%

                ------------------------------------------------------------

                Sparrow Career Report

                {uploaded_report_text}

                ------------------------------------------------------------

                Instructions

                Explain Sparrow's findings professionally.

                Tailor every recommendation specifically to the detected career domain.

                For example:

                • AI & Data Science → AI, ML, Data Science technologies and roles.

                • Software Engineering → Software development, backend, frontend and full-stack careers.

                • Cybersecurity → Security certifications, networking and penetration testing.

                • Cloud Computing → AWS, Azure, DevOps and Cloud Engineering.

                • Mechanical Engineering → CAD, Manufacturing, Design Engineering.

                • Civil Engineering → Structural, Construction and Site Engineering.

                • Electronics → Embedded Systems, VLSI and IoT.

                • Business & Management → Business Analytics, Marketing, Operations and Management.

                ------------------------------------------------------------

                Respond using Markdown.

                Use exactly these sections.

                # 📌 Career Summary

                # 💪 Key Strengths

                # ⚠ Areas for Improvement

                # 📚 Recommended Learning Path

                # 🚀 Next Career Steps

                # ⭐ Final Advice

                Keep the response under 300 words.

                Be encouraging, realistic and actionable.

                Avoid generic career advice.

                Base every recommendation on Sparrow's report.
                """
                with st.spinner("🪶 Sparrow AI is analyzing your report... Please wait..."):
                    response = ask_ai(prompt)

                st.session_state.show_report_upload = False

                st.success("🪶 AI Career Guidance generated successfully!")  

                st.divider()

                st.subheader("🪶 Sparrow AI Career Mentor")
                st.caption("Powered by Google Gemini 2.5 Flash AI")

                with st.container(border=True):
                    st.markdown(response)