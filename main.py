import discord
from jokes import get_random_joke
from fun_facts import get_random_fun_fact
from weather_functions import get_weather
from postfix_calculator import evaluate_postfix, infix_to_postfix
from prime_factorization import prime_factorization
from wazirx_api import get_coin_price

# Define your bot's intents
intents = discord.Intents.default()
intents.typing = False  # Disable typing notifications for simplicity
intents.message_content = True  # Enable message content intent

# Create a bot instance with the specified intents
bot = discord.Client(intents=intents)


# Define an event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Here is the main code!!!
# Here is the main code!!!
# Here is the main code!!!
# Here is the main code!!!
# Here is the main code!!!
# Here is the main code!!!

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    if message.content.startswith('Buddy, joke'):
        joke = get_random_joke()
        await message.channel.send(joke)

    if message.content.startswith('Buddy, weather'):
        location = message.content[14:]  # Extract location from the message
        if location:
            api_key = "1486bdd4245443e58c6170007232009"
            weather_info = get_weather(location, api_key)
            await message.channel.send(weather_info)
        else:
            await message.channel.send("Please provide a location for the weather.")

    if message.content.startswith('Buddy, fun fact'):
        fun_fact = get_random_fun_fact()
        await message.channel.send(fun_fact)

    if message.content.startswith('Buddy, cal'):
        print(infix_to_postfix(message.content[11:]))
        cal = infix_to_postfix(message.content[11:])
        print(cal)
        await message.channel.send(evaluate_postfix(cal))

    if message.content.startswith('Buddy, prime factor'):
        yo = prime_factorization(int(message.content[19:]))
        await message.channel.send(yo)

    if message.content.startswith('Buddy, crypto '):
        try:
            a = message.content.split(' ')[2].upper()
            b = message.content.split(' ')[3].upper()
            coin_price = get_coin_price(a, b)
            await message.channel.send(coin_price)
        except IndexError:
            await message.channel.send("Please provide a valid coin symbol.")

    if message.content.startswith('Buddy, help'):
        await message.channel.send(""""
        =========Commands==========
        Prefix all commands with "Buddy, "
        
        
        ***Basic Commands***
        1) help - See all commands
        
        2) weather [Location] - See weather of that location {Avoid using 5000 times a day...}
        
        3) joke - Bot tells a joke
        
        4) fun fact - tells a fact
        
        5) prime factor [Integer]
        
        eg: Buddy, weather Thane
        eg: Buddy, joke
        
        
        *** For calculations ***
        use "cal" and enter any problem
        eg: Buddy, cal 1 + 2 + 3 / 4
        ###DO REMEMBER TO USE SPACES BETWEEN EACH NUMBER AND OPERATOR###
        
        
        *** Crypto Exchange ***
        use "crypto" and enter 2 coins a and b
        a - the coin whose value you want
        b - it will show the value in this coin or currency
        eg: Buddy, crypto btc inr       
        
        """)


# Start the bot with your token
bot.run("MTE1NDA3MDEzOTc2ODE1NjI2MQ.GDEU-O.uOJaH9lJ7Hf0S_grjPG1oUQX7EM4aZ94bXSSpY")
