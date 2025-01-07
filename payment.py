# account creation, transactions
from algosdk import account, util, transaction
# algod to connect with algorand blockchain - v2client
# if we transfer data use indexer
from algosdk.v2client import algod
import os
# handling environment variables
from dotenv import load_dotenv

load_dotenv()

private_key = os.getenv("PRIVATE_KEY")
address = account.address_from_private_key(private_key)
print("Address:", address)

algod_token = os.getenv("ALGOD_TOKEN")
algod_url = os.getenv("ALGOD_URL")
algod_port = os.getenv("ALGOD_PORT")

algod_client = algod.AlgodClient(algod_token=algod_token, algod_address=algod_url)

suggested_params = algod_client.suggested_params()

payTxn = transaction.PaymentTxn(sender = address, 
                                sp = suggested_params, 
                                amt = util.algos_to_microalgos(0.673), receiver="MFTLPXPAOQSE5GXR6FXG7ONQMQTQGDL7BMHJOZIEJHRCGCE47EEB225FRI",
                                note = "Sending Transactions")

signedTxn = payTxn.sign(private_key=private_key)

txid = algod_client.send_transaction(signedTxn)

print(f"Txn sent : https://lora.algokit.io/testnet/transaction/{txid}")

result = transaction.wait_for_confirmation(algod_client=algod_client,txid=txid,wait_rounds = 4)

print(f"Txn Confirmed in round {result['confirmed-round']}")