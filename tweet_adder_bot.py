import requests
import random

url = "http://127.0.0.1:5000/posts"
url = 'http://127.0.0.1:5000/posts/'

def post_tweet():
    msg_templates = ["This post is made by 'Tweet Adder Bot'.", 
            "Any suggestions on improving this websites backend a little? No frontend improvement can be done currently.;]",
            "Tweets are sorted by location not time.", 
            "There is no filter added for limiting posts by distance.",
            "Any suggestions on improving this websites backend a little? No frontend improvement can be done currently.;]",
            "Any post can be seen by any location.",
            "Enter location coordinates wisely.",
            "Any suggestions on improving this websites backend a little? No frontend improvement can be done currently.;]",
            "This is a flask website.",
            "These are tweets not posts.",
            "Any suggestions on improving this websites backend a little? No frontend improvement can be done currently.;]",
            'Thanks for viewing this website.',
            "Any suggestions on improving this websites backend a little? No frontend improvement can be done currently.;]",
        ]
    msg = random.sample(msg_templates, 1)
    lat = random.randint(-90, 90)
    lon = random.randint(-180, 180)

    payload = {
        "msg_box" : msg,
        "lat_box" : lat,
        "lon_box" : lon,
    }

    r = requests.post(url, payload)
    return r.text

for i in range(int(input("Enter the no of random posts to do on this flask website: "))):
    print(post_tweet())


    