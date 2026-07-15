from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from get_bus import get_pb, get_data, convert_to_geojson

app = FastAPI()
@app.get("/")
def get_bus_data():
    return convert_to_geojson(get_data(get_pb()))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)