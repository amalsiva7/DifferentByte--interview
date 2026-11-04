from fastapi import APIRouter, status, Depends, HTTPException
from app.schemas.users import UserResponse, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.crud.users import crud_user

router = APIRouter(prefix="/user", tags=["User"])


@router.post(
    "/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def create_user(data: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        username, email, pw = data.username, data.email, data.password
        data = UserCreate(username=username, email=email, password=hash(pw))
        return await crud_user.create(db=db, object=data)
    except Exception as e:
        raise HTTPException(detail=f"{e}", status_code=status.HTTP_409_CONFLICT)
