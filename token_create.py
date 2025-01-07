from algosdk import account, util, transaction
from algosdk.v2client import algod
import os
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

total = 1000000
decimals = 2

total_supply  = total * 10 ** decimals

tokenCreateTxn = transaction.AssetCreateTxn(sender = address,
                                          sp = suggested_params,
                                          total = total,
                                          decimals = decimals,
                                          default_frozen= False,
                                          asset_name="Pravallika",
                                          unit_name ="Pk",
                                          manager=address,
                                          reserve=address,
                                          clawback=address,
                                          freeze=address)


signedTxn = tokenCreateTxn.sign(private_key=private_key)

txid = algod_client.send_transaction(signedTxn)

print(f"Txn sent : https://lora.algokit.io/testnet/transaction/{txid}")

result = transaction.wait_for_confirmation(algod_client=algod_client,txid=txid,wait_rounds = 4)

asset_id = result['asset-index']

print(f"Txn Confirmed in round {result['confirmed-round']}")

# print(f"Token Create Txn Confirmed in round {result['confirmed-round']} with asset id {asset_id} [https://lora.algokit.io/testnet/{asset_id}/transactions]")

# #https://lora.algokit.io/testnet/asset/47490462/transactions