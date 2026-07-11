# Binance Futures Testnet Trading Bot

A lightweight command-line trading bot built in Python for placing orders on Binance Futures Testnet. It provides a simple interface for submitting market and limit orders using the Binance API.

## Overview

This project is designed for testing and learning purposes. It allows users to:

- Connect to Binance Futures Testnet
- Place market orders
- Place limit orders
- Validate order input before submission

## Features

- Simple CLI-based interface
- Support for BUY and SELL orders
- Support for MARKET and LIMIT order types
- Input validation for symbols, quantity, and price
- Logging for order activity and errors

## Project Structure

- cli.py: Command-line entry point
- bot/client.py: Binance client initialization
- bot/orders.py: Order placement logic
- bot/validators.py: Input validation
- bot/constants.py: Supported values and constants
- bot/logging_config.py: Logging setup

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a .env file in the project root with your Binance testnet credentials:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

> Keep your API credentials private and do not commit the .env file to version control.

## Usage

Run the bot from the project root:

```bash
python cli.py --symbol BITCUSDT --side BUY --type MARKET --quantity 0.001
```

Example for a limit order:

```bash
python cli.py --symbol BITCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

### Arguments

- --symbol: Trading symbol (for example, BITCUSDT)
- --side: Order side (BUY or SELL)
- --type: Order type (MARKET or LIMIT)
- --quantity: Order quantity
- --price: Required for LIMIT orders

## Notes

- This bot connects to Binance Futures Testnet by default.
- Use testnet credentials only.
- Orders are submitted only after basic validation checks.

## Disclaimer

This project is intended for educational and testing use. Use it responsibly and ensure you understand the risks involved in trading.
