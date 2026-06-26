from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import ForeignKey

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
        unique=True,
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


class Road(Base):

    __tablename__ = "roads"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    source_id = Column(
        Integer,
        ForeignKey("cities.id")
    )

    destination_id = Column(
        Integer,
        ForeignKey("cities.id")
    )

    distance = Column(
        Float,
        nullable=False
    )

    speed_limit = Column(
        Float,
        nullable=False
    )