from datetime import datetime

from app.database.db import SessionLocal
from app.models.route_history import RouteHistory


class HistoryService:

    @staticmethod
    def save_route(
        source_id,
        destination_id,
        algorithm,
        distance
    ):

        db = SessionLocal()

        try:

            route = RouteHistory(
                source_id=source_id,
                destination_id=destination_id,
                algorithm=algorithm,
                distance=distance,
                created_at=datetime.utcnow()
            )

            db.add(route)

            db.commit()

        except Exception as e:

            db.rollback()

            print("History Error:", e)

        finally:

            db.close()