# openDTC — Live Bus Tracker

Live vehicle tracking for Delhi's public bus network, built on the Open Transit Data (OTD) Delhi GTFS-Realtime feed. Pulls live vehicle positions, converts them to GeoJSON, and renders them on an interactive map that auto-refreshes without a page reload.

How it works


Backend (backend/) — a FastAPI service fetches the GTFS-Realtime VehiclePositions.pb feed, parses the protobuf into vehicle entities, and converts them into a GeoJSON FeatureCollection. Served over a single / endpoint.
Frontend (frontend/) — a Folium map using the Realtime plugin (leaflet-realtime under the hood), which polls the backend on an interval and updates bus markers in place — no flicker, no full re-render. Static bus stops are pulled from a local SQLite database (static.db) and rendered as fixed markers.


Project structure

.
├── backend/
│   ├── main.py              # FastAPI app — GTFS-RT fetch + GeoJSON conversion endpoint
│   ├── get_bus.py            # feed fetching, parsing, GeoJSON conversion logic
│   └── requirements.txt
├── frontend/
│   ├── maps.py                # builds index.html — stops + live Realtime bus layer
│   └── static.db               # GTFS static data 
└── README.md

Setup

Backend

bashcd backend
pip install -r requirements.txt

Create a .env file in backend/ with your OTD Delhi API key:

API_KEY=your_key_here

Run locally:

bashuvicorn main:app --reload --port 8000

Hit http://127.0.0.1:8000/ — should return a GeoJSON FeatureCollection of live vehicle positions.

Frontend

bashcd frontend
python maps.py

This generates index.html with the bus stops layer plus a live-updating vehicle layer pointed at the backend's source URL (update this in maps.py to your deployed API URL once hosted).

Deployment

The backend deploys to Vercel as a Python serverless function (zero-config FastAPI detection — entrypoint is backend/main.py). Set API_KEY as an environment variable in the Vercel project dashboard rather than committing a .env file.

The frontend is a static index.html — host it anywhere that serves static files (Vercel, GitHub Pages, Netlify, etc.), or drop it in a public/ folder alongside the backend for a single deployment.

Data source

GTFS-Realtime feed: Open Transit Data Delhi — requires a free API key.

Notes


Vehicle markers update via polling (default interval: 30s) — tune interval in maps.py to match how often the upstream feed actually refreshes.
Bus stop data (static.db) is static reference data, read-only at runtime.

* This readme was written by AI and the vercel setup was also done with the help of AI I haven't used AI anywhere else