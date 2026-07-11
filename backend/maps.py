import folium
import sqlite3

conn = sqlite3.connect("static.db")
c = conn.cursor()

c.execute("SELECT stop_lat, stop_lon, stop_name FROM stops")
stop_data = c.fetchall()

m = folium.Map(location=(28.683891,77.222282), zoom_start=20)

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

m.save("index.html")

