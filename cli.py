import argparse
from bot.logging_config import setup_logger
from bot.orders import OrderService
from bot.validators import validate

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )
    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (e.g. BITCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order Side"
    )
    
    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order Type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (Required for LIMIT Order)"
    )

    args = parser.parse_args()


    validate(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    service = OrderService()

    if args.type == "MARKET":
        response = service.place_market_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity,
        )
    else:
        response = service.place_limit_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity,
            price=args.price,
        )

    print("\n========== ORDER SUMMARY ==========")
    print(f"Symbol       : {args.symbol}")
    print(f"Side         : {args.side}")
    print(f"Order Type   : {args.type}")
    print(f"Quantity     : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price        : {args.price}")

    print("\n========== RESPONSE ==========")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice')}")

    print("\n Order placed successfully.")

    
if __name__=="__main__":
    main()