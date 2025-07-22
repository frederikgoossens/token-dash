import sqlite3

conn = sqlite3.connect("wallet_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM wallet_balance ORDER BY timestamp DESC LIMIT 10")
rows = cursor.fetchall()

for row in rows:
    print(f"Time: {row[0]} | Balance: {row[1]:.4f} ETH")
