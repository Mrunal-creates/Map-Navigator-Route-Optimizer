from fastapi import APIRouter

from app.database.db import SessionLocal

from app.models.city import City
from app.models.route_history import RouteHistory

from app.services.graph_builder import (
    build_graph,
    get_cities
)

from app.algorithms.dijkstra import dijkstra
from app.algorithms.astar import astar

from app.services.cache_service import CacheService

from app.services.analytics_service import AnalyticsService
from app.services.benchmark_service import BenchmarkService
from app.services.history_service import HistoryService
from app.services.usage_analytics import UsageAnalytics
from app.services.route_serializer import RouteSerializer
from app.services.city_service import CityService


router = APIRouter()


# ===================================================
# DIJKSTRA
# ===================================================

@router.get("/route")
def get_route(
    source: str,
    destination: str
):

    source_city = CityService.get_city_by_name(source)

    if source_city is None:
        return {
            "success": False,
            "message": f"{source} not found"
        }

    destination_city = CityService.get_city_by_name(destination)

    if destination_city is None:
        return {
            "success": False,
            "message": f"{destination} not found"
        }

    cached = CacheService.get_route(
        source,
        destination
    )

    if cached:

        coordinates = RouteSerializer.serialize(
            cached["path"]
        )

        return {
            "cache": True,
            "message": "Route fetched from cache",
            "data": cached,
            "coordinates": coordinates
        }

    graph = build_graph()

    result = dijkstra(
        graph,
        source_city.id,
        destination_city.id
    )

    if result is None:

        return {
            "success": False,
            "message": "No route found"
        }

    CacheService.save_route(
        source,
        destination,
        result
    )

    HistoryService.save_route(
        source_city.id,
        destination_city.id,
        "dijkstra",
        result["distance"]
    )

    coordinates = RouteSerializer.serialize(
        result["path"]
    )

    return {
        "cache": False,
        "message": "Shortest route found",
        "data": result,
        "coordinates": coordinates
    }


# ===================================================
# ASTAR
# ===================================================

@router.get("/route/astar")
def shortest_route_astar(
    source: str,
    destination: str
):

    source_city = CityService.get_city_by_name(source)

    destination_city = CityService.get_city_by_name(destination)

    if source_city is None:

        return {
            "success": False,
            "message": "Source city not found"
        }

    if destination_city is None:

        return {
            "success": False,
            "message": "Destination city not found"
        }

    graph = build_graph()

    cities = get_cities()

    result = astar(
        graph,
        cities,
        source_city.id,
        destination_city.id
    )

    if result is None:

        return {
            "success": False,
            "message": "No route found"
        }

    HistoryService.save_route(
        source_city.id,
        destination_city.id,
        "astar",
        result["distance"]
    )

    coordinates = RouteSerializer.serialize(
        result["path"]
    )

    return {
        "algorithm": "astar",
        "data": result,
        "coordinates": coordinates
    }


# ===================================================
# ANALYTICS
# ===================================================

@router.get("/analytics")
def analytics():

    return AnalyticsService.get_statistics()


@router.get("/analytics/usage")
def usage():

    return UsageAnalytics.get_stats()


# ===================================================
# HISTORY
# ===================================================

@router.get("/history")
def history():

    db = SessionLocal()

    try:

        routes = db.query(RouteHistory).all()

        result = []

        for route in routes:

            source = (
                db.query(City)
                .filter(City.id == route.source_id)
                .first()
            )

            destination = (
                db.query(City)
                .filter(City.id == route.destination_id)
                .first()
            )

            result.append(

                {
                    "id": route.id,
                    "source": source.name if source else "",
                    "destination": destination.name if destination else "",
                    "algorithm": route.algorithm,
                    "distance": route.distance,
                    "created_at": route.created_at
                }

            )

        return result

    finally:

        db.close()


# ===================================================
# BENCHMARK
# ===================================================

@router.get("/benchmark")
def benchmark(
    source: str,
    destination: str
):

    graph = build_graph()

    return BenchmarkService.benchmark(
        graph,
        source,
        destination
    )


# ===================================================
# CITIES
# ===================================================

@router.get("/cities")
def cities():

    city_list = CityService.get_all_cities()

    return [

        city.name

        for city in city_list

    ]


# ===================================================
# DEBUG GRAPH
# ===================================================

@router.get("/debug/graph")
def debug():

    return build_graph()