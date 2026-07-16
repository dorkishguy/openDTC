# openDTC — Live Delhi Bus Tracker

Live vehicle tracking for Delhi's public bus network, built on the [Open Transit Data (OTD) Delhi](https://otd.delhi.gov.in/) GTFS-Realtime feed. Pulls live vehicle positions, converts them to GeoJSON, and renders them on an interactive map that auto-refreshes without a page reload.

## How it works

**Backend** (`backend/`) — a FastAPI service fetches the GTFS-Realtime `VehiclePositions.pb` feed, parses the protobuf into vehicle entities, and converts them into a GeoJSON `FeatureCollection`. Served over a single `/` endpoint.

**Frontend** (`frontend/`) — a Folium map using the [Realtime plugin](https://github.com/python-visualization/folium) (leaflet-realtime under the hood), which polls the backend on an interval and updates bus markers in place — no flicker, no full re-render. Static bus stops are pulled from a local SQLite database (`static.db`) and rendered as fixed markers.

All "live" behavior is client-side: once `index.html` loads, the browser polls the backend directly via JS. This means the frontend can be hosted anywhere that serves static files, independent of the backend.

## Project structure

```
.
├── backend/
│   ├── main.py            # FastAPI app — GTFS-RT fetch + GeoJSON conversion endpoint
│   ├── get_bus.py         # feed fetching, parsing, GeoJSON conversion logic
│   └── requirements.txt
├── frontend/
│   ├── maps.py             # builds index.html — stops + live Realtime bus layer
│   └── static.db            # GTFS static data (stops)
└── README.md
```

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in `backend/` with your OTD Delhi API key:

```
API_KEY=your_key_here
```

Run locally:

```bash
uvicorn main:app --reload --port 8000
```

Visit `http://127.0.0.1:8000/` — should return a GeoJSON `FeatureCollection` of live vehicle positions.

### Frontend

```bash
cd frontend
python maps.py
```

This generates `index.html` with the bus stops layer plus a live-updating vehicle layer pointed at the backend's source URL. Update the `source` URL in `maps.py` to your deployed API URL before generating.

## Deployment

**Backend** deploys to Vercel as a Python serverless function (zero-config FastAPI detection — entrypoint is `backend/main.py`, Root Directory set to `backend` in project settings). Set `API_KEY` as an environment variable in the Vercel dashboard rather than committing a `.env` file.

**Frontend** is a single static `index.html` — host it anywhere that serves static files:

- **Vercel** — separate project, Root Directory `frontend`, Framework Preset "Other", no build command
- **GitHub Pages** — copy/generate `index.html` into a `docs/` folder at repo root (or use a `gh-pages` branch), then enable Pages on that folder
- **Netlify** or any static host works the same way

Since all live-update logic runs client-side, the frontend's hosting platform has no effect on realtime behavior — the browser just needs to reach the backend, which is why the backend's CORS is set to allow all origins (`allow_origins=["*"]`).

## Data source

GTFS-Realtime feed: [Open Transit Data Delhi](https://otd.delhi.gov.in/) — requires a free API key.

## Notes

- Vehicle markers update via polling (default interval: 30s) — tune this in `maps.py` to match how often the upstream feed actually refreshes.
- Bus stop data (`static.db`) is static reference data, read-only at runtime.
- `index.html` is a generated artifact, not hand-written — regenerate and recommit it whenever stop data or the backend URL changes.

# used ai for this readme and for help with vercel deployment didnt use ai anywhere else

