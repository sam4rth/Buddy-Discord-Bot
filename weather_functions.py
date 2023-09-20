import requests

def get_weather(location, api_key):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Current weather in {location}: {condition}, Temperature: {temperature}°C"
    else:
        return "Unable to fetch weather information."
