import urllib.request as request
import json

url_1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url_2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

with request.urlopen(url_1) as response1:
    data1 = json.load(response1)

with request.urlopen(url_2) as response2:
    data2 = json.load(response2)

spot_list = data1["data"]["results"]
mrt_list = data2["data"]

with open("spot.csv", "w", encoding="utf-8") as file:
    for spot in spot_list:
        img_url = spot["filelist"]
        splitHttp = img_url.split("" + "https://")
        firstPic = "https://" + splitHttp[1]
        # spot_seriel = spot["SERIAL_NO"]

        for mrt in mrt_list:
            if mrt["SERIAL_NO"] == spot["SERIAL_NO"]:
                mrt_address = mrt["address"].split("" + "  ")
        file.write(spot["stitle"] + ", " + mrt_address[1][0:3] + ", " +
                   spot["longitude"] + ", " + spot["latitude"] + ", " +
                   firstPic + "\n")

mrt_to_spots = {}

for mrt in mrt_list:
    mrt_value = mrt["MRT"]
    if mrt_value not in mrt_to_spots:
        mrt_to_spots[mrt_value] = []

    for spot in spot_list:
        if spot["SERIAL_NO"] == mrt["SERIAL_NO"]:
            mrt_to_spots[mrt_value].append(spot["stitle"])

with open("mrt.csv", "w", encoding="utf-8") as file:
    for mrt, spots in mrt_to_spots.items():
        spots_str = ", ".join(spots)
        file.write(f"{mrt}, {spots_str}\n")
