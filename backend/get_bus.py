import sqlite3
import sys
import datetime

conn = sqlite3.connect("static.db")

c = conn.cursor()

if len(sys.argv) == 2:
    now = str(datetime.datetime.now()).split()[1].split(".")[0].split(":")
    now = datetime.time(int(now[0]), int(now[1]), int(now[2]))
    bus = sys.argv[1]
    c.execute(f"SELECT * FROM routes WHERE route_long_name LIKE '%{bus}%'")
    print(c.fetchall(), "\n \n")
    # c.execute(f"SELECT * FROM trips WHERE route_id = {c.fetchall()[0][1]}")
    # print(c.fetchall(), "\n \n")
    # c.execute(f"SELECT * FROM stop_times WHERE trip_id = '{c.fetchone()[2]}'")
    # print(c.fetchall(), "\n \n")
    data = c.fetchall()
    arrivals = [datas[1] for datas in data]
    # for arrival in arrivals:
    #     arrival = arrival.split(":")
    #     arrival = datetime.time(int(arrival[0]), int(arrival[1]), int(arrival[2]))
    #     if arrival < now:
    #         print(f"{arrival} < {now}")
    #         pass
    #     else:
    #         print(f"Next bus on {arrival}")

elif len(sys.argv) < 2:
    print("add bus code")
elif len(sys.argv) > 2: 
    print("improper bus code")