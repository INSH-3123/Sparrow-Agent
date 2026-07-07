from career_profiles import CAREER_PROFILES


def analyze_career(text, detected_domain):

    text = text.upper()

    profile = CAREER_PROFILES.get(detected_domain)

    career_scores = {}

    aliases = {
        "AUTOCAD": ["AUTOCAD", "AUTO CAD", "AUTO-CAD", "AUTODESK AUTOCAD"]
    }

    for role, skills in profile["roles"].items():

        score = 0

        for skill in skills:
            keywords = aliases.get(skill, [skill])

            if any(keyword in text for keyword in keywords):
                score += 15

        if "PROJECT" in text:
            score += 10

        if "EXPERIENCE" in text:
            score += 10

        score = min(score, 100)

        career_scores[role] = score

    best_role = max(career_scores, key=career_scores.get)

    return career_scores, best_role