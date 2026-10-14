from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Cat(Base):
    __tablename__ = "cat"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Cat(id={self.id!r}, name={self.name!r}, age={self.age!r})"
