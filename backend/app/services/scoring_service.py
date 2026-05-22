def calculate_trust_score(job_description: str):

    overall_score = 100
    warnings = []
    positive_signals = []
    
    scam_risk_score = 0
    job_quality_score = 50
    transparency_score = 50
    remote_authenticity_score = 50
    graph_flags = []


    # NEGATIVE SIGNALS
    negative_rules = {
        "telegram": 15,
        "whatsapp": 15,
        "quick money": 20,
        "payment required": 40,
        "crypto payment": 50,
        "earn instantly": 25,
        "no experience required": 10,
        "easy income": 20,
        "investment required": 40
    }

    # POSITIVE SIGNALS
    positive_rules = {
        "health insurance": 10,
        "remote policy": 10,
        "flexible hours": 5,
        "career growth": 5,
        "visa sponsorship": 10,
        "distributed systems": 5,
        "cloud infrastructure": 5,
        "benefits": 5,
        "paid time off": 5,
        "engineering": 5
    }
    
    transparency_rules = {
    "salary": 10,
    "benefits": 5,
    "remote policy": 10,
    "visa sponsorship": 5,
    "paid time off": 5
}
    
    remote_rules = {
    "remote": 10,
    "worldwide remote": 15,
    "remote policy": 10,
    "hybrid": -10,
    "onsite": -20
}
    
    
    
    description_lower = job_description.lower()
    
    # APPLY NEGATIVE RULES
    for keyword, penalty in negative_rules.items():
        if keyword in description_lower:

            scam_risk_score += penalty
            job_quality_score -= penalty / 2
            
            warnings.append(
                f"Suspicious keyword detected: {keyword}"
            )
    
    # APPLY POSITIVE RULES
    for keyword, bonus in positive_rules.items():

        if keyword in description_lower:

            job_quality_score += bonus

            positive_signals.append(
                f"Positive trust signal: {keyword}"
            )
    # APPLY TRANSPARENCY RULES
    for keyword, bonus in transparency_rules.items():
        if keyword in description_lower:
            transparency_score += bonus
            
    # APPLY REMOTE RULES       
    for keyword, impact in remote_rules.items():
        if keyword in description_lower:
            remote_authenticity_score += impact

    # LIMIT SCORE RANGES
    overall_score = max(0, min(overall_score, 100))
    scam_risk_score = max(0, min(scam_risk_score, 100))
    job_quality_score = max(0, min(job_quality_score, 100))
    transparency_score = max(0, min(transparency_score, 100))
    remote_authenticity_score = max(0, min(remote_authenticity_score, 100))
    
    overall_score = (
        job_quality_score
        + transparency_score
        + remote_authenticity_score
        - scam_risk_score
    ) / 3

    return {
        "overall_score": overall_score,
        "scam_risk_score": scam_risk_score,
        "job_quality_score": job_quality_score,
        "transparency_score": transparency_score,
        "remote_authenticity_score": remote_authenticity_score,
        "warnings": warnings,
        "positive_signals": positive_signals,
        "graph_flags": graph_flags
    }