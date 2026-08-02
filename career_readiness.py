MAX_PROJECTS = 20
MAX_EXPERIENCE = 20
MAX_GITHUB = 10
MAX_PORTFOLIO = 10
MAX_CERTIFICATIONS = 10
MAX_COMMUNICATION = 10
MAX_LINKEDIN = 5
MAX_RESUME_QUALITY = 10
MAX_ATS_QUALITY = 5

import re

def score_projects(text):
    text = text.upper()

    match = re.search(
        r"PROJECTS?(.*?)(EDUCATION|SKILLS|EXPERIENCE|WORK EXPERIENCE|INTERNSHIPS|CERTIFICATIONS|CERTIFICATES|ACHIEVEMENTS|SUMMARY|PROFILE|$)",
        text,
        re.DOTALL
    )

    if not match:
        return 0

    project_section = match.group(1)

    project_lines = [
        line.strip()
        for line in project_section.splitlines()
        if line.strip()
    ]

    project_count = 0

    for line in project_lines:
        words = line.split()

        # Project titles are usually short
        if 2 <= len(words) <= 8:
            project_count += 1

    if project_count >= 4:
        return MAX_PROJECTS

    elif project_count >= 3:
        return 15

    elif project_count >= 2:
        return 10

    elif project_count >= 1:
        return 5

    return 0

def score_experience(text):
    text = text.upper().strip()

    if "PROFESSIONAL EXPERIENCE" in text:
        return MAX_EXPERIENCE

    elif "WORK EXPERIENCE" in text:
        return MAX_EXPERIENCE

    elif "EXPERIENCE" in text:
        return 15

    elif "INTERNSHIP" in text or "INTERNSHIPS" in text:
        return 10

    return 0

def score_github(text):
    text = text.upper().strip()

    if "GITHUB" in text:
        return MAX_GITHUB
    return 0

def score_portfolio(text):
    text = text.upper().strip()

    portfolio_keywords = [
        "PORTFOLIO",
        "VERCEL.APP",
        "NETLIFY.APP",
        "GITHUB.IO",
        "BEHANCE.NET",
        "DRIBBBLE.COM",
        "MYPORTFOLIO.COM"
    ]

    if any(keyword in text for keyword in portfolio_keywords):
        return MAX_PORTFOLIO

    return 0

def score_certifications(text):
    text = text.upper().strip()

    headings = [
        "CERTIFICATION",
        "CERTIFICATIONS",
        "CERTIFICATES"
    ]
    if any(heading in text for heading in headings):
        return MAX_CERTIFICATIONS
    return 0

def score_communication(text):
    text = text.upper().strip()

    headings = [
        "SUMMARY",
        "PROFILE",
        "OBJECTIVE",
        "ABOUT ME"
    ]

    if any(heading in text for heading in headings):
        return MAX_COMMUNICATION

    return 0

def score_linkedin(text):
    text = text.upper().strip()

    headings = [ 
        "LINKEDIN",
        "LINKEDIN.COM"
    ]

    if any(heading in text for heading in headings):
        return MAX_LINKEDIN

    return 0

def score_resume_quality(resume_score):

    if resume_score >= 80:
        return MAX_RESUME_QUALITY

    elif resume_score >= 60:
        return 7

    elif resume_score >= 40:
        return 4

    return 0

def score_ats_quality(ats_score):

    if ats_score >= 80:
        return 5

    elif ats_score >= 60:
        return 3

    elif ats_score >= 40:
        return 2

    return 0

def calculate_career_readiness(text, resume_score, ats_score):

    breakdown = { 
        "Projects": score_projects(text),
        "Experience": score_experience(text),
        "GitHub": score_github(text),
        "Portfolio": score_portfolio(text),
        "Certifications": score_certifications(text),
        "Communication": score_communication(text),
        "LinkedIn": score_linkedin(text),
        "Resume Quality": score_resume_quality(resume_score),
        "ATS Quality": score_ats_quality(ats_score)
    }

    total = sum(breakdown.values())

    return total, breakdown