import json
from fastapi import FastAPI
from get_bus import get_pb, get_data, convert_to_geojson
app = FastAPI()


@app.get("/")
def get_bus_data():
    get_pb()
    data = convert_to_geojson(get_data())
    return data