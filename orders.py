from binance.exceptions import BinanceAPIException,BinanceOrderException
from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()

class OrderService:
    def __init__(self):
        self.client = get_client()

    def place_market_order(self,symbol:str,side:str,quantity:float):
        try:
            logger.info(
                f"Sending MARKET order | "
                f"Symbol={symbol} Side={side} Quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"MARKET order placed successfully | {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise 
        except BinanceOrderException as e:
            logger.error(f"Network Error: {e}")
            raise 
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise 

    
    def place_limit_order(
        self,
        symbol : str,
        side:str,
        quantity:float,
        price:float,
    ):
        try:
            logger.info(
                f"Sending LIMIT order | "
                f"Symbol={symbol} Side={side} "
                f"Quantity={quantity} Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            logger.info(f"LIMIT order placed successfully | {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            raise

        except Exception as e:
            logger.exception(f"Unexpected Error: {e}")
            raise