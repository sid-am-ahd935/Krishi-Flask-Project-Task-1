from flask import Flask
import requests, os, time
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# For easily transferring app from here to there

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') # twitter_clone_db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app



# Current directory here is app folder because it is running from run.py
BASE_DIR = os.getcwd()




api_key = os.environ.get('WEATHER_API_KEY')

def get_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    r = requests.get(url)
    return r.json()






def beautify(t1, t2 = time.time()):
    t = int(t2-t1)

    if t < 60:
        return "Just Now"
    
    if t < 120:
        return "A Minute Ago"
    
    if t < 60 * 60:
        return f"{t//60} Minutes Ago"

    if t < 60 * 60 * 2:
        return "An Hour Ago"

    if t < 60 * 60 * 24:
        return f"{t//(3600)} Hours Ago"

    if t <= 60 * 60 * 24 * 2:
        return "Yesterday"

    if t < 60 * 60 * 24 * 28:
        return f"{t//(3600 * 24)} Days Ago"
    
    if t < 60 * 60 * 24 * 28 * 2:
        return "A Month Ago"
    
    if t < 60 * 60 * 24 * 30 * 12:
        return "Few Months Ago"
    
    else:
        return "A Year Ago"