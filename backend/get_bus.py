from google.transit import gtfs_realtime_pb2
import requests
import sys
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

# if len(sys.argv) == 3:
# bus = sys.argv[1]
# stop = sys.argv[2]
feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(f'https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key={API_KEY}')
response = feed.ParseFromString(response.content)
print(response)
for entity in feed.entity:
  print(entity)


# elif len(sys.argv) < 3:
#     print("add bus code")
# elif len(sys.argv) == 2: 
#     print("add stop name")
# elif len(sys.argv) == 1:
#     print("add bus code and stop")