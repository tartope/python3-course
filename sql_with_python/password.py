import sqlite3

con = sqlite3.connect("users.db")
c = con.cursor()

# query = "CREATE TABLE users (username TEXT, password TEXT);"
# c.execute(query)

# data = [
#     ("Mr", "rogers"),
#     ("Bob", "ross")
# ]
# c.executemany("INSERT INTO users VALUES (?,?)", data)

u = input("please enter username...")
p = input("please enter password...")

# better way to set up passwords using "?" placeholders; this lets the SQLite library handle it and preven any malicious injection
query = f"SELECT * FROM users WHERE username=? AND PASSWORD=?"
c.execute(query, (u,p))

result = c.fetchone()
if result:
    print("welcome back")
else:
    print("failed login")

con.commit()
con.close()