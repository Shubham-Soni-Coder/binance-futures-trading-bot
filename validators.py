from bot.constants import VALID_SIDES,VALID_ORDERS_TYPES,SUPPORED_QUOTES
from bot.logging_config import setup_logger

logger = setup_logger()

def validate(symbol,side,order_type,quantity,price):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()
    logger.info(
    f"Validating Input | "
    f"Symbol={symbol} "
    f"Side={side} "
    f"Type={order_type} "
    f"Quantity={quantity} "
    f"Price={price}"
)

    if not symbol.endswith(SUPPORED_QUOTES):
        logger.error(f"Invalid Symbol: {symbol}")
        raise ValueError("Symbol must end with USDT.")

        if side not in VALID_SIDES:
            logger.error(f"Invalid Side: {side}")
            raise ValueError("Invalid side.")
        
        if order_type not in VALID_ORDERS_TYPES:
            logger.error(f"Invalid Order Type: {order_type}")
            raise ValueError("Invalid order type.")
        
        if quantity <= 0:
            logger.error(f"Invalid Quantity: {quantity}")
            raise ValueError("Quantity must be greater than 0")
        
        if order_type == "LIMIT":
            if price is None:
                logger.error("Price is missing for LIMIT order.")
                raise ValueError("Price is required for LIMIT order.")
            
            if price <= 0:
                logger.error(f"Invalid Price: {price}")
                raise ValueError("Price must be greater than 0.")
            
    logger.info("Input validation successful.")
