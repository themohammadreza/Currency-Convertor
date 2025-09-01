import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def get_exchange_rate(src_currency, dst_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{src_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["rates"].get(dst_currency)
    return None

def convert_currency(amount, exchangerate):
    if exchangerate:
        return amount * exchangerate
    return 'conversion failed '

if __name__ == "__main__":
    print("Currency Converter")

    src_currency = input("Enter source currency (e.g. USD): ")
    dst_currency = input("Enter destination currency (e.g. EUR): ")
    amount = int(input("Enter amount to convert: "))

    exchange_rate = get_exchange_rate(src_currency, dst_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    print(f"{amount} {src_currency} is {converted_amount} {dst_currency}")