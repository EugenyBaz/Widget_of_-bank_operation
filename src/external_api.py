import json
import requests


cur_in = "USD"
cur_out = "RUB"
list_cur = 1

url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur_in}&from={cur_out}&amount={list_cur}"

payload = {}
headers = {"apikey": "gUiCIVV0bjZdFfmI3bOXuoGSLD60xml7"}

response = requests.request("GET", url, headers=headers, data=payload)
status_code = response.status_code
result = response.text
result_py = json.loads(result)

# tot_res = result_py['result']

print(result_py)

