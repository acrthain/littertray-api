from datetime import datetime
from typing import ClassVar

from sqlalchemy import Integer, Float, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from cat import Cat, Base
from sqlalchemy.orm import relationship


class TrayVisit(Base):
    __tablename__ = "tray_visit"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    time: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    visit_type: Mapped[str] = mapped_column(Text)
    cat_weight: Mapped[float] = mapped_column(Float)
    cat_id: Mapped[int] = mapped_column(Integer, ForeignKey("cat.id"))
    cat_name: ClassVar[str]

    # cat: Mapped[Cat] = relationship("Cat")

    def __repr__(self) -> str:
        return f"TrayVisit(id={self.id!r}, time={self.time!r}, visit_type={self.visit_type!r}, cat_weight={self.cat_weight!r}, cat_id={self.cat_id!r})"
