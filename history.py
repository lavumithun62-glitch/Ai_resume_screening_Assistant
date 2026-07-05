from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.services.history_service import HistoryService

from app.schemas.history import HistoryResponse

from app.models.user import User

from app.core.security import get_current_user


router = APIRouter(

    prefix="/history",

    tags=["History"]
)


@router.get(
    "/",
    response_model=list[HistoryResponse]
)
def get_history(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )

):

    service = HistoryService(db)

    return service.get_history()