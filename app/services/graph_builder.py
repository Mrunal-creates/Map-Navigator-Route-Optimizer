from collections import defaultdict
from app.models.city import City
from app.database.db import SessionLocal
from app.models.road import Road


def build_graph():
    """
    Build adjacency list graph from PostgreSQL roads table.
    """

    db = SessionLocal()

    try:
        roads = db.query(Road).all()

        graph = defaultdict(list)

        for road in roads:

            graph[road.source_id].append(
                {
                    "destination": road.destination_id,
                    "distance": road.distance,
                    "speed_limit": road.speed_limit
                }
            )

        return graph

    finally:
        db.close()


def get_cities():

    db = SessionLocal()

    cities = db.query(
        City
    ).all()

    db.close()

    return cities