from career_profiles import CAREER_PROFILES

from aliases import ALIASES

CORE_SKILL_SCORE = 20
IMPORTANT_SKILL_SCORE = 15
BONUS_SKILL_SCORE = 5
PROJECT_SCORE = 15
EXPERIENCE_SCORE = 20

def analyze_career(text, detected_domain):

    text = text.upper()

    profile = CAREER_PROFILES.get(detected_domain)

    career_scores = {}

    for role, role_data in profile["roles"].items():

        score = 0

        core_skills = role_data["core_skills"]
        important_skills = role_data["important_skills"]
        bonus_skills = role_data["bonus_skills"]

        for skill in core_skills:
            keywords = ALIASES.get(skill.upper(), [skill])

            if any(keyword in text for keyword in keywords):
                score += CORE_SKILL_SCORE

        for skill in important_skills:
            keywords = ALIASES.get(skill.upper(), [skill])

            if any(keyword in text for keyword in keywords):
                score += IMPORTANT_SKILL_SCORE

        for skill in bonus_skills:
            keywords = ALIASES.get(skill.upper(), [skill])

            if any(keyword in text for keyword in keywords):
                score += BONUS_SKILL_SCORE

        if "PROJECT" in text:
            score += PROJECT_SCORE

        if "EXPERIENCE" in text:
            score += EXPERIENCE_SCORE

        score = min(score, 100)

        career_scores[role] = score

    best_role = max(career_scores, key=career_scores.get)

    return career_scores, best_role