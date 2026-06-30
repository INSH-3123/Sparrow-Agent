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

            if keyword in resume_text:
            if keyword in [
                "artificial intelligence",
                "artificial intelligence & data science",
                "artificial intelligence and data science"
            ]:
                scores[domain] += 5
            else:
                scores[domain] += 1

    detected_domain = max(scores, key=scores.get)

    return detected_domain, scores