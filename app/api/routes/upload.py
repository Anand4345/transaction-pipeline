from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.job import Job
from app.workers.worker import process_job

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs/upload")
def upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    path = f"uploads/{file.filename}"

    with open(path, "wb") as f:
        f.write(file.file.read())

    job = Job(filename=file.filename, status="pending")

    db.add(job)
    db.commit()
    db.refresh(job)

    process_job.delay(job.id, path)

    return {"job_id": job.id}