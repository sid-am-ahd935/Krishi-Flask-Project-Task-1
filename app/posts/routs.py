from .models import Tweet, db
from utils import BASE_DIR, os, beautify, time
from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from sqlalchemy import func
from geoalchemy2.shape import to_shape

post_blueprint = Blueprint("post_blueprint", __name__, template_folder= os.path.join(BASE_DIR, "templates"))

# For reducing time complexity by storing the model_queryset in cache
class Cache:
    tweet_queryset = None


@post_blueprint.route('/', methods= ['GET', 'POST'])
def send_message_endpoint():
    if request.method == "GET":
        return render_template("send_message.html")
    elif request.method == "POST":
        msg = request.form['msg_box']
        lat = request.form['lat_box']
        lon = request.form['lon_box']

        try:
            tweet = Tweet(msg= msg, lat= lat, lon= lon)
            db.session.add(tweet)
            db.session.commit()

            return jsonify("success")
        
        except Exception as e:
            return jsonify("failure" + str(e))
    
    return jsonify("Undefined Method Request" + str(request.method))



@post_blueprint.route('/show', methods= ["GET", "POST"])
def show_messages_endpoint():
    if request.method == "GET":
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        show_all = False
        want_json = False

        if not(lat or lon):
            return render_template("get_location.html")

    elif request.method == "POST":
        lat = request.form['lat']
        lon = request.form['lon']
        show_all = request.form.get('show-all')
        want_json = request.form.get('want-json')
    
    else:
        return jsonify("Undefined Method Request" + str(request.method))
    
    # global tweet_queryset
    Cache.tweet_queryset = Tweet.query.order_by(
        func.ST_Distance(
            Tweet.location, func.Geometry(func.ST_GeomFromText('POINT({} {})'.format(lat, lon), 0))
        )
    )

    if show_all:
        if want_json:
            return jsonify(
                list({
                        "id" : tweet.id,
                        "message" : tweet.msg,
                        "lattitude" : to_shape(tweet.location).x,
                        "longitude" : to_shape(tweet.location).y,
                        "timestamp" : beautify(tweet.epoch_time, time.time()),
                    }
                for tweet in Cache.tweet_queryset.all())
            )
        else:
            return render_template("show_messages.html", tweets= tweets, beautify_time= beautify, point= to_shape, int= int, time= time.time)

    else:
        if want_json:
            return redirect(url_for("post_blueprint.show_pagination_endpoint", page_no= 1, json= True))
        else:
            return redirect(f"{request.url}/1")



@post_blueprint.route('/show/<int:page_no>')
def show_pagination_endpoint(page_no):
    # global tweet_queryset

    if not Cache.tweet_queryset:
        return redirect(url_for('post_blueprint.show_messages_endpoint'))
    
    want_json = request.args.get('json')
    
    tweets = Cache.tweet_queryset.paginate(page= page_no, per_page= 10, error_out= True)

    if want_json:
        return jsonify(
            current_page_tweets= list({
                    "id" : tweet.id,
                    "message" : tweet.msg,
                    "lattitude" : to_shape(tweet.location).x,
                    "longitude" : to_shape(tweet.location).y,
                    "timestamp" : beautify(tweet.epoch_time, time.time()),
            } for tweet in tweets.items),
            next= (f'{request.host_url[:-1]}{url_for("post_blueprint.show_pagination_endpoint", page_no= tweets.page+1, json= True)}' if tweets.has_next else None),
            prev= (f'{request.host_url[:-1]}{url_for("post_blueprint.show_pagination_endpoint", page_no= tweets.page-1, json= True)}' if tweets.has_prev else None),
            page=  tweets.page,
            total_pages= tweets.pages
        )
    else:
        return render_template("show_paginated.html", tweets= tweets, beautify_time= beautify, point= to_shape, int= int, time= time.time)
