from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.ai import (
    MatchRequest,
    MatchResponse,
    InterviewQuestionRequest,
    InterviewQuestionResponse,
    SummaryRequest,
    SummaryResponse
)

from app.services.ai_service import AIService
from app.services.interview_service import InterviewService
from app.services.summary_service import SummaryService

from app.core.security import get_current_user
from app.models.user import User




router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post(
    "/match",
    response_model=MatchResponse
)
def match_resume(
    request: MatchRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = AIService(db)

    return service.match_candidate(
        candidate_id=request.candidate_id,
        job_id=request.job_id
    )

@router.post(
    "/questions",
    response_model=InterviewQuestionResponse
)
def generate_interview_questions(
    request: InterviewQuestionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = InterviewService(db)

    return service.generate_questions(
        request
    )

@router.post(
    "/summary",
    response_model=SummaryResponse
)
def generate_candidate_summary(
    request: SummaryRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = SummaryService(db)

    return service.generate_summary(
        request
    )