from insurance_app.database import SessionLocal

from insurance_app.models.models import User

from passlib.context import CryptContext

 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

 

def create_test_user():

    db = SessionLocal()

    username = "testuser"

    password = "testpass"

    hashed_password = pwd_context.hash(password)

    role = "admin"

    email = "testuser@example.com"

    status = "Active"

 

    # Check if user already exists

    user = db.query(User).filter(User.username == username).first()

    if not user:

        user = User(

            username=username,

            password_hash=hashed_password,

            role=role,

            email=email,

            status=status

        )

        db.add(user)

        db.commit()

        print("Test user created.")

    else:

        print("Test user already exists.")

    db.close()

 

if __name__ == "__main__":

    create_test_user()

