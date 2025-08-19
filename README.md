# ton-transfer-demo

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

✨ Welcome to **ton-transfer-demo**! ✨ This project provides a Python script to decode and optionally send TON transactions received via TonConnect. Base64-encoded transaction cells are converted into usable formats, making it ideal for developers exploring the TON blockchain.

## Key Features:

*  **Decode TonConnect Transactions**: Converts Base64-encoded cells into `pytoniq.Cell` objects.
*  **Extract Transaction Details**: Retrieve destination addresses, amounts, and send modes easily.
*  **Optional Transaction Sending**: Integrate with TON SDK to send processed transactions.
*  **Test Mode**: Preview decoded transaction details without sending, perfect for debugging.

## Technologies Used:

* **Python 3.8+**
* **pytoniq-core**: TON cell serialization/deserialization.
* **tonclient**: Official TON SDK client.
* **tonutils-py**: Utility library for TON.
* **aiohttp**: Async HTTP requests.
* **asyncio**: Python's async framework.

## Installation:

1. Clone the repository:

```bash
git clone https://github.com/crc137/ton-transfer-demo.git
cd ton-transfer-demo
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> ⚠ Note: `tonclient` and `tonutils-py` may require GitHub access or manual installation.

## Configuration:

1. Open `test.py`.
2. Set `ENABLE_SEND` to control sending transactions:

```python
ENABLE_SEND = False  # True to send, False for test mode
```

3. Enter your wallet details:

```python
WALLET_ADDRESS = "0:YOUR_WALLET_ADDRESS"
WALLET_PRIVATE_KEY = "YOUR_PRIVATE_KEY_64_BYTES_HEX"
```

> **Keep your private key secure and do not commit it to GitHub!**

## Running the Script:

```bash
python test.py
```

The script will decode the example transaction and either display details or send it based on `ENABLE_SEND`.

## Safety & Notes:

* This project is for **development and demonstration purposes only**.
* Handle real transactions and keys **with extreme caution**.
* Ensure all dependencies are installed in the correct Python environment.
* Never share private keys publicly.

## 🛡 License
MIT © [Coonlink](https://coonlink.com)
