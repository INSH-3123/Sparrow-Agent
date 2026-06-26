def analyze_ats(text):

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

    sections = {
        "Education": "EDUCATION" in text.upper(),
        "Skills": "SKILLS" in text.upper(),
        "Projects": "PROJECT" in text.upper(),
        "Experience": "EXPERIENCE" in text.upper(),
        "Certifications": "CERTIFICATION" in text.upper()
    }

    return ats_score, sections