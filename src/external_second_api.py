import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv('API_KEY')

def convert_currency(currency):
    cur_in = currency

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{cur_in}"

    response = requests.get(url)
    result = response.json()

    tot_res = round(result['conversion_rates']["RUB"],4)

    return tot_res
print(convert_currency("USD"))
print(type(convert_currency("USD")))






