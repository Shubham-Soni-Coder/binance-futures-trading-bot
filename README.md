# Binance Futures Testnet Trading Bot

A lightweight CLI-based Python application for placing Market and Limit orders on Binance Futures Testnet. The project demonstrates clean code structure, input validation, logging, and exception handling.

---

## Features

- Place **Market Orders**
- Place **Limit Orders**
- Supports **BUY** and **SELL**
- Binance Futures Testnet integration
- Command Line Interface (CLI)
- Input validation
- Structured logging
- Exception handling

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── constants.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Requirements

- Python 3.x
- Binance Futures Testnet Account
- Binance Testnet API Key & Secret

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
BASE_URL=https://testnet.binancefuture.com
```

> **Note:** Never upload your `.env` file to GitHub.

---

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

---

## Command Line Arguments

| Argument | Description |
|----------|-------------|
| `--symbol` | Trading Symbol (Example: BTCUSDT) |
| `--side` | BUY or SELL |
| `--type` | MARKET or LIMIT |
| `--quantity` | Order Quantity |
| `--price` | Required for LIMIT Orders |

---

## Logging

Application logs are automatically saved in:

```text
logs/trading_bot.log
```

The log file contains:

- Input validation logs
- API request logs
- API response logs
- Error logs

---

## Validation

The application validates:

- Trading Symbol
- Order Side
- Order Type
- Quantity
- Price (Required for LIMIT Orders)

---

## Error Handling

The application handles:

- Invalid user input
- Binance API errors
- Network errors
- Unexpected exceptions

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

---

## Assumptions

- Binance Futures Testnet account is already created.
- API credentials are valid.
- Internet connection is available.
- LIMIT orders require a valid price.

---

## Disclaimer

This project is developed for educational purposes and uses **Binance Futures Testnet** only. No real funds are involved.
