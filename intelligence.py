def analyze_candidate(text):

    text = text.upper()

    strengths = []
    weaknesses = []
    suggestions = []

   

    if "PYTHON" in text:
        strengths.append("Strong Python programming foundation")

    if "MACHINE LEARNING" in text:
        strengths.append("Knowledge of Machine Learning concepts")

    if "PROJECT" in text:
        strengths.append("Hands-on project experience")

    if "SQL" in text:
        strengths.append("Database management skills")


    if "EXPERIENCE" not in text:
        weaknesses.append("No internship or professional experience detected")

    if "CERTIFICATION" not in text:
        weaknesses.append("No certifications found")

    if "LINKEDIN" not in text:
        weaknesses.append("LinkedIn profile missing")



    if "EXPERIENCE" not in text:
        suggestions.append("Apply for internships or contribute to open-source projects")

    if "CERTIFICATION" not in text:
        suggestions.append("Complete an industry-recognized certification")

    if "LINKEDIN" not in text:
        suggestions.append("Create and optimize your LinkedIn profile")

    return strengths, weaknesses, suggestions