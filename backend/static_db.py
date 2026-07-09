import sqlite3
import csv

conn = sqlite3.connect("static.db")

c = conn.cursor()

# c.execute("""CREATE TABLE trips (
#           route_id integer,
#           service_id integer,
#           trip_id text,
#           shape_id null)""")

# with open("/home/dorkishguy/projects/Public-transport/bus/trips.txt", "r") as file:
#     routes = csv.DictReader(file)
#     insertions = [(row['route_id'], row['service_id'], row['trip_id'], row['shape_id'])
#                   for row in routes]
#     c.executemany(f"INSERT INTO trips VALUES (?, ?, ?, ?)", insertions)

# c.execute("SELECT * FROM trips;")
# print(c.fetchmany(5))

c.execute("SELECT COUNT(*) FROM trips;")
row_count = c.fetchone()
print(row_count)

conn.commit()
conn.close()