EXACT_MATCH_SCORE = 5
NORMAL_MATCH_SCORE = 1

HIGH_PRIORITY_KEYWORDS = [
    "artificial intelligence",
    "artificial intelligence & data science",
    "artificial intelligence and data science",
    "machine learning",
    "deep learning",
]

from aliases import ALIASES

DOMAINS = {

    "AI & Data Science": [
        "python",
        "tensorflow",
        "machine learning",
        "deep learning",
        "data science",
        "pandas",
        "numpy",
        "scikit",
        "keras",
        "pytorch",
        "cnn",
        "nlp",
        "artificial intelligence",
        "ai",
        "artificial intelligence & data science",
        "artificial intelligence and data science",
        "ai & data science",
        "computer vision",
        "large language models",
        "llm",
        "generative ai",
        "data analytics",
    ],

    "Software Engineering": [
        "java",
        "c++",
        "javascript",
        "react",
        "node",
        "django",
        "flask",
        "api",
        "backend",
        "frontend",
        "sql",
        "git"
    ],

    "Cybersecurity": [
        "penetration testing",
        "ethical hacking",
        "kali",
        "wireshark",
        "network security",
        "cryptography",
        "firewall"
    ],

    "Cloud Computing": [
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",
        "cloud",
        "terraform"
    ],

    "Mechanical Engineering": [
        "autocad",
        "solidworks",
        "catia",
        "manufacturing",
        "thermodynamics",
        "cad"
    ],

    "Civil Engineering": [
        "autocad",
        "staad",
        "revit",
        "surveying",
        "construction",
        "structural"
    ],

    "Electronics": [
        "arduino",
        "embedded",
        "vlsi",
        "verilog",
        "pcb",
        "microcontroller",
        "iot"
    ],

    "Business & Management": [
        "marketing",
        "finance",
        "sales",
        "business",
        "operations",
        "hr",
        "management"
    ]

}

def detect_domain(resume_text):
    """
    Detects the most suitable career domain
    based on keyword matching.
    """

    resume_text = resume_text.lower()

    scores = {}

    for domain, keywords in DOMAINS.items():

        scores[domain] = 0

        for keyword in keywords:

            keyword_aliases = ALIASES.get(keyword.upper(), [keyword])

            if any(alias.lower() in resume_text for alias in keyword_aliases):

                if keyword in HIGH_PRIORITY_KEYWORDS:
                    scores[domain] += EXACT_MATCH_SCORE
                else:
                    scores[domain] += NORMAL_MATCH_SCORE

    highest_score = max(scores.values())

    if highest_score == 0:
        return "Unknown", scores, 0

    total_score = sum(scores.values())

    confidence = int(
        highest_score /
        total_score
        * 100
    ) if total_score else 0

    detected_domain = max(scores, key=scores.get)

    return detected_domain, scores, confidence