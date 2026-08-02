from career_profiles import CAREER_PROFILES

from aliases import ALIASES

CORE_SKILL_SCORE = 40
IMPORTANT_SKILL_SCORE = 10
BONUS_SKILL_SCORE = 5
PROJECT_SCORE = 5
EXPERIENCE_SCORE = 5

def analyze_career(text, detected_domain):

    text = text.upper()

    profile = CAREER_PROFILES.get(detected_domain)

    career_scores = {}

    for role, role_data in profile["roles"].items():

        score = 0
        core_matches = 0 

        core_skills = role_data["core_skills"]
        important_skills = role_data["important_skills"]
        bonus_skills = role_data["bonus_skills"]

        for skill in core_skills:
            keywords = ALIASES.get(skill.upper(), [skill])

            if any(keyword in text for keyword in keywords):
                core_matches += 1

        if core_matches == 0:
            career_scores[role] = 0
            continue

        core_ratio = core_matches / len(core_skills)

        score += core_ratio * CORE_SKILL_SCORE

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

        experience_headings = [
            "EXPERIENCE",
            "WORK EXPERIENCE",
            "PROFESSIONAL EXPERIENCE",
            "INTERNSHIP",
            "INTERNSHIPS"
        ]

        if any(h in text for h in experience_headings):
            score += EXPERIENCE_SCORE

        possible = (
            CORE_SKILL_SCORE +
            len(important_skills) * IMPORTANT_SKILL_SCORE +
            len(bonus_skills) * BONUS_SKILL_SCORE +
            PROJECT_SCORE +
            EXPERIENCE_SCORE
        )
        score = round((score / possible) * 100)

        career_scores[role] = score

    best_role = max(career_scores, key=career_scores.get)

    return career_scores, best_role