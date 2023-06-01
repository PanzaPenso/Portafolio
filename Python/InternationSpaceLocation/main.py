import requests
from datetime import datetime

MY_LAT = 52.520008
MY_LNG = 13.404954

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])
#print(iss_longitude, "---")
#print(iss_latitude, "****")

def compare_positions():
    # print(iss_latitude - 5)
    # print(iss_latitude + 5)
    # print(iss_longitude - 5)
    # print(iss_longitude + 5)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        if MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
            return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunrise_min = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
sunset_min = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# print(time_now.hour)
# print(time_now.minute)

def compare_times():
    if time_now.hour <= 23:
        if time_now.hour >= sunset_hour:
            print("mira pa arriba ome")
    elif time_now.hour >= 0:
        if time_now.hour < sunrise_hour:
            print("mira pa arriba ome que sigue de dia")
    else:
        print("no es de noche deja de joder")


if compare_positions():
    compare_times()
else:
    print("esa monda ni esta cerca")

