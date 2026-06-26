from datetime import datetime


def get_today():
    return datetime.now().strftime("%d-%m-%Y")

def get_candidate_name(text):
    return text.strip().split("\n")[0]

def get_rating(career_score):

    if career_score >= 85:
        return "🌟 Excellent"

    elif career_score >= 70:
        return "✅ Good"

    elif career_score >= 50:
        return "⚠️ Average"

    else:
        return "❌ Needs Improvement"