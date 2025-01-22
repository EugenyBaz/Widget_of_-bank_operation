import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def convert_currency(currency):
    cur_in = currency
    cur_out = "RUB"

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{cur_in}"


    response = requests.request("GET", url)
    result = response.text
    result_py = json.loads(result)

    tot_res = round(result_py['conversion_rates']["RUB"],4)

    return tot_res



