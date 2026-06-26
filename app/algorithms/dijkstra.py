import heapq


def dijkstra(
    graph,
    source,
    destination
):

    distances = {}
    previous = {}
    travel_times = {}

    all_nodes = set()

    for node in graph:

        all_nodes.add(node)

        for edge in graph[node]:

            all_nodes.add(
                edge["destination"]
            )

    for node in all_nodes:

        distances[node] = float("inf")
        previous[node] = None
        travel_times[node] = 0

    distances[source] = 0

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (0, source)
    )

    while priority_queue:

        current_distance, current_node = (
            heapq.heappop(priority_queue)
        )

        if current_node == destination:
            break

        for edge in graph.get(
            current_node,
            []
        ):

            neighbor = edge["destination"]

            distance = edge["distance"]

            speed_limit = edge["speed_limit"]

            new_distance = (
                current_distance
                + distance
            )

            if (
                new_distance
                <
                distances[neighbor]
            ):

                distances[neighbor] = (
                    new_distance
                )

                previous[neighbor] = (
                    current_node
                )

                travel_times[neighbor] = (
                    travel_times[current_node]
                    +
                    (
                        distance
                        /
                        speed_limit
                    )
                )

                heapq.heappush(
                    priority_queue,
                    (
                        new_distance,
                        neighbor
                    )
                )

    if (
        destination not in distances
        or
        distances[destination] == float("inf")
    ):
        return None

    path = []

    current = destination

    while current is not None:

        path.append(current)

        current = previous[current]

    path.reverse()

    return {
        "path": path,
        "distance": round(
            distances[destination],
            2
        ),
        "travel_time": round(
            travel_times[destination],
            2
        )
    }