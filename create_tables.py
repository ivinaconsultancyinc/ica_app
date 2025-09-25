import os

from sqlalchemy import create_engine

from insurance_app.models.models import Base  # Import Base from your models

 

# Use the same database URL as your main app

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./insurance.db")

 

# Fix for PostgreSQL on Render (if needed)

if DATABASE_URL.startswith("postgresql://"):

    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)

 

# Create the engine

engine = create_engine(

    DATABASE_URL,

    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

)

 

def create_tables():

    """Create database tables if they don't exist."""

    try:

        Base.metadata.create_all(bind=engine)

        print("✅ Database tables initialized successfully!")

    except Exception as e:

        print(f"❌ Error initializing database tables: {e}")

 

if __name__ == "__main__":

    create_tables()
