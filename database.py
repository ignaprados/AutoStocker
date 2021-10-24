import sqlite3
import pandas


df = pandas.read_csv("./registros.csv")
conn = sqlite3.connect('./database.db')
df.to_sql('registros', conn, if_exists='replace', index=False)
conn.close()

# Print matriz.db using pandas


def print1():
    conn = sqlite3.connect('./database.db')
    df = pandas.read_sql_query("SELECT * FROM registros", conn)
    print(df)
    conn.close()


print1()
