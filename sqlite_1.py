import sqlite3


artist_id = int(input('Upisite ID izvodjaca: '))

# 1. Konekcija
conn = sqlite3.connect('/Users/jaso/downloads/chinook.db')

# 2. Cursor
c = conn.cursor()

# 3. EXECUTE
# c.execute('''SELECT * FROM albums''')
c.execute('''SELECT * FROM albums WHERE artistid = ?''', (artist_id,))


# 3.1. Dohvat -> Fetch
data_from_db = c.fetchall()
print(data_from_db)

# 3.2 promjena u bazi -> commit
# 4. CLOSE
c.close()
conn.close()