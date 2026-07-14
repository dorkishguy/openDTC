import folium
from folium import JsCode
from folium.plugins import Realtime
import sqlite3
from get_bus import get_data

conn = sqlite3.connect("static.db")
c = conn.cursor()

c.execute("SELECT stop_lat, stop_lon, stop_name FROM stops")
stop_data = c.fetchall()

source = "http://127.0.0.1:8000"

m = folium.Map(location=(28.683891,77.222282), zoom_start=12)

for stop in stop_data:
    folium.Circle(
    location=[stop[0], stop[1]],
    color="black",
    radius=2,
    weight=1,
    fill_opacity=1,
    opacity=1,
    fill_color="green",
    popup=stop[2].format(1),
    ).add_to(m)
    print(f"Done with {stop[2]}")

Realtime(
    source,
    get_feature_id=JsCode("(f) => { return f.properties.id }"),
    point_to_layer=JsCode("(f, latlng) => { return L.circleMarker(latlng, {radius: 8, fillOpacity: 0.2})}"),
    interval=30000,
).add_to(m)

m.save("index.html")

