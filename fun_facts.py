import requests

def get_random_fun_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["text"]
    else:
        return "Unable to fetch a fun fact."
