from fastapi import  APIRouter
from pydantic import BaseModel
from models import Users


router = APIRouter()

class CreateUserRequest(BaseModel):
    username : str
    email : str
    first_name : str
    last_name : str
    password : str
    role: str



@router.post('/auth')
async def create_user(create_user_request: CreateUserRequest):
    """
    usually we use 
    
        create_user_model = Users(**create_user_request.model_dump())

    But since in here the password will not be recongnized in the Users Model, bcs there
    we had hashed_password we are individual fields and mapping it to the Users model.

    """


    create_user_model = Users(
        email = create_user_request.email,
        username = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        role = create_user_request.role,
        hashed_password = create_user_request.password,
        is_active = True
    )

    return create_user_model