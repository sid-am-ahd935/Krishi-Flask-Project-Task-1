import requests, random, json

class Cache:
    cached_result = []

def generate_location():
    lat = random.randint(-90, 90)
    lon = random.randint(-180, 180)

    return lat, lon


def test(start_msg, test_func):
    try:
        print("Starting Tests For", start_msg, "...")
        Cache.cached_result.append({"Testing Response From" : test_func.__name__,
                                    'Result Response' : json.loads(test_func())})
        print("Test Completed.")
    except Exception as e:
        print("There was an error while testing", test_func.__name__, "\nThe error:", e)


def get_weather():
    lat, lon = generate_location()
    url = f"http://127.0.0.1:5000/weather/results?lat={lat}&lon={lon}"
    
    r = requests.get(url)
    return json.dumps(r.json(), indent= 2)


def post_message():
    url = 'http://127.0.0.1:5000/posts/'

    msg_templates = [
        "This message is meant to be stored in JSON API examples file.",
        "Dummy message for filling in database for JSON documentation.",
        "JSON API support!!",
        "JSON API Bot to the rescue.",
    ]
    message = random.choice(msg_templates)
    lat, lon = generate_location()

    payload = {
        "msg_box" : message,
        "lat_box" : lat,
        "lon_box" : lon,
    }
    r = requests.post(url, data= payload)

    return json.dumps(r.json(), indent= 2)


def get_posts():
    url = 'http://127.0.0.1:5000/posts/show/'
    content = {}
    # From Page: 3
    # To Page: 7
    for i in range(int(input("From Page:")), int(input("To Page:"))):
        lat, lon = generate_location()
        full_url = url + str(i) + f"?lat={lat}&lon={lon}&json=true"

        r = requests.get(full_url)

        content['Page Number From JSON Bot'] = i
        content['lat'] = lat
        content['lon'] = lon
        content[f'Point(lat={lat} & lon={lon})'] = r.json()
    return json.dumps(content, indent= 5)


if __name__ == "__main__":
    test("Weather API", get_weather)
    test("Send Posts API", post_message)
    test("Getting Paginated Posts API", get_posts)
    
    with open("API_Data.json", 'w') as f:
        json.dump(Cache.cached_result, f, indent= 2)
    