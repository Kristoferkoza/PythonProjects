import requests
from datetime import datetime

MY_LAT = 52.746980
MY_LONG = 19.464600

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# response = requests.get(url="http://api.kanye.rest")
# data = response.json()
# print(data)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_hour = datetime.now().hour
print(sunrise)
print(sunset)
print(time_hour)
