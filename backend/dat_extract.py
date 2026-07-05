import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_pb():
    r = requests.get(f('https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key=', {API_KEY}))
    with open("data.pb", "wb") as file:
        file.write(r.content)

def main():
    print("Getting realtime data")
    get_pb()
    print("Downloaded")

if __name__ == "__main__":
    main()