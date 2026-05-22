def calculate_trust_score(job_description: str):

    score = 100
    warnings = []

    suspicious_keywords = [
        "quick money",
        "telegram",
        "whatsapp",
        "payment required",
        "earn instantly"
    ]

    for keyword in suspicious_keywords:
        if keyword.lower() in job_description.lower():
            score -= 20
            warnings.append(f"Suspicious keyword detected: {keyword}")

    if score < 0:
        score = 0

    return {
        "trust_score": score,
        "warnings": warnings
    }