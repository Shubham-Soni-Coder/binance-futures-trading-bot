from bot.client import get_client
from pprint import pprint
client = get_client()

info = client.futures_exchange_info()