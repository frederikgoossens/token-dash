import sqlite3

conn = sqlite3.connect("wallet_data.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS wallet_balance (
    timestamp TEXT,
    eth_balance REAL
)
''')

conn.commit()
conn.close()
print("✅ Database initialised.")
