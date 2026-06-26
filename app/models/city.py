from sqlalchemy import Column, Integer, String, Float

from app.database.db import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    latitude = Column(
        Float,
        nullable=False
    )

    longitude = Column(
        Float,
        nullable=False
    )