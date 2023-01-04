from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap5
import requests
from pymongo import MongoClient


app= Flask(__name__)
bootstrap = Bootstrap5(app)
client= MongoClient("mongodb+srv://auzair:Pakauzi123@microblogapp.1inbaxm.mongodb.net/test")
app.db= client.Weather

@app.route("/",methods=["POST","GET"])
def run():
    client= MongoClient("mongodb+srv://auzair:Pakauzi123@microblogapp.1inbaxm.mongodb.net/test")
    app.db= client.Weather
    city= request.form.get("citysearch")
    
    url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID=c80be740f2de2ede385a2392ec343830"
    req= requests.get(url).json()
    print(req)
    weatherdata={
            "city": "NULL",
            "Temperature": 0,
            "feelslike": 0,
            "Max": 0,
            "Min":0
            
        }
        
    if request.method=="POST":
        app.db.city.insert_one({"Cityname":city})
        final_city=app.db.city.find({})
        weatherdata={
            "city": city,
            "Temperature":req["main"]["temp"],
            "feelslike": int(req["main"]["feels_like"]),
            "Max": req["main"]["temp_max"],
            "Min":req["main"]["temp_min"],
            "weather":req["weather"][0]["description"],
            "speed":req["wind"]["speed"],
            "humid": req["main"]["humidity"],
            "icon": req["weather"][0]["icon"]
        }
    
    
    return render_template("index.html",weatherdata=weatherdata)