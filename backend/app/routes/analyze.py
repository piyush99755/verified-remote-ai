from fastapi import APIRouter
from app.models.job import JobInput
from app.services.scoring_service import calculate_trust_score
from app.services.ai_service import analyze_job_with_ai

router = APIRouter()


@router.post("/analyze-job")
def analyze_job(job: JobInput):

    score_result = calculate_trust_score(job.description)

    ai_analysis = analyze_job_with_ai(
        job.title,
        job.company,
        job.description
    )

    return {
        "job_title": job.title,
        "company": job.company,
        "trust_analysis": score_result,
        "ai_analysis": ai_analysis
    }