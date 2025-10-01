from sqlalchemy.orm import Session

from insurance_app.models.user import User

from insurance_app.schemas.user_schema import UserCreate, UserUpdate

import uuid

from passlib.context import CryptContext

 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

 

class UserService:

    def __init__(self, db: Session):

        self.db = db

 

    def create_user(self, user_data: UserCreate) -> User:

        hashed_password = pwd_context.hash(user_data.password)

        user = User(

            id=uuid.uuid4(),

            username=user_data.username,

            email=user_data.email,

            role=user_data.role,

            status=user_data.status,

            password_hash=hashed_password

        )

        self.db.add(user)

        self.db.commit()

        self.db.refresh(user)

        return user

 

    def get_all_users(self):

        return self.db.query(User).all()

 

    def get_user_by_id(self, user_id: uuid.UUID):

        return self.db.query(User).filter(User.id == user_id).first()

 

    def update_user(self, user_id: uuid.UUID, user_data: UserUpdate):

        user = self.get_user_by_id(user_id)

        if not user:

            return None

        update_data = user_data.dict(exclude_unset=True)

        if "password" in update_data and update_data["password"]:

            update_data["password_hash"] = pwd_context.hash(update_data.pop("password"))

        for field, value in update_data.items():

            setattr(user, field, value)

        self.db.commit()

        self.db.refresh(user)

        return user

 

    def delete_user(self, user_id: uuid.UUID):

        user = self.get_user_by_id(user_id)

        if user:

            self.db.delete(user)

            self.db.commit()

