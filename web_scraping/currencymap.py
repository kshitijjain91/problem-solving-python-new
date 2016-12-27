import requests, json, pprint
from bs4 import BeautifulSoup

currency_url = "https://openexchangerates.org/api/latest.json?app_id=59379dbb1b7743b19daa017bcdbf264e"

res_currency = requests.get(currency_url)
try:
    res_currency.raise_for_status()
except Exception as exc:
    print("An error occured while fetching currency rates: {0}".format(exc))

currency_soup = BeautifulSoup(res_currency.text, 'html.parser')
currency_dict =json.loads(str(currency_soup))

print(currency_dict["rates"]["INR"])

frm = "INR"
to = "GBP"


frm_value = currency_dict.get(frm.upper())
to_value = currency_dict.get(to.upper())
print(frm_value, to_value)

print(currency_dict.get("rates")[frm.upper()])
print(currency_dict.get("rates")[to.upper()])
print(currency_dict['rates'].keys())
print(type(currency_dict['rates'].keys()))

keys = currency_dict['rates'].keys()
for key in keys:
    print(key)