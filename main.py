from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, SessionLocal, engine

from app.models import *

from app.routers.auth import router as auth_router
from app.routers.candidate import router as candidate_router
from app.routers.job import router as job_router

from app.seed.role_seed import seed_roles

from app.routers.ai import router as ai_router

from app.routers.dashboard import (
    router as dashboard_router
)

from app.routers.history import (
    router as history_router
)


Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    seed_roles(db)
finally:
    db.close()


app = FastAPI(
    title="AI Resume Screening & Interview Assistant API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(candidate_router)
app.include_router(job_router)
app.include_router(ai_router)
app.include_router(dashboard_router)
app.include_router(history_router)


@app.get("/")
def root():

    return {
        "message": "AI Resume Screening API is running successfully."
    }