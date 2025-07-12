from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import re


requested = requests.get("https://www.scrapethissite.com/pages/simple/")

conn = BeautifulSoup(requested.text, "html.parser")

title = conn.find("p", class_="lead")
fixed_title = re.sub(r'\n \s+','',title.text)

country_n = conn.find_all("h3", class_="country-name")
country_d = conn.find_all("div", class_="country-info")

listed_info = []
listed_info.append(fixed_title)


for x, z in zip(country_n, country_d):
    text_n = x.text
    text_d = z.text

    split_n = text_n.split()
    split_d = text_d.split()

    fixed_n = re.sub(r'\s+', '', text_n)

    l1 = [split_d[0], split_d[1]]
    j1 = " ".join(l1)

    l2 = [split_d[2], split_d[3]]
    j2 = " ".join(l2)

    l3 = [split_d[4], split_d[5], split_d[6]]
    j3 = " ".join(l3)
    
    listed_info.append((fixed_n, j1, j2, j3))

print(listed_info)

app = Flask(__name__)

API_KEY = "20020227"
WEATHER_KEY = "tumbatumba"
key = ""

@app.route("/")
def home():
    return jsonify("webpage working.")

@app.route("/cities")
def city():
    key = request.args.get("api-key")
    if key != API_KEY:
        return jsonify({"error": "Wrong key."}, 401)
    else:
        return jsonify(listed_info)
    

@app.route("/weather")
def weather():
    w_key = request.args.get('weather-api')
    if w_key != WEATHER_KEY:
        return jsonify({"error": "Wrong api key."})
    else:
        vilnius = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Vilnius&appid={key}")
        return jsonify(vilnius.json())

app.run(debug=True)
