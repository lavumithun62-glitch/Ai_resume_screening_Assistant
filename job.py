from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.job import (
    JobCreate,
    JobDeleteResponse,
    JobListResponse,
    JobResponse,
    JobUpdate
)

from app.services.job_service import JobService

from app.core.security import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post(
    "",
    response_model=JobResponse
)
def create_job(
    job_data: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = JobService(db)

    return service.create_job(job_data)


@router.get(
    "",
    response_model=list[JobListResponse]
)
def get_all_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = JobService(db)

    return service.get_all_jobs()


@router.get(
    "/{job_id}",
    response_model=JobResponse
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = JobService(db)

    return service.get_job(job_id)


@router.put(
    "/{job_id}",
    response_model=JobResponse
)
def update_job(
    job_id: int,
    job_data: JobUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = JobService(db)

    return service.update_job(
        job_id,
        job_data
    )


@router.delete(
    "/{job_id}",
    response_model=JobDeleteResponse
)
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = JobService(db)

    return service.delete_job(job_id)