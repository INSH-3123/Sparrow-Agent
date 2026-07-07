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

    if "EDUCATION" in text:
        return MAX_EDUCATION
    return 0    

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


def score_projects(text):
    pass


def score_experience(text):
    pass


def score_certifications(text):
    pass


def score_achievements(text):
    pass


def score_portfolio(text):
    pass


def score_github(text):
    pass


def score_linkedin(text):
    pass


def score_formatting(text):
    pass


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