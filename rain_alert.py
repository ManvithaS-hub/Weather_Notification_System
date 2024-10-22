import os
import requests
from twilio.rest import Client

# Fetch credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
LATITUDE = 13.063093
LONGITUDE = 77.575824
api_key = os.getenv('OWM_API_KEY')

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_param = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_param)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if int(condition_data) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, Remember to bring ☂️",
        from_='+19093262171',
        to='MY_PHONE_NUM'
    )
    print(message.status)
