from graph.models import Graph
from algorithms.dijkstra import Dijkstra


graph = Graph()


graph.add_node(
    1,
    "Pune",
    18.5204,
    73.8567
)

graph.add_node(
    2,
    "Mumbai",
    19.0760,
    72.8777
)

graph.add_node(
    3,
    "Nashik",
    19.9975,
    73.7898
)

graph.add_node(
    4,
    "Aurangabad",
    19.8762,
    75.3433
)

graph.add_node(
    5,
    "Nagpur",
    21.1458,
    79.0882
)


graph.add_bidirectional_edge(
    1,
    2,
    150,
    80
)

graph.add_bidirectional_edge(
    2,
    3,
    170,
    80
)

graph.add_bidirectional_edge(
    3,
    4,
    180,
    80
)

graph.add_bidirectional_edge(
    4,
    5,
    480,
    80
)


graph.add_bidirectional_edge(
    1,
    5,
    1200,
    80
)


dijkstra = Dijkstra(graph)

result = dijkstra.shortest_path(
    source=1,
    destination=5
)

print("\nShortest Path Result\n")

print(
    "Route:",
    result["path"]
)

print(
    "Distance:",
    result["distance"],
    "km"
)