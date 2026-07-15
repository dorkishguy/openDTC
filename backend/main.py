from get_bus import get_pb, get_data, convert_to_geojson
from maps import db_get, add_to_map

geojson = convert_to_geojson(get_data(get_pb()))
add_to_map(db_get())