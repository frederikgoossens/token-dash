import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()
API_KEY = os.getenv("ETHERSCAN_API_KEY")

# Replace with any ETH address
wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&tag=latest&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

# Convert from wei to ETH
eth_balance = int(data["result"]) / 10**18
wallet_name = "Binance Cold Wallet"
print(f"{wallet_name} Balance: {eth_balance:.4f} ETH")
