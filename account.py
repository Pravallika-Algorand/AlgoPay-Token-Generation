# account creation, transactions
from algosdk import account, encoding,  mnemonic
import os
# handling environment variables
from dotenv import load_dotenv

load_dotenv()

# Generate an account
private_key, address = account.generate_account()

print("Private Key:", private_key)
print("Address:",address)

mnemon = mnemonic.from_private_key(private_key)
print("Mnemonic:",mnemon)

derived_private_key = mnemonic.to_private_key(mnemon)
print("Private Key derived from mnemonic:",derived_private_key)

print(f"Checking if Private Key and Private key from Mnemonic:{private_key == derived_private_key}")

env_private = os.getenv("PRIVATE_KEY")
print("Private Key From .env", env_private)
print("Address from .env:",account.address_from_private_key(env_private))

