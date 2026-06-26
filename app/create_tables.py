from app.database.db import Base
from app.database.db import engine

from app.models.city import City
from app.models.road import Road
from app.models.route_history import RouteHistory

Base.metadata.create_all(bind=engine)

print("Tables created successfully")