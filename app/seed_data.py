from math import radians, sin, cos, sqrt, atan2

from app.database.db import SessionLocal
from app.models.city import City
from app.models.road import Road

db = SessionLocal()


def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return round(R * c, 2)


try:

    print("Deleting old data...")

    db.query(Road).delete()
    db.query(City).delete()

    db.commit()

    cities = [

        City(id=1, name="Mumbai", latitude=19.0760, longitude=72.8777),
        City(id=2, name="Delhi", latitude=28.6139, longitude=77.2090),
        City(id=3, name="Bangalore", latitude=12.9716, longitude=77.5946),
        City(id=4, name="Hyderabad", latitude=17.3850, longitude=78.4867),
        City(id=5, name="Chennai", latitude=13.0827, longitude=80.2707),
        City(id=6, name="Kolkata", latitude=22.5726, longitude=88.3639),
        City(id=7, name="Pune", latitude=18.5204, longitude=73.8567),
        City(id=8, name="Ahmedabad", latitude=23.0225, longitude=72.5714),
        City(id=9, name="Jaipur", latitude=26.9124, longitude=75.7873),
        City(id=10, name="Lucknow", latitude=26.8467, longitude=80.9462),
        City(id=11, name="Kanpur", latitude=26.4499, longitude=80.3319),
        City(id=12, name="Nagpur", latitude=21.1458, longitude=79.0882),
        City(id=13, name="Indore", latitude=22.7196, longitude=75.8577),
        City(id=14, name="Bhopal", latitude=23.2599, longitude=77.4126),
        City(id=15, name="Patna", latitude=25.5941, longitude=85.1376),
        City(id=16, name="Surat", latitude=21.1702, longitude=72.8311),
        City(id=17, name="Vadodara", latitude=22.3072, longitude=73.1812),
        City(id=18, name="Rajkot", latitude=22.3039, longitude=70.8022),
        City(id=19, name="Nashik", latitude=19.9975, longitude=73.7898),
        City(id=20, name="Aurangabad", latitude=19.8762, longitude=75.3433),
        City(id=21, name="Chandigarh", latitude=30.7333, longitude=76.7794),
        City(id=22, name="Amritsar", latitude=31.6340, longitude=74.8723),
        City(id=23, name="Ludhiana", latitude=30.9000, longitude=75.8573),
        City(id=24, name="Dehradun", latitude=30.3165, longitude=78.0322),
        City(id=25, name="Shimla", latitude=31.1048, longitude=77.1734),
        City(id=26, name="Agra", latitude=27.1767, longitude=78.0081),
        City(id=27, name="Varanasi", latitude=25.3176, longitude=82.9739),
        City(id=28, name="Prayagraj", latitude=25.4358, longitude=81.8463),
        City(id=29, name="Noida", latitude=28.5355, longitude=77.3910),
        City(id=30, name="Meerut", latitude=28.9845, longitude=77.7064)

    ]

    db.add_all(cities)
    db.commit()

    roads = []

    # Connect each city to 8 nearest cities
    for city in cities:

        distances = []

        for other in cities:

            if city.id == other.id:
                continue

            distance = haversine(
                city.latitude,
                city.longitude,
                other.latitude,
                other.longitude
            )

            distances.append(
                (
                    distance,
                    other
                )
            )

        distances.sort(
            key=lambda x: x[0]
        )

        for distance, neighbor in distances[:8]:

            roads.append(
                Road(
                    source_id=city.id,
                    destination_id=neighbor.id,
                    distance=distance,
                    speed_limit=80
                )
            )

            roads.append(
                Road(
                    source_id=neighbor.id,
                    destination_id=city.id,
                    distance=distance,
                    speed_limit=80
                )
            )

    major_routes = [

        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 6),
        (2, 21),
        (2, 9),
        (3, 5),
        (3, 4),
        (4, 12),
        (6, 15),
        (15, 27),
        (12, 7),
        (8, 16),
        (8, 17),
        (13, 14),
        (21, 22),
        (21, 23)

    ]

    for source_id, destination_id in major_routes:

        source = next(
            city for city in cities
            if city.id == source_id
        )

        destination = next(
            city for city in cities
            if city.id == destination_id
        )

        distance = haversine(
            source.latitude,
            source.longitude,
            destination.latitude,
            destination.longitude
        )

        roads.append(
            Road(
                source_id=source_id,
                destination_id=destination_id,
                distance=distance,
                speed_limit=100
            )
        )

        roads.append(
            Road(
                source_id=destination_id,
                destination_id=source_id,
                distance=distance,
                speed_limit=100
            )
        )

    db.add_all(roads)
    db.commit()

    print(f"{len(cities)} cities inserted")
    print(f"{len(roads)} roads inserted")
    print("Seed completed successfully")

except Exception as e:

    db.rollback()
    print(f"Error: {e}")

finally:

    db.close()