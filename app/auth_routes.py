from fastapi import APIRouter,status
from app.database import Session,engine
from app.schemas import SignUpModel
from app.models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash

auth_router=APIRouter(
    prefix='/auth',
    tags=['auth']

)

session=Session(bind=engine)

@auth_router.get('/')
async def hello():
    return {"message": "Hello world1!"}

@auth_router.post('/signup',
    status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpModel):
    """
        ## Create a user
        This requires the following
        ```
            username:int
            email:str
            password:str
            is_staff:bool
            is_active:bool
        ```
    """
    db_email = session.query(User).filter(User.email == user.email).first()
    
    # Nếu email đã tồn tại trong database
    if db_email is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='User with the email already exits'
        )
    
    db_username = session.query(User).filter(User.username == user.username).first()
    
    # Nếu username đã tồn tại trong database
    if db_username is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User with the username already exits"
            )
    
    new_user = User(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff=user.is_staff
    )
    
    session.add(new_user)
    
    session.commit()
    
    return new_user