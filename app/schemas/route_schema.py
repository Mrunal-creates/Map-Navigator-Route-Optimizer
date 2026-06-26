from pydantic import BaseModel


class RouteResponse(BaseModel):

    path: list[str]
    distance: float
    travel_time: float