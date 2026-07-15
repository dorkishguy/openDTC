from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
from dotenv import load_dotenv
import requests
import requests
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_pb():
    r = requests.get(f'https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key={API_KEY}')
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(r.content)
    return feed

def get_data(feed):
    data = []
    for entity in feed.entity:
        entity_data = MessageToDict(entity)
        data.append(entity_data)
    return data

def convert_to_geojson(datas):
    geojson = {"type": "FeatureCollection", "features": []}
    for data in datas:
        feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [data["vehicle"]["position"]['longitude'], data["vehicle"]["position"]['latitude']]
        },
        "properties": {
            "id": data["id"]
        }
    }
        geojson["features"].append(feature)
    return geojson
    
def main():
    data = get_pb()
    data = convert_to_geojson(get_data(data))
    print(data)

if __name__ == "__main__":
    main()