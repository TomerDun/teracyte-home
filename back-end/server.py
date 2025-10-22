from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session


from database import engine, Base, get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
from core.security import get_password_hash


from routers import auth as auth_router
from routers import image_data as image_data_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Teracyte Home API",
    description="Backend API for Teracyte Home application",
    version="1.0.0"
)


api_router = APIRouter(prefix="/api")

# CORS
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api_router.get("/")
async def root():    
    return {        
        "status": "running",        
    }


# Database test endpoint
@api_router.get("/db-test")
async def db_test(db: Session = Depends(get_db)):
    """Test database connection and return user count"""
    try:
        user_count = db.query(User).count()
        return {
            "status": "success",
            "message": "Database connected successfully",
            "users_count": user_count
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# Test endpoint to create a user (for testing only)
@api_router.post("/test-create-user", response_model=UserResponse)
async def test_create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """Test endpoint to create a user (should be replaced with proper auth)"""
    # Check if user exists
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        return {"error": "User already exists"}
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        username=user_data.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


# Include routers
api_router.include_router(auth_router.router)
api_router.include_router(image_data_router.router)

# Include the API router in the app
app.include_router(api_router)

# Mount static files directory to serve images
app.mount("/static", StaticFiles(directory="static"), name="static")
