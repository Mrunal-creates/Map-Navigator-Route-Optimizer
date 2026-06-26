from sqlalchemy import func

from app.database.db import SessionLocal

from app.models.route_history import (
    RouteHistory
)


class UsageAnalytics:

    @staticmethod
    def get_stats():

        db = SessionLocal()

        total_requests = db.query(
            RouteHistory
        ).count()

        avg_distance = db.query(
            func.avg(
                RouteHistory.distance
            )
        ).scalar()

        db.close()

        return {
            "total_requests":
                total_requests,

            "average_distance":
                round(
                    avg_distance or 0,
                    2
                )
        }