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

def score_headings(text):
    text = text.upper().strip()

    headings = ["EDUCATION", "SKILLS", "PROJECT", "EXPERIENCE", "CERTIFICATION"]

    headings_found = sum(1 for heading in headings if heading in text)

    return min(headings_found * 2, MAX_HEADINGS)

def score_skills(text):
    text = text.upper().strip()

    headings = [
        "SKILLS",
        "TECHNICAL SKILLS",
        "TECHNICAL EXPERTISE",
        "CORE COMPETENCIES"
    ]

    if any(heading in text for heading in headings):
        return MAX_SKILLS

    return 0

def score_projects(text):
    text = text.upper().strip()

    headings = [
        "PROJECT",
        "PROJECTS",
        "ACADEMIC PROJECTS",
        "RESEARCH PROJECTS"
    ]

    if any(heading in text for heading in headings):
        return MAX_PROJECTS

    return 0

def score_experience(text):
    text = text.upper().strip()

    headings = [
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "PROFESSIONAL EXPERIENCE",
        "INTERNSHIP",
        "INTERNSHIPS"
    ]

    if any(heading in text for heading in headings):
        return MAX_EXPERIENCE

    return 0

def score_certifications(text):
    text = text.upper().strip()

    headings = [
        "CERTIFICATION",
        "CERTIFICATIONS",
        "CERTIFICATE",
        "LICENSES"
    ]

    if any(heading in text for heading in headings):
        return MAX_CERTIFICATIONS

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
    text = text.upper().strip()

    score = 0

    if "@" in text:
        score += 2

    if "+" in text or any(char.isdigit() for char in text):
        score += 2

    if "EDUCATION" in text:
        score += 2

    if "SKILLS" in text:
        score += 2

    if "EXPERIENCE" in text:
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
        "Education": score_headings(text),
        "Skills": score_skills(text),
        "Projects": score_projects(text),
        "Experience": score_experience(text),
        "Certifications": score_certifications(text),
        "GitHub": score_github(text),
        "LinkedIn": score_linkedin(text),
        "Readability": score_readability(text),
        "Formatting": score_formatting(text),
        "ATS Headings": score_headings(text),
    }

    total = sum(breakdown.values())

    return total, breakdown