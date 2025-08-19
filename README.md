# ton-transfer-demo

✨ Welcome to **ton-transfer-demo**! ✨ This project features a handy Python script designed to process and optionally send transactions received via TonConnect. It efficiently decodes Base64-encoded cells into a usable format for the TON network, making it perfect for developers looking to understand or interact with TON transactions programmatically!

## 🚀 Key Features

* 🔄 **Decode TonConnect Transactions**: Converts Base64-encoded transaction cells into `pytoniq.Cell` objects, ready for inspection.
* 🔍 **Extract Transaction Details**: Easily retrieve essential information like destination address, amount, and send mode from decoded transactions.
* ✉️ **Optional Transaction Sending**: Integrate with the TON SDK to send processed transactions to the network after decoding.
* 🧪 **Test Mode**: Safely preview decoded transaction details without actually sending them, ideal for development and debugging.

## 🛠️ Technologies Used

### Backend

* **Python**: The core language powering the `ton-transfer-demo` script.
* **pytoniq-core**: Essential library for handling TON cell serialization and deserialization.
* **tonclient**: The official TON SDK client for seamless interaction with the TON network.
* **tonutils-py**: A utility library providing helpful functionalities for TON development.
* **aiohttp**: Used for asynchronous HTTP requests, ensuring efficient network communication.
* **asyncio**: Python's built-in library for writing concurrent code, enabling non-blocking operations.

## 🚀 Getting Started

Follow these steps to set up and run the `ton-transfer-demo` project on your local machine.

### Prerequisites

* Python 3.8+ installed on your system.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/crc137/ton-transfer-demo.git
   cd ton-transfer-demo
   ```

2. **Create and activate a virtual environment** (recommended for dependency isolation):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   > ⚠️ **Note**: `tonclient` and `tonutils-py` may require special installation steps if installing directly from their GitHub repositories (e.g., manual download and local `pip install` or GitHub token/SSH access). Refer to their respective repository instructions if you encounter issues.

### Configuration

Before running `ton-transfer-demo`, you need to configure the main script:

1. **Open `test.py`** in your preferred text editor.

2. **Enable Sending (Optional)**:
   Locate the `ENABLE_SEND` variable. Set it to `True` if you wish to actually send transactions to the TON network, or `False` to only decode and display information (test mode).

   ```python
   ENABLE_SEND = False # Change to True to enable transaction sending
   ```

3. **Set your Wallet Details**:
   Replace the placeholder values for `WALLET_ADDRESS` and `WALLET_PRIVATE_KEY` with your actual TON wallet address and your 64-byte private key (in hexadecimal format). **Ensure these are kept private and secure.**

   ```python
   WALLET_ADDRESS = "0:YOUR_WALLET_ADDRESS"
   WALLET_PRIVATE_KEY = "YOUR_PRIVATE_KEY_64_BYTES_HEX"
   ```

### Running the Script

Once configured, execute the `ton-transfer-demo` script from its root directory:

```bash
python test.py
```

The script will process the included example transaction. Depending on your `ENABLE_SEND` setting, it will either display its decoded details or attempt to send it to the TON network.

<hr>

### ⚠️ Important Notes

* The `ton-transfer-demo` project is primarily for **demonstration and development purposes**.
* Always exercise **extreme caution** when dealing with real transactions and private keys.
* Ensure your Python environment is correctly set up and all dependencies are installed.
* **Never share your private keys publicly** or commit them to a public repository.
