import requests


# Function to fetch a random joke from the JokeAPI
def get_random_joke():
    #url = "https://v2.jokeapi.dev/joke/Dark?type=single"
    url = "https://v2.jokeapi.dev/joke/Programming?type=single"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get("joke")
    else:
        return "Failed to fetch a joke, The API is joking with me"
