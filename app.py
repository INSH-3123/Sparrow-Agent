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

from ats_analyzer import analyze_ats

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
        text += page.extract_text()

    st.session_state.resume_text = text    

    detected_domain, domain_scores = detect_domain(text)

    career_profile = CAREER_PROFILES.get(detected_domain)

    st.success(f"🎯 Detected Domain: {detected_domain}")

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

            with st.expander("🪶 Why this score?"):

                if score >= 80:
                    st.success("Excellent resume quality!")

                elif score >= 60:
                    st.info("Your resume is well structured with a few areas to improve.")

                else:
                    st.warning("Your resume needs significant improvements.")

                st.markdown("### 📄 Resume Review")

                st.write("✅ Clear contact information")

                st.write("✅ Technical skills included")

                st.write("✅ Education section present")

                st.write("💡 Add measurable achievements")

                st.write("💡 Strengthen project descriptions")

    ats_score, ats_sections = analyze_ats(text)

    with col2:
        with st.container(border=True):
            st.metric(
                "ATS Score",
                f"{ats_score}/100"
            )
            st.progress(ats_score / 100)

            with st.expander("🪶 Why this score?"):
                if ats_score >= 80:
                    st.success("Excellent ATS compatibility!")

                elif ats_score >= 60:
                    st.warning("Good ATS compatibility, but there is room for improvement.")

                else:
                    st.error("Your resume needs ATS optimization.")

                st.markdown("### ✔ ATS Checklist")

                if "Education" in ats_sections:
                    st.write("✅ Education section detected")
                else:
                    st.write("⚠️ Education section missing")

                if "Skills" in ats_sections:
                    st.write("✅ Skills section detected")
                else:
                    st.write("⚠️ Skills section missing")

                if "Projects" in ats_sections:
                    st.write("✅ Projects section detected")
                else:
                    st.write("⚠️ Projects section missing")

                if "Experience" in ats_sections:
                    st.write("✅ Experience section detected")
                else:
                    st.write("⚠️ Experience section missing")

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

            with st.expander("🪶 Why this score?"):

                if career_score >= 80:
                    st.success("You're highly prepared for entry-level opportunities.")

                elif career_score >= 60:
                    st.info("You're on a good path. A few improvements can make you much stronger.")

                else:
                    st.warning("Your profile needs further development before applying confidently.")

                st.markdown("### 🚀 Career Readiness Factors")

                st.write(f"📄 Resume Quality: **{score}/100**")

                st.write(f"🤖 ATS Compatibility: **{ats_score}/100**")

                st.write("💼 Projects and technical skills improve readiness.")

                st.write("📚 Certifications and portfolio can further strengthen your profile.")


    st.subheader("🎯 Skill Gap Analysis")

    required_skills = career_profile["required_skills"]

    print(required_skills)

    missing_skills = []

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
            "STAADPRO",
            "STAAD.PRO",
            "STAAD-PRO"
        ]
    }

    for skill in required_skills:

        keywords = aliases.get(skill, [skill])

        if not any(keyword in text.upper() for keyword in keywords):
            missing_skills.append(skill)

    st.write(f"Career Domain: {detected_domain}")
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
                st.caption(f"Recommended skill for {detected_domain}.")

    st.subheader("💡 Recommendations")
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.analyzed:

            with st.expander("🎯 Skill Recommendations"):

                st.subheader("📚 Learning Recommendations")

            unique_skills = sorted(set(missing_skills))

            for skill in unique_skills:
                st.success(f"📘 Learn {skill}")

    with col2:
        if st.session_state.analyzed:
            
            with st.expander("💼 Job Role Recommendations"):

                roles = career_profile["roles"]

                st.subheader(f"💼 Recommended Roles for {detected_domain}")

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
        career_scores, best_role = analyze_career(text, detected_domain)

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

    if st.button(
        "✨ Analyze with Sparrow AI",
        use_container_width=True
    ):

            prompt = f"""
            You are Sparrow AI Career Mentor.

            The user's selected career domain is:

            {detected_domain}

            The following report was generated by Sparrow Agent after resume analysis,
            ATS evaluation, career matching and career coaching.

            Treat the report as factual.

            Do NOT change the analysis.

            Do NOT contradict the report.

            Instead, explain it professionally while tailoring all advice specifically for the user's career domain.

            For example:

            - If the domain is AI & Data Science, recommend AI technologies and career paths.
            - If the domain is Software Engineering, recommend software engineering technologies and roles.
            - If the domain is Mechanical Engineering, recommend mechanical engineering skills and careers.
            - If the domain is Civil Engineering, recommend civil engineering skills and careers.
            - If the domain is Business & Management, recommend business-related careers and certifications.

            Sparrow Career Report:

            {report}

            Respond in Markdown.

            Use these sections:

            # 📌 Career Summary

            # 💪 Key Strengths

            # ⚠ Areas for Improvement

            # 📚 Recommended Learning Path

            # 🚀 Next Career Steps

            # ⭐ Final Advice

            Keep the response under 300 words.

            Be encouraging, realistic and actionable.
            """

            with st.spinner("🪶 Sparrow AI is analyzing your report... Please wait..."):
                response = ask_ai(prompt)

            st.toast("🪶 Sparrow AI analysis completed!")  

            st.divider()

            st.subheader("🪶 Sparrow AI Career Mentor")
            st.caption("Powered by Google Gemini 2.5 Flash AI")

            with st.container(border=True):
                st.markdown(response)