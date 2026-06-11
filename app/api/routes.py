from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "healthy"}

@router.get("/jobs")
def get_jobs():
    return []

@router.get("/jobs/{job_id}/status")
def get_status(job_id: str):
    return {
        "job_id": job_id,
        "status": "processing"
    }

@router.get("/jobs/{job_id}/results")
def get_results(job_id: str):
    return {
        "job_id": job_id,
        "cleaned_transactions": [],
        "anomalies": [],
        "summary": {}
    }