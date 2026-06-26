from app.database.db import SessionLocal
from app.models.city import City


class CityService:

    @staticmethod
    def get_city_by_name(name):

        db = SessionLocal()

        try:

            return (
                db.query(City)
                .filter(
                    City.name.ilike(name)
                )
                .first()
            )

        finally:

            db.close()

    @staticmethod
    def get_all_cities():

        db = SessionLocal()

        try:

            return (
                db.query(City)
                .order_by(
                    City.name
                )
                .all()
            )

        finally:

            db.close()