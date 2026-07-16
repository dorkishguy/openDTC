import folium
from folium import JsCode
from folium.plugins import Realtime, MarkerCluster
import sqlite3

def db_get():
    conn = sqlite3.connect("static.db")
    c = conn.cursor()
    c.execute("SELECT stop_lat, stop_lon, stop_name FROM stops")
    return c.fetchall()

def add_to_map(stop_data):

    source = "https://open-dtc-hvvg.vercel.app/"
    m = folium.Map(location=(28.683891,77.222282), zoom_start=12, prefer_canvas=True, tiles='CartoDB positron')
    marker_cluster = MarkerCluster().add_to(m)

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
        get_feature_id=JsCode("""
        (f) => {
            console.log("Feature:", f);
            console.log("ID:", f.properties.id);
            return f.properties.id;
        }
        """),
        point_to_layer=JsCode("""
        (f, latlng) => {
            console.log("Feature:", f);
            console.log("LatLng:", latlng);
            return L.circle(latlng, {
                radius: 2,
                fillOpacity: 1
            });
        }
        """),
        interval=30000,
    ).add_to(marker_cluster)

    m.save("index.html")

def main():
    add_to_map(db_get())

main()
