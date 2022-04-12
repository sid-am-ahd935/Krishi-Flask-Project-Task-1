from utils import BASE_DIR, os, get_weather
from flask import Blueprint, render_template, request

weather_blueprint = Blueprint("weather_blueprint", __name__, template_folder= os.path.join(BASE_DIR, "templates"))


@weather_blueprint.route('/')
def weather_endpoint():
    return render_template('weather.html')

@weather_blueprint.route('/results', methods= ["GET", "POST"])
def results_endpoint():
    if request.method == "GET":
        lat = request.args.get('lat')
        lon = request.args.get('lon')
    elif request.method == "POST":
        lat = request.form['lat']
        lon = request.form['lon']

    return get_weather(lat, lon)