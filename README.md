# OpenDTC - A live bus tracker for all of Delhi's buses.

This is OpenDTC, a live bus tracker for Delhi's buses. It works by taking the stops from the static data and the buses from a geojson api made by me. The static files and Realtime API was taken from the Open Transit Data provided by the Delhi government
# How it works
- Backend
It queries the Realtime API of Delhi's GTFS system and gets a protobuf file. It converts that protobuf into GeoJSON and exposes it on a FastAPI api endpoint hosted on vercel. 
- Frontend
A Folium map using the Realtime plugin which queries the backend API for the bus co-ordinates and displays them in the map as blue dots and gets the stops from the static db and displays them on the map together.
All "live" behavior is client-side: once index.html loads, the browser polls the backend directly via JS. This means the frontend can be hosted anywhere that serves static files, independent of the backend.
# Project structure
```
.
├── backend/
│   ├── main.py            # FastAPI app — GTFS-RT fetch + GeoJSON conversion endpoint
│   ├── get_bus.py         # feed fetching, parsing, GeoJSON conversion logic
│   └── requirements.txt
├── frontend/
│   ├── maps.py             # builds index.html — stops + live Realtime bus layer
├── docs/
│   ├── index.html # to host on GitHub pages 
│   └── static.db            # GTFS static data (stops)
└── README.md
```
# Setup
Backend
```
cd backend
pip install -r requirements.txt
```
Create a .env file in backend/ with your OTD Delhi API key
```
API_KEY=your-api-key
```
Run locally:
```
uvicorn main:app --reload --port 8000
```
Visit http://127.0.0.1:8000/ — should return a GeoJSON FeatureCollection of live vehicle positions.
Frontend 
```
cd frontend
python maps.py
```
# deploying
- backend
The ``/backend`` folder has a vercel.json to make it easy to deploy on  vercel
- frontend
move the ``index.html`` to ``/docs`` and host on github pages
