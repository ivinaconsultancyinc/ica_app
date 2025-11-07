from sqlalchemy.orm import Session

from database import SessionLocal  # Adjust import if needed

from models.user import User      # Adjust import if needed

from schemas.user_schema import UserCreate  # Adjust import if needed

from user_service import UserService        # Adjust import if needed

 

# Initialize database session

db: Session = SessionLocal()

 

# Create user service instance

user_service = UserService(db)

 

# Define initial users

initial_users = [

    UserCreate(username="admin", email="admin@example.com", password="admin123", role="admin"),

    UserCreate(username="user1", email="user1@example.com", password="password1", role="user"),

    UserCreate(username="user2", email="user2@example.com", password="password2", role="user")

]

 

# Seed users into the database

for user_data in initial_users:

    existing_user = db.query(User).filter_by(username=user_data.username).first()

    if not existing_user:

        user_service.create_user(user_data)

 

# Close the session

db.close()

 

print("Initial users have been successfully added to the database.")

 
