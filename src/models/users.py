from sqlalchemy.orm import Mapped, mapped_column

from base import Base
from src.schemas.users import UserSchema


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
        )
