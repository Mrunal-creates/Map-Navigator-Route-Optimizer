from app.database.db import SessionLocal
from app.models.city import City


class RouteSerializer:

    @staticmethod
    def serialize(path):

        db = SessionLocal()

        try:

            result = []

            for city_id in path:

                city = (
                    db.query(City)
                    .filter(
                        City.id == city_id
                    )
                    .first()
                )

                if city:

                    result.append(
                        {
                            "id": city.id,
                            "name": city.name,
                            "latitude": city.latitude,
                            "longitude": city.longitude
                        }
                    )

            return result

        finally:

            db.close()