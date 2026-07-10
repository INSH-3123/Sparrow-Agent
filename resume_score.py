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
    text = text.upper().strip()

    if "PROJECT" not in text:
        return 0

    project_text = text 

    technologies_found = 0

    for tech, aliases in ALIASES.items():

        if any(alias in project_text for alias in aliases):
            technologies_found += 1

    if technologies_found >= 10:
        return MAX_PROJECTS

    elif technologies_found >= 7:
        return 15

    elif technologies_found >= 4:
        return 10

    elif technologies_found >= 1:
        return 5    

    return 0 


def score_experience(text):
    text = text.upper().strip()
    
    if "EXPERIENCE" in text:
        return MAX_EXPERIENCE

    elif "INTERNSHIP" in text:
        return 15 

    return 0


def score_certifications(text):
    text = text.upper().strip()

    if "CERTIFICATION" not in text:
        return 0
    
    if "CERTIFICATION" in text:
        return MAX_CERTIFICATIONS
    
    return 0


def score_achievements(text):
    text = text.upper().strip()

    if "ACHIEVEMENT" in text:
        return MAX_ACHIEVEMENTS

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