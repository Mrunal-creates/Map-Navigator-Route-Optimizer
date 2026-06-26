const map = L.map("map").setView(
    [22.5937, 78.9629],
    5
);

L.tileLayer(
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        attribution: "&copy; OpenStreetMap"
    }
).addTo(map);

let polyline = null;
let markers = [];

loadCities();

async function loadCities() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/cities"
        );

        const cities = await response.json();

        const datalist = document.getElementById(
            "cities"
        );

        datalist.innerHTML = "";

        cities.forEach(city => {

            const option = document.createElement(
                "option"
            );

            option.value = city;

            datalist.appendChild(
                option
            );

        });

    }
    catch (error) {

        console.error(error);

        alert(
            "Unable to load cities from server."
        );

    }

}

async function findRoute() {

    const source =
        document.getElementById(
            "source"
        ).value;

    const destination =
        document.getElementById(
            "destination"
        ).value;

    try {

        const response =
            await fetch(
                `http://127.0.0.1:8000/route?source=${source}&destination=${destination}`
            );

        const data =
            await response.json();

        if (data.error) {

            alert(data.error);
            return;
        }

        document.getElementById(
            "result"
        ).innerHTML = `

            <div class="stats-card">

                <h2>
                    Route Statistics
                </h2>

                <p>
                    Distance:
                    ${data.data.distance} km
                </p>

                <p>
                    Travel Time:
                    ${data.data.travel_time} hrs
                </p>

                <p>
                    Cities Traversed:
                    ${data.coordinates.length}
                </p>

                <p>
                    Cache:
                    ${data.cache}
                </p>

            </div>
        `;

        if (polyline) {

            map.removeLayer(
                polyline
            );
        }

        markers.forEach(
            marker =>
                map.removeLayer(marker)
        );

        markers = [];

        const coordinates =
            data.coordinates.map(
                city =>
                    [
                        city.latitude,
                        city.longitude
                    ]
            );

        polyline =
            L.polyline(
                coordinates,
                {
                    weight: 5
                }
            ).addTo(map);

        coordinates.forEach(
            (
                coordinate,
                index
            ) => {

                const city =
                    data.coordinates[index];

                const marker =
                    L.marker(
                        coordinate
                    )
                    .addTo(map)
                    .bindPopup(
                        city.name
                    );

                markers.push(
                    marker
                );
            }
        );

        map.fitBounds(
            polyline.getBounds()
        );

    } catch {

        alert(
            "Route not found."
        );
    }
}