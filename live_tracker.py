import sqlite3
import os
import time
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()
API_KEY = os.getenv("ETHERSCAN_API_KEY")
wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Binance Cold Wallet

# Connect to SQLite database
conn = sqlite3.connect("wallet_data.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS wallet_balance (
    timestamp TEXT,
    eth_balance REAL
)
''')
conn.commit()

# Setup matplotlib live plot
timestamps = []
balances = []

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], '-o')
ax.set_title("Live ETH Wallet Balance")
ax.set_xlabel("Time")
ax.set_ylabel("ETH")

# Function to get balance from Etherscan
def get_balance():
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&tag=latest&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return int(data["result"]) / 1e18  # Convert Wei → ETH

# Main loop
try:
    while True:
        balance = get_balance()
        timestamp = time.strftime("%H:%M:%S")

        timestamps.append(timestamp)
        balances.append(balance)

        # Update plot
        line.set_xdata(range(len(timestamps)))
        line.set_ydata(balances)
        ax.relim()
        ax.autoscale_view()
        plt.xticks(range(len(timestamps)), timestamps, rotation=45)
        plt.draw()
        plt.pause(10)  # Update every 10 seconds

        print(f"[{timestamp}] ETH Balance: {balance:.4f}")

        # Insert into database
        cursor.execute(
            "INSERT INTO wallet_balance (timestamp, eth_balance) VALUES (?, ?)",
            (timestamp, balance)
        )
        conn.commit()

except KeyboardInterrupt:
    pr
