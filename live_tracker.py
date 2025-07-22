import os
import time
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Load .env
load_dotenv()
API_KEY = os.getenv("ETHERSCAN_API_KEY")
wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example: Binance Cold Wallet

# For plotting
timestamps = []
balances = []

plt.ion()  # Interactive mode on
fig, ax = plt.subplots()
line, = ax.plot([], [], '-o')
ax.set_title("Live ETH Wallet Balance")
ax.set_xlabel("Time")
ax.set_ylabel("ETH")

def get_balance():
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&tag=latest&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return int(data["result"]) / 1e18  # Wei → ETH

while True:
    try:
        balance = get_balance()
        timestamp = time.strftime("%H:%M:%S")

        timestamps.append(timestamp)
        balances.append(balance)

        line.set_xdata(range(len(timestamps)))
        line.set_ydata(balances)
        ax.relim()
        ax.autoscale_view()

        plt.xticks(range(len(timestamps)), timestamps, rotation=45)
        plt.draw()
        plt.pause(10)  # Update every 10 seconds

        print(f"[{timestamp}] ETH Balance: {balance:.4f}")

    except KeyboardInterrupt:
        print("Tracking stopped.")
        break
