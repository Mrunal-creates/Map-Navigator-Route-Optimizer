from app.graph.models import Graph
from app.algorithms.dijkstra import Dijkstra
from app.algorithms.astar import astar
from app.services.graph_builder import GraphBuilder

class RouteService:

    def __init__(self):

        self.graph = (
            GraphBuilder.build_graph()
        )

        self.dijkstra = Dijkstra(
            self.graph
        )

        self.astar = astar(
            self.graph
        )


    def get_node_id_by_name(
        self,
        city_name: str
    ):

        for node_id, node in self.graph.nodes.items():

            if node.name.lower() == city_name.lower():

                return node_id

        return None

    def find_route(
        self,
        source: str,
        destination: str
    ):

        source_id = self.get_node_id_by_name(
            source
        )

        destination_id = self.get_node_id_by_name(
            destination
        )

        if source_id is None:
            raise ValueError(
                f"Unknown city: {source}"
            )

        if destination_id is None:
            raise ValueError(
                f"Unknown city: {destination}"
            )

        return self.dijkstra.shortest_path(
            source_id,
            destination_id
        )

    def find_route_astar(
        self,
        source,
        destination
    ):

        source_id = self.get_node_id_by_name(
            source
        )

        destination_id = self.get_node_id_by_name(
            destination
        )

        return self.astar.shortest_path(
            source_id,
            destination_id
        )