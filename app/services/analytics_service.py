from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.city import City
from app.models.road import Road


class AnalyticsService:

    @staticmethod
    def get_statistics():

        db: Session = SessionLocal()

        try:

            total_cities = (
                db.query(City)
                .count()
            )

            total_roads = (
                db.query(Road)
                .count()
            )

            roads = (
                db.query(Road)
                .all()
            )

            if roads:

                avg_distance = round(
                    sum(
                        r.distance
                        for r in roads
                    )
                    /
                    len(roads),
                    2
                )

                avg_speed = round(
                    sum(
                        r.speed_limit
                        for r in roads
                    )
                    /
                    len(roads),
                    2
                )

            else:

                avg_distance = 0
                avg_speed = 0

            return {

                "total_cities":
                    total_cities,

                "total_roads":
                    total_roads,

                "average_distance":
                    avg_distance,

                "average_speed_limit":
                    avg_speed
            }

        finally:

            db.close()