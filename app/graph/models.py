from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Node:
    """
    Represents a location/city in the map.
    """

    id: int
    name: str
    latitude: float
    longitude: float


@dataclass
class Edge:
    """
    Represents a road between two locations.
    """

    destination: int
    distance: float
    speed_limit: float

    @property
    def travel_time(self) -> float:
        """
        Returns estimated travel time in hours.

        Formula:
            Time = Distance / Speed
        """

        if self.speed_limit == 0:
            return float("inf")

        return self.distance / self.speed_limit


class Graph:
    """
    Graph implementation using an Adjacency List.

    Example:

    {
        1: [
            Edge(destination=2, distance=150)
        ],

        2: [
            Edge(destination=3, distance=170)
        ]
    }
    """

    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.adj: Dict[int, List[Edge]] = {}

    def add_node(
        self,
        node_id: int,
        name: str,
        latitude: float,
        longitude: float
    ) -> None:
        """
        Add a new location node.
        """

        node = Node(
            id=node_id,
            name=name,
            latitude=latitude,
            longitude=longitude
        )

        self.nodes[node_id] = node

        if node_id not in self.adj:
            self.adj[node_id] = []

    def add_edge(
        self,
        source: int,
        destination: int,
        distance: float,
        speed_limit: float
    ) -> None:
        """
        Adds a road between source and destination.

        Example:

        Pune ----150km---- Mumbai
        """

        edge = Edge(
            destination=destination,
            distance=distance,
            speed_limit=speed_limit
        )

        self.adj[source].append(edge)

    def add_bidirectional_edge(
        self,
        source: int,
        destination: int,
        distance: float,
        speed_limit: float
    ) -> None:
        """
        Adds roads in both directions.

        Pune <----> Mumbai
        """

        self.add_edge(
            source,
            destination,
            distance,
            speed_limit
        )

        self.add_edge(
            destination,
            source,
            distance,
            speed_limit
        )

    def get_neighbors(
        self,
        node_id: int
    ) -> List[Edge]:
        """
        Returns all neighboring roads.
        """

        return self.adj.get(node_id, [])

    def get_node(
        self,
        node_id: int
    ) -> Node:
        """
        Returns a node object.
        """

        return self.nodes.get(node_id)

    def display(self) -> None:
        """
        Prints graph structure.
        Useful for debugging.
        """

        print("\nGraph Structure\n")

        for source, edges in self.adj.items():

            node_name = self.nodes[source].name

            print(f"{node_name} ->")

            for edge in edges:

                destination_name = self.nodes[
                    edge.destination
                ].name

                print(
                    f"   {destination_name}"
                    f" | Distance={edge.distance} km"
                    f" | Speed={edge.speed_limit} km/h"
                )

            print()