import requests
import smtplib
from datetime import datetime
import math

MY_LAT = 52.746980
MY_LONG = 19.464600
MY_EMAIL = "kristoferkozaczek@gmail.com"
PASSWORD = "ksenfvbwerilujfd"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
is_close = False
# is_close = True
if math.fabs(MY_LAT - iss_latitude) <= 5 and math.fabs(MY_LONG - iss_longitude) <= 5:
    is_close = True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

is_dark = False
# is_dark = True
if time_now.hour > sunset or time_now.hour < sunrise:
    is_dark = True

if is_dark and is_close:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Information\n\nLook Up!"
        )

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
