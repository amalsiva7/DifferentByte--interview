from fastcrud import FastCRUD
from app.database.models import User
from app.schemas.users import UserCreate, UserUpdate

CRUDUser = FastCRUD[User, UserCreate, UserUpdate, None, None, None]
crud_user = CRUDUser(User)
