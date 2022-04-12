from flask import request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from posts.models import db, Tweet
from posts.routs import post_blueprint
from utils import create_app
from weather.routs import weather_blueprint


# print(get_weather(29.39291, -98.50925))

app = create_app()
db.init_app(app= app)
db.create_all(app= app)


app.register_blueprint(weather_blueprint, url_prefix= "/weather")
app.register_blueprint(post_blueprint, url_prefix= "/posts")



@app.route('/')
def home():
    return f"Go to {request.host_url}/weather for weather, either fill the fields or directly send a post request at {request.host_url} and go to {request.host_url}posts for Twitter API"




if __name__ == "__main__":
    app.run(debug= True)
