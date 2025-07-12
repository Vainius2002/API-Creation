import requests

api_key = "20020227"
weather_api = "tumbatumba"
r = requests.get("http://127.0.0.1:5000/cities", params={"api-key": api_key})

print(r.json())

r2 = requests.get("http://127.0.0.1:5000/weather", params={"weather-api": weather_api})

print("\n" * 3)
print(r2.json())
