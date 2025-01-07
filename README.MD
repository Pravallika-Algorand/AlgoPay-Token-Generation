# AlgoPay Token Projects

This repository contains three main Python scripts that interact with the Algorand blockchain using the Algorand SDK (`algosdk`). The scripts cover account creation, payment transactions, and token creation. All the scripts work together to create an account, send payments, and generate a custom token on the Algorand blockchain. These scripts use environment variables stored in a `.env` file for sensitive data.

## 1. `account.py`

This script handles **account creation**, **mnemonic generation**, and **private key management**. It:
- Generates a new Algorand account.
- Derives the private key from the mnemonic phrase.
- Verifies if the derived private key matches the original one.
- Fetches private key and address from the `.env` file.

### How to run:
```bash
python account.py
```

## 2. payment.py
-This script performs payment transactions on the Algorand blockchain. It:

--Connects to the Algorand network using algod client.
--Sends a payment transaction from one address to another.
--Waits for the transaction to be confirmed and provides the transaction link.
How to run:
```bash
python payment.py
```

## 3. token_create.py
- This script creates a custom Algorand token on the blockchain. It:

-- Creates a new asset with a specified total supply and decimal precision.
-- Assigns the current account as the asset's manager, reserve, clawback, and freeze addresses.
-- Waits for the transaction to be confirmed and provides the asset ID.

### How to run:
```bash
python token_create.py
```

## Setup

### 1. Clone the repository

### 2. Install dependencies

```bash
pip install algosdk python-dotenv
```

### 3. Create a .env file in the root directory with the following content

```bash
PRIVATE_KEY=your_private_key
ALGOD_TOKEN=your_algod_token
ALGOD_URL=your_algod_url
ALGOD_PORT=your_algod_port
```

### 4. Run the scripts individually using python <script_name>.py