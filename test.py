import asyncio
import base64
from pytoniq import Cell
from tonclient.client import TonClient
from tonclient.types import ClientConfig, NetworkConfig, ParamsOfEncodeMessage, ParamsOfSendMessage

ENABLE_SEND = False  # True - отправка, False - только тест/вывод
WALLET_ADDRESS = "0:ВАШ_АДРЕС_КОШЕЛЬКА"
WALLET_PRIVATE_KEY = "ВАШ_ПРИВАТНЫЙ_КЛЮЧ_64_БАЙТА_HEX"

def tonconnect_to_cell(tx_dict):
    cell_boc = base64.b64decode(tx_dict["cell"])
    cell = Cell.one_from_boc(cell_boc)
    return cell

async def main():
    client = TonClient(
        config=ClientConfig(
            network=NetworkConfig(server_address="https://net.ton.dev")
        )
    )

    response_json = {
        "transactions": [
            {
                "address": "0:8e459f28bbfae363e7c2275a502840fed1879199ee5a18161f4013cd48c70c8e",
                "value": "300000000",
                "cell": "te6cckECAwEAAQEAAbAPin6lADwP6Aea2KFAX14QCADFAZO2xwaprdg7fm9XarzNf/kR3t5sj8++t2uyKseIqwA9GGZOgfd0YtTuwJwTHP6OjFjtMxyqpoJ4YVW5C0yYusgeGbBBAQHhZmTeKoARzd7tC8glcUI+NXyBFoFVTunDxGCIAUxORnBKLd+FvDAD0YZk6B93Ri1O7AnBMc/o6MWO0zHKqmgnhhVbkLTJi64AejDMnQPu6MWp3YE4Jjn9HRix2mY5VU0E8MKrchaZMXWAAAAANFINBcACAF+gGGYssVva6ApcCAHowzJ0D7ujFqd2BOCY5/R0YsdpmOVVNBPDCq3IWmTF1gAAABDx62iu",
                "send_mode": 3
            }
        ]
    }

    transactions = []
    for tx_dict in response_json.get("transactions", []):
        cell = tonconnect_to_cell(tx_dict)
        transactions.append({
            "destination": tx_dict["address"],
            "amount": int(tx_dict["value"]),
            "body": cell,
            "send_mode": tx_dict.get("send_mode", 3)
        })

    for i, tx in enumerate(transactions, start=1):
        print(f"Transaction {i}:")
        print("Destination:", tx["destination"])
        print("Amount:", tx["amount"])
        print("Body:", tx["body"])
        print("Send mode:", tx["send_mode"])
        print("-" * 50)

    if ENABLE_SEND:
        for tx in transactions:
            encode_msg = await client.abi.encode_message(
                ParamsOfEncodeMessage(
                    abi={"type": "Contract", "value": {}},  
                    address=WALLET_ADDRESS,
                    call_set={
                        "function_name": "sendTransaction",
                        "input": {
                            "dest": tx["destination"],
                            "value": str(tx["amount"]),
                            "bounce": False,
                            "flags": tx["send_mode"],
                            "payload": tx["body"].to_boc().hex()
                        }
                    },
                    signer={"type": "Keys", "keys": {"private": WALLET_PRIVATE_KEY}},
                    is_internal=True
                )
            )

            send_result = await client.processing.send_message(
                ParamsOfSendMessage(message=encode_msg.message, send_events=False)
            )

            print("TX hash:", send_result.transaction.hash)
            print("=" * 60)
    else:
        print("Отправка транзакций отключена (тестовый режим).")

if __name__ == "__main__":
    asyncio.run(main())
