from fastapi import APIRouter

from .jobs import router as jobs_router
from .upload import router as upload_router

router = APIRouter()

router.include_router(jobs_router)
router.include_router(upload_router)