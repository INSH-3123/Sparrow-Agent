def analyze_career(text):

    text = text.upper()

    ai_engineer = 35
    ml_engineer = 25
    data_analyst = 30
    python_dev = 30

    if "PYTHON" in text:
        ai_engineer += 10
        ml_engineer += 15
        python_dev += 25

    if "SQL" in text:
        ai_engineer += 5
        data_analyst += 20

    if "MACHINE LEARNING" in text:
        ai_engineer += 15
        ml_engineer += 25

    if "DEEP LEARNING" in text:
        ai_engineer += 15
        ml_engineer += 20

    if "PANDAS" in text:
        data_analyst += 15

    if "NUMPY" in text:
        ml_engineer += 10

    if "REACT" in text:
        python_dev += 10

    if "PROJECT" in text:
        ai_engineer += 10
        ml_engineer += 5
        python_dev += 10

    if "EXPERIENCE" in text:
        ai_engineer += 10
        ml_engineer += 10
        python_dev += 5

    career_scores = {
        "AI Engineer": ai_engineer,
        "ML Engineer": ml_engineer,
        "Data Analyst": data_analyst,
        "Python Developer": python_dev
    }

    best_role = max(career_scores, key=career_scores.get)

    return career_scores, best_role