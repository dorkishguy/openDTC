from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests
import sys
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_pb():
    r = requests.get(f'https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key={API_KEY}')
    print("downloaded")
    with open("data.pb", "wb") as file:
        file.write(r.content)
    print("saved")

def get_data():
    get_pb()
    data = []
    with open("data.pb", "rb") as file:
        response = file.read()
    feed = gtfs_realtime_pb2.FeedMessage()
    response = feed.ParseFromString(response)
    for entity in feed.entity:
        entity_data = MessageToDict(entity)
        data.append(entity_data)
    print(data)

get_data()