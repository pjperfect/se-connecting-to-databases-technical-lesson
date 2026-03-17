import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

cur = conn.cursor()

df = pd.DataFrame(
    cur.execute("""SELECT * FROM offices;""").fetchall(),
    columns = [x[0] for x in cur.description]
)

# cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")
# cur.execute("""SELECT * FROM offices;""")

# table_names = cur.fetchall()
# office_data = cur.fetchall()
# office_cols = cur.description

print(df)

conn.close()