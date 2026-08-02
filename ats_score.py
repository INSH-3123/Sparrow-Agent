MAX_CONTACT = 10
MAX_EDUCATION = 10
MAX_SKILLS = 10
MAX_PROJECTS = 10
MAX_EXPERIENCE = 10
MAX_CERTIFICATIONS = 10
MAX_GITHUB = 5
MAX_LINKEDIN = 5
MAX_READABILITY = 10
MAX_FORMATTING = 10
MAX_HEADINGS = 10

def score_contact(text):
    text = text.upper().strip()

    has_email = "@" in text

    has_phone = "+" in text or any(char.isdigit() for char in text)

    if has_email and has_phone:
        return MAX_CONTACT  

    elif has_email or has_phone:
        return 5 

    return 0

def score_education(text):
    text = text.upper().strip()

    if "EDUCATION" not in text:
        return 0

    degree_keywords = [
        "B.TECH", "BTECH", "B.E", "BE",
        "BACHELOR", "M.TECH", "MTECH",
        "M.E", "ME", "MASTER",
        "BSC", "MSC", "MCA", "DIPLOMA"
    ]

    if any(degree in text for degree in degree_keywords):
        return MAX_EDUCATION

    return 4

def score_headings(text):
    text = text.upper().strip()

    headings = ["EDUCATION", "SKILLS", "PROJECT", "EXPERIENCE", "CERTIFICATION"]

    headings_found = sum(1 for heading in headings if heading in text)

    return min(headings_found * 2, MAX_HEADINGS)

from aliases import ALIASES

def score_skills(text):
    text = text.upper()

    if "SKILLS" not in text:
        return 0

    skills_found = 0

    for skill, aliases in ALIASES.items():
        if any(alias in text for alias in aliases):
            skills_found += 1

    if skills_found >= 10:
        return MAX_SKILLS
    elif skills_found >= 7:
        return 8
    elif skills_found >= 4:
        return 6
    elif skills_found >= 2:
        return 4

    return 2

import re

def score_projects(text):
    text = text.upper()

    match = re.search(
        r"PROJECTS?(.*?)(EDUCATION|SKILLS|EXPERIENCE|WORK EXPERIENCE|INTERNSHIPS|CERTIFICATIONS|ACHIEVEMENTS|SUMMARY|PROFILE|$)",
        text,
        re.DOTALL
    )

    if not match:
        return 0

    project_section = match.group(1)

    project_count = len([
        line.strip()
        for line in project_section.splitlines()
        if line.strip()
    ])

    if project_count >= 4:
        return MAX_PROJECTS
    elif project_count >= 3:
        return 8
    elif project_count >= 2:
        return 6
    elif project_count >= 1:
        return 3

    return 0

def score_experience(text):
    text = text.upper()

    if "WORK EXPERIENCE" in text or "PROFESSIONAL EXPERIENCE" in text:
        return MAX_EXPERIENCE

    elif "INTERNSHIP" in text or "INTERNSHIPS" in text:
        return 7

    elif "EXPERIENCE" in text:
        return 3

    return 0

import re

def score_certifications(text):
    text = text.upper()

    match = re.search(
        r"CERTIFICATIONS?(.*?)(PROJECTS?|EDUCATION|SKILLS|EXPERIENCE|ACHIEVEMENTS|SUMMARY|PROFILE|$)",
        text,
        re.DOTALL
    )

    if not match:
        return 0

    cert_section = match.group(1)

    cert_count = len([
        line.strip()
        for line in cert_section.splitlines()
        if line.strip()
    ])

    if cert_count >= 3:
        return MAX_CERTIFICATIONS
    elif cert_count == 2:
        return 7
    elif cert_count == 1:
        return 4

    return 0

def score_github(text):
    text = text.upper().strip()
    
    headings = [
        "GITHUB",
        "GITHUB.COM"
    ]   

    if any(heading in text for heading in headings):
        return MAX_GITHUB

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

def score_readability(text):
    text = text.strip()

    score = 0

    words = len(text.split())

    if words >= 200:
        score += 2

    if text.count("\n") >= 15:
        score += 2

    if "@" in text:
        score += 2

    if "LINKEDIN" in text.upper():
        score += 2

    if "GITHUB" in text.upper():
        score += 2

    return min(score, MAX_READABILITY)

def score_formatting(text):
    text = text.upper().strip()

    headings = [
        "EDUCATION",
        "SKILLS",
        "PROJECT",
        "EXPERIENCE",
        "CERTIFICATION"
    ]

    score = sum(1 for heading in headings if heading in text)

    return min(score * 2, MAX_FORMATTING)

def calculate_ats_score(text): 
    breakdown = {
        "Contact": score_contact(text),
        "Education": score_education(text),
        "Skills": score_skills(text),
        "Projects": score_projects(text),
        "Experience": score_experience(text),
        "Certifications": score_certifications(text),
        "GitHub": score_github(text),
        "LinkedIn": score_linkedin(text),
        "Readability": score_readability(text),
        "Formatting": score_formatting(text),
    }

    total = sum(breakdown.values())

    return total, breakdown