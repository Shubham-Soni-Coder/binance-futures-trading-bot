VALID_SIDES = ("BUY","SELL")
VALID_ORDERS_TYPES = (
    "MARKET",
    "LIMIT",
)
SUPPORED_QUOTES = (
    "USDT"
)
DEFAULT_TESTNET_URL = (
    "https://testnet.binancefuture.com"
)

LOG_FILE = "logs/trading_bot.log"

INVALID_SYMBOL= "Symbol must end with USDT."
INVALID_SIDE= "Side must be BUY or SELL."
INVALID_ORDER_TYPE= "Order type must be MARKET or LIMIT."
INVALID_QUANTITY= "Quantity must be grater than 0."
INVALID_REQUIRED= "Price is required for LIMIT order."
INVALID_PRICE= "Price must be greater than 0."