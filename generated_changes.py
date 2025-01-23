import sqlite3

# Open database connection
conn = sqlite3.connect('database.db') 

def transfer(from_acct, to_acct, amount):
  try:
    conn.execute("BEGIN TRANSACTION")
    
    conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_acct))
    conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_acct))
    
    conn.execute("COMMIT")
  except:
    conn.execute("ROLLBACK")
    raise

try:
  transfer(1, 2, 100) 
except:
  print("Transfer failed, rolling back changes")

conn.close()