from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database.db import Base


class Road(Base):
    __tablename__ = "roads"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    source_id = Column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False
    )

    destination_id = Column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False
    )

    distance = Column(
        Float,
        nullable=False
    )

    speed_limit = Column(
        Float,
        nullable=False
    )