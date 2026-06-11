from fastapi import FastAPI
from app.database.init_db import init_db
from app.api.routes.jobs import router
from app.api.routes.jobs import router


app = FastAPI()

init_db()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Transaction Pipeline API is running"}

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)