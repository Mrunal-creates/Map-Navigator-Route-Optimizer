import time

from app.algorithms.dijkstra import dijkstra
from app.algorithms.astar import astar


class BenchmarkService:

    @staticmethod
    def benchmark(
        graph,
        source,
        destination
    ):

        start = time.perf_counter()

        dijkstra(
            graph,
            source,
            destination
        )

        dijkstra_time = (
            time.perf_counter()
            - start
        )

        start = time.perf_counter()

        astar(
            graph,
            source,
            destination
        )

        astar_time = (
            time.perf_counter()
            - start
        )

        return {

            "dijkstra_ms":
                round(
                    dijkstra_time * 1000,
                    3
                ),

            "astar_ms":
                round(
                    astar_time * 1000,
                    3
                )
        }