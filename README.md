# Smart Route Navigator

## Overview

Smart Route Navigator is a route planning application that calculates the shortest path between cities using graph-based pathfinding algorithms. The project demonstrates how routing systems can be built by representing cities as graph nodes and road connections as weighted edges.

The application provides a REST API built with FastAPI, stores city and road data in PostgreSQL, uses Redis for caching frequently requested routes, and displays routes on an interactive map using Leaflet.js.

---

## Features

* Calculate the shortest route between two cities using Dijkstra's Algorithm.
* Compute routes using the A* Algorithm for comparison.
* Interactive map visualization of the calculated route.
* Route history storage in PostgreSQL.
* Redis-based caching for faster repeated requests.
* Benchmark endpoint for comparing routing algorithms.
* REST APIs with Swagger documentation.
* Dynamic city selection from the available dataset.

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Redis

### Frontend

* HTML
* CSS
* JavaScript
* Leaflet.js

### Algorithms

* Dijkstra's Algorithm
* A* Search Algorithm

---

## Project Structure

```text
SmartRouteNavigator/
│
├── app/
│   ├── algorithms/
│   ├── api/
│   ├── config/
│   ├── database/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── frontend/
├── requirements.txt
├── seed_data.py
└── README.md
```

---

## How It Works

1. The user selects a source and destination city.
2. The backend checks Redis to determine whether the requested route has already been calculated.
3. If a cached route exists, it is returned immediately.
4. Otherwise, the application builds a graph from the road network stored in PostgreSQL.
5. Dijkstra's Algorithm or A* computes the shortest route.
6. The computed result is stored in Redis for future requests and saved in the route history.
7. The frontend displays the route, distance, estimated travel time, and the cities along the path on an interactive map.

---

## API Endpoints

| Method | Endpoint           | Description                                        |
| ------ | ------------------ | -------------------------------------------------- |
| GET    | `/route`           | Find the shortest route using Dijkstra's Algorithm |
| GET    | `/route/astar`     | Find the shortest route using A*                   |
| GET    | `/cities`          | Retrieve the list of available cities              |
| GET    | `/analytics`       | View routing statistics                            |
| GET    | `/analytics/usage` | View usage analytics                               |
| GET    | `/benchmark`       | Compare algorithm performance                      |
| GET    | `/history`         | Retrieve previously searched routes                |

---

## Running the Project

### Backend

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

Start a local server inside the frontend directory.

For example:

```bash
python -m http.server 5500
```

Or use the **Live Server** extension in Visual Studio Code.

---

## Future Improvements

* Integration with live traffic data.
* Turn-by-turn navigation support.
* Route optimization based on traffic conditions.
* User authentication and saved routes.
* Support for multiple transportation modes.
* Larger road network and city dataset.

---

## Author

**Mrunal Parashar**


<img width="1896" height="968" alt="image" src="https://github.com/user-attachments/assets/ffa78e4e-93ae-4c23-af39-209fc7d1d0b2" />

<img width="1907" height="967" alt="image" src="https://github.com/user-attachments/assets/41d00ba9-2090-4865-8334-68e25dc3b6f7" />

<img width="1895" height="977" alt="image" src="https://github.com/user-attachments/assets/c611ff78-c82e-4210-968f-19b23a32ffd8" />

<img width="1902" height="971" alt="image" src="https://github.com/user-attachments/assets/42974e99-a171-4bdf-bf53-e978d9b0bff4" />

<img width="1902" height="977" alt="image" src="https://github.com/user-attachments/assets/6a166b5b-4a51-47d1-bbdb-7d1952224558" />

<img width="1908" height="971" alt="image" src="https://github.com/user-attachments/assets/3d648da5-2f07-47bb-9849-5e90c8cd9bfb" />

<img width="1897" height="988" alt="image" src="https://github.com/user-attachments/assets/35b27442-eb05-4c36-8030-2a6968d440a3" />






