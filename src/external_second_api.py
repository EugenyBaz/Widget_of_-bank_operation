import json
import requests

def convert_currency(currency):
    cur_in = currency
    cur_out = "RUB"

    url = f"https://v6.exchangerate-api.com/v6/2eeb61ae9abeb967454825f0/latest/{cur_in}"


    headers = {"apikey": "2eeb61ae9abeb967454825f0"}

    response = requests.request("GET", url)
    status_code = response.status_code
    result = response.text
    result_py = json.loads(result)

    tot_res = round(result_py['conversion_rates']["RUB"],4)

    return tot_res

print (convert_currency("EUR"))


