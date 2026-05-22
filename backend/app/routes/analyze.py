from fastapi import APIRouter
from app.models.job import JobInput
from app.services.scoring_service import calculate_trust_score

router = APIRouter()


@router.post("/analyze-job")
def analyze_job(job: JobInput):

    result = calculate_trust_score(job.description)

    return {
        "job_title": job.title,
        "company": job.company,
        "analysis": result
    }