# ton-transfer-demo

✨ Welcome to **ton-transfer-demo**! ✨ This project provides a handy Python script designed to process and optionally send transactions received via TonConnect, decoding them from Base64-encoded cells into usable formats for the TON network. It's a perfect tool for developers looking to understand or interact with TON transactions programmatically!

## 🚀 Key Features

*   🔄 **Decode TonConnect Transactions**: Converts Base64-encoded transaction cells into `pytoniq.Cell` objects.
*   🔍 **Extract Transaction Details**: Easily retrieve essential information like destination address, amount, and send mode from decoded transactions.
*   ✉️ **Optional Transaction Sending**: Integrate with the TON SDK to send processed transactions to the network.
*   🧪 **Test Mode**: Safely preview decoded transaction details without actually sending them, perfect for development and debugging.

## 🛠️ Technologies Used

### Backend

*   **Python**: The core language for the script.
*   **pytoniq-core**: For handling TON cell serialization and deserialization.
*   **tonclient**: The official TON SDK client for interacting with the TON network.
*   **tonutils-py**: A utility library for TON.
*   **aiohttp**: For asynchronous HTTP requests.
*   **asyncio**: Python's built-in library for writing concurrent code.

## 🚀 Getting Started

Follow these steps to set up and run the `ton-transfer-demo` project on your local machine.

### Prerequisites

*   Python 3.8+

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/crc137/ton-transfer-demo.git
    cd ton-transfer-demo
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Before running, you need to configure the `test.py` script:

1.  **Edit `test.py`**: Open the `test.py` file in your favorite text editor.
2.  **Enable Sending (Optional)**:
    Set `ENABLE_SEND` to `True` if you want to actually send transactions, or `False` to only decode and display information (test mode).
    ```python
    ENABLE_SEND = False # Set to True to enable sending transactions
    ```
3.  **Set your Wallet Details**:
    Replace the placeholder values for `WALLET_ADDRESS` and `WALLET_PRIVATE_KEY` with your actual TON wallet address and 64-byte private key (in hexadecimal format).
    ```python
    WALLET_ADDRESS = "0:YOUR_WALLET_ADDRESS"
    WALLET_PRIVATE_KEY = "YOUR_PRIVATE_KEY_64_BYTES_HEX"
    ```

### Running the Script

Once configured, execute the script from the `ton-transfer-demo` directory:

```bash
python test.py
```

The script will process the example transaction and, depending on your `ENABLE_SEND` setting, either display its decoded details or attempt to send it to the TON network.
