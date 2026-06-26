import heapq
import math


def heuristic(
    cities,
    node,
    destination
):

    city1 = cities[node]
    city2 = cities[destination]

    return math.sqrt(
        (city2["latitude"] - city1["latitude"]) ** 2
        +
        (city2["longitude"] - city1["longitude"]) ** 2
    )


def astar(
    graph,
    cities_list,
    source,
    destination
):

    cities = {}

    for city in cities_list:

        cities[city.id] = {
            "name": city.name,
            "latitude": city.latitude,
            "longitude": city.longitude
        }

    open_set = []

    heapq.heappush(
        open_set,
        (0, source)
    )

    g_score = {
        node: float("inf")
        for node in cities.keys()
    }

    previous = {
        node: None
        for node in cities.keys()
    }

    g_score[source] = 0

    while open_set:

        current_f, current = heapq.heappop(
            open_set
        )

        if current == destination:
            break

        for edge in graph.get(
            current,
            []
        ):

            neighbor = edge["destination"]

            tentative = (
                g_score[current]
                +
                edge["distance"]
            )

            if tentative < g_score[neighbor]:

                g_score[neighbor] = tentative

                previous[neighbor] = current

                f_score = (
                    tentative
                    +
                    heuristic(
                        cities,
                        neighbor,
                        destination
                    )
                )

                heapq.heappush(
                    open_set,
                    (
                        f_score,
                        neighbor
                    )
                )

    path = []

    current = destination

    while current is not None:

        path.append(current)

        current = previous[current]

    path.reverse()

    city_names = [
        cities[node]["name"]
        for node in path
    ]

    return {
        "path": city_names,
        "distance": round(
            g_score[destination],
            2
        )
    }