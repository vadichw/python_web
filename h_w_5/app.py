import argparse
import asyncio
import logging
from datetime import datetime, timedelta
from pprint import pprint
import aiohttp

API_URL = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'


async def fetch_currency():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(API_URL) as response:
                return await response.json() if response.status == 200 else None
        except aiohttp.ClientConnectorError as e:
            logging.error(f"Connection error {API_URL}: {e}")
            return None


async def get_currency_history(max_days_history):
    if max_days_history > 10:
        raise ValueError("The maximum number of days allowed is 10.")

    return [{'date': datetime.now() - timedelta(days=i), 'rates': await fetch_currency()} for i in
            range(max_days_history)]


def format_currency_history(currency_history):
    formatted_history = []
    for entry in currency_history:
        date_str = entry['date'].strftime('%d.%m.%Y')
        rates = entry['rates']

        formatted_entry = {date_str: {}}

        for rate in rates:
            ccy = rate['ccy']
            sale = float(rate['sale'])
            purchase = float(rate['buy'])

            if ccy not in formatted_entry[date_str]:
                formatted_entry[date_str][ccy] = {'sale': sale, 'purchase': purchase}

        formatted_history.append(formatted_entry)

    return formatted_history


def parse_args():
    parser = argparse.ArgumentParser(description='Get currency exchange rates for the last N days.')
    parser.add_argument('days', type=int, help='Number of days to retrieve currency rates for')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    try:
        currency_history = asyncio.run(get_currency_history(args.days))
        formatted_history = format_currency_history(currency_history)
        pprint(formatted_history)
    except ValueError as e:
        print(f"Error: {e}")














