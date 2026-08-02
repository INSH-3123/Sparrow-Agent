from aliases import ALIASES 

MAX_EDUCATION = 15
MAX_SKILLS = 20
MAX_PROJECTS = 20
MAX_EXPERIENCE = 20
MAX_CERTIFICATIONS = 10
MAX_ACHIEVEMENTS = 5
MAX_PORTFOLIO = 5
MAX_GITHUB = 5
MAX_LINKEDIN = 5
MAX_FORMATTING = 5

def score_education(text):
    text = text.upper().strip()

    score = 0

    if "EDUCATION" in text :
        score += 5

    else:
        return 0

    degree_keywords = [
        "B.TECH", "BTECH", "B.E", "BE",
        "BACHELOR", "M.TECH", "MTECH",
        "M.E", "ME", "MASTER",
        "BSC", "MSC", "MCA", "DIPLOMA"
    ]

    if any(degree in text for degree in degree_keywords):
        score += 5

    if "%" in text or "CGPA" in text or "GPA" in text:
        score += 5

    return min(score, MAX_EDUCATION)


def score_skills(text):
    text = text.upper().strip()
    
    skills_found = 0

    for skill, aliases in ALIASES.items():

        if any(alias in text for alias in aliases): 
            skills_found += 1

    if skills_found >= 10:
        return MAX_SKILLS

    elif skills_found >= 7:
        return 15

    elif skills_found >= 4:
        return 10

    elif skills_found >= 1:
        return 5

    return 0      


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

    technologies_found = 0

    for tech, aliases in ALIASES.items():
        if any(alias in project_section for alias in aliases):
            technologies_found += 1

    if technologies_found >= 10:
        return MAX_PROJECTS
    elif technologies_found >= 7:
        return 15
    elif technologies_found >= 4:
        return 10
    elif technologies_found >= 2:
        return 5

    return 0



def score_experience(text):
    text = text.upper().strip()
    
    if "WORK EXPERIENCE" in text or "PROFESSIONAL EXPERIENCE" in text:
        return MAX_EXPERIENCE

    elif "INTERNSHIP" in text or "INTERNSHIPS" in text:
        return 15

    elif "EXPERIENCE" in text:
        return 10

    return 0


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


def score_achievements(text):
    text = text.upper()

    match = re.search(
        r"ACHIEVEMENTS?(.*?)(PROJECTS?|EDUCATION|SKILLS|EXPERIENCE|CERTIFICATIONS|SUMMARY|PROFILE|$)",
        text,
        re.DOTALL
    )

    if not match:
        return 0

    achievement_section = match.group(1)

    count = len([
        line.strip()
        for line in achievement_section.splitlines()
        if line.strip()
    ])

    if count >= 2:
        return MAX_ACHIEVEMENTS

    elif count == 1:
        return 3

    return 0


def score_portfolio(text):
    text = text.upper().strip()

    if "PORTFOLIO" in text:
        return MAX_PORTFOLIO

    return 0


def score_github(text):
    text = text.upper().strip()

    if "GITHUB" in text:
        return MAX_GITHUB

    return 0


def score_linkedin(text):
    text = text.upper().strip()

    if "LINKEDIN" in text:
        return MAX_LINKEDIN

    return 0


def score_formatting(text):
    text = text.upper().strip()

    formatting_score = 0

    if "@" in text:
        formatting_score += 2

    if "+" in text or any(char.isdigit() for char in text):
        formatting_score += 1

    if "EDUCATION" in text:
        formatting_score += 1

    if "SKILLS" in text:
        formatting_score += 1

    return min(formatting_score, MAX_FORMATTING)


def calculate_resume_score(text):

    breakdown = {
        "Education": score_education(text),
        "Relevant Skills": score_skills(text),
        "Projects": score_projects(text),
        "Experience": score_experience(text),
        "Certifications": score_certifications(text),
        "Achievements": score_achievements(text),
        "Portfolio": score_portfolio(text),
        "GitHub": score_github(text),
        "LinkedIn": score_linkedin(text),
        "Formatting": score_formatting(text)
    }

    total = sum(breakdown.values())

    return total, breakdown