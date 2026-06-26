import json

from app.cache.redis_client import (
    redis_client
)


class CacheService:

    @staticmethod
    def get_route(
        source,
        destination
    ):

        key = (
            f"route:"
            f"{source}:"
            f"{destination}"
        )

        data = redis_client.get(key)

        if data:
            return json.loads(data)

        return None

    @staticmethod
    def save_route(
        source,
        destination,
        result
    ):

        key = (
            f"route:"
            f"{source}:"
            f"{destination}"
        )

        redis_client.set(
            key,
            json.dumps(result)
        )