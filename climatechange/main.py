from distutils.log import debug
from posixpath import split
from flask import Flask, render_template, request, send_from_directory
import base64
from github import Github
import requests
from flask import Markup
import gunicorn
import requests
import json

import os
from flask import Flask,render_template,request,redirect
import smtplib, ssl
from flask_mail import Mail, Message
import json
from ast import literal_eval
#defining flask name
app = Flask(__name__)


#Defining home page(index.html)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aqi', methods = ['POST', 'GET'])
def repo():
    if request.method == 'POST':
        name_of_country = request.form['name']
        return redirect(f"/country/{name_of_country}")

#Defining repo function for returning data
@app.route('/country/<name_of_country>')
def users(name_of_country):
    
    name_of_country_clarified = name_of_country.lower() 
    latitude = {'afghanistan':'33.93911', 'united states':'37.09024','united kingdom':'55.378051','pakistan':'30.375321', 'mexico':'23.634501'}
    longtitude = {'afghanistan':'67.709953','united states':'-95.712891','united kingdom':'-3.435973','pakistan':'69.345116', 'mexico':'-102.552784'}

    population = {'united states':'329.5 million','africa':'1.216 billion','afghanistan':'38.93 million','pakistan':'220.9 million','mexico':'128.9 million','russia':'144.1 million','germany':'83.24 million','ukraine':'44.13 million','china':'1.402 billion','india':'1.38 billion','saudi arabia':'34.81 million','iran':'83.99 million','turkey':'84.34 million','iraq':'40.22 million','poland':'37.95 million','sweden':'10.35 million','finland':'5.531 million','norway':'5.379 million','france':'67.39 million','italy':'59.55 million','spain':'47.35 million','portugal':'10.31 million','brazil':'212.6 million','united kingdom':'67.22 million'}
    #3725
    c = population[name_of_country_clarified]
    response = requests.get(f'https://api.waqi.info/feed/{name_of_country}/?token=xxxxx')

    countryone = latitude[name_of_country_clarified]

    countrytwo = longtitude[name_of_country_clarified]
    response_two = requests.get(f'https://api.weatherbit.io/v2.0/current?lat={countryone}&lon={countrytwo}&key=xxxxxx&include=minutely')
    json_data_threee = response_two.json()

    aw = (json_data_threee["data"]["weather"]["description"])
    print(aw)
    json_data = response.json()
    print(json_data)

    b = (json_data["data"]["aqi"])
    
    return render_template("countryreturn.html", splits = Markup(f'AQI: {b}<br>Population: {c}<br>Weather: {aw} ')
)


#Noise pollution 
#Amount of power plants in country
#Average weather

if __name__ == "__main__":
    app.run(debug=True)