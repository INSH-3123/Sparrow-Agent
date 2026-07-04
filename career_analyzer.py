from career_profiles import CAREER_PROFILES


def analyze_career(text, detected_domain):

    text = text.upper()

    profile = CAREER_PROFILES.get(detected_domain)

    roles = profile["roles"]

    career_scores = {}

    for role in roles:

        score = 0

        for skill in profile["required_skills"]:
            if skill in text:
                score += 15

        if "PROJECT" in text:
            score += 10

        if "EXPERIENCE" in text:
            score += 10

        score = min(score, 100)

        career_scores[role] = score = score

    best_role = max(career_scores, key=career_scores.get)

    return career_scores, best_role