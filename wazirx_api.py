# bot_modules/wazirx_api.py

import requests

BASE_WAZIRX_API_URL = 'https://api.wazirx.com/api/v2/tickers/'

def get_coin_price(source_symbol, target_symbol):
    try:
        # Construct the URL with both source and target symbols
        url = BASE_WAZIRX_API_URL + source_symbol.lower() + target_symbol.lower()

        response = requests.get(url)
        data = response.json()

        if 'ticker' in data:
            ticker_data = data['ticker']
            if 'last' in ticker_data:
                last_price = ticker_data['last']
                return f'Last {source_symbol.upper()} price in {target_symbol.upper()}: {last_price} {target_symbol.upper()}'
            else:
                return f"Last price not available for {source_symbol.upper()} in {target_symbol.upper()}."
        else:
            return f"Data not available for {source_symbol.upper()} in {target_symbol.upper()}."

    except requests.exceptions.RequestException as re:
        return f"Request error: {str(re)}"
    except ValueError as ve:
        return f"Invalid JSON response: {str(ve)}"
    except Exception as e:
        return f'Error: {str(e)}'
