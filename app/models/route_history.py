from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class RouteHistory(Base):

    __tablename__ = "route_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    source_id = Column(
        Integer,
        nullable=False
    )

    destination_id = Column(
        Integer,
        nullable=False
    )

    algorithm = Column(
        String,
        nullable=False
    )

    distance = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )