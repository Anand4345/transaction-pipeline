from app.core.celery_app import celery
from app.services.pipeline import run_pipeline

@celery.task
def process_job(job_id, file_path):
    run_pipeline(job_id, file_path)