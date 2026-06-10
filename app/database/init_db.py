from app.models.base import Base
from app.database.session import engine

from app.models.job import Job
from app.models.transaction import Transaction
from app.models.summary import JobSummary

def init_db():
    Base.metadata.create_all(bind=engine)