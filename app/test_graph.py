from graph.models import Graph

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

graph.add_bidirectional_edge(
    1,
    2,
    150,
    80
)

graph.add_bidirectional_edge(
    1,
    3,
    210,
    70
)

graph.display()