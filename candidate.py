from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database import get_db
from app.models.user import User
from app.schemas.candidate import (
    CandidateDeleteResponse,
    CandidateListResponse,
    CandidateResponse
)
from app.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


@router.post(
    "/upload",
    response_model=CandidateResponse
)
def upload_candidate(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str | None = Form(None),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return CandidateService.upload_candidate(
        full_name=full_name,
        email=email,
        phone=phone,
        file=file,
        current_user=current_user,
        db=db
    )


@router.get(
    "",
    response_model=list[CandidateListResponse]
)
def get_all_candidates(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return CandidateService.get_all_candidates(
        db=db
    )


@router.get(
    "/{candidate_id}",
    response_model=CandidateResponse
)
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return CandidateService.get_candidate(
        candidate_id=candidate_id,
        db=db
    )


@router.delete(
    "/{candidate_id}",
    response_model=CandidateDeleteResponse
)
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return CandidateService.delete_candidate(
        candidate_id=candidate_id,
        db=db
    )