import sqlite3                                                                                   # importar libreria sqlite3
import pandas                                                                                    # importar libreria pandas


df = pandas.read_csv("./registros.csv")                                                         # leer archivo csv
conn = sqlite3.connect('./database.db')                                                         # conectar a la base de datos
df.to_sql('registros', conn, if_exists='replace', index=False)                                  # guardar en la base de datos
conn.close()                                                                                    # cerrar conexion a la base de datos



# funcion para imprimir la base de datos
def print1():       
    conn = sqlite3.connect('./database.db')                                                    # conectar a la base de datos
    df = pandas.read_sql_query("SELECT * FROM registros", conn)                                # convertir la base de datos a matriz con pandas
    print(df)                                                                                  # imprimir la base de datos
    conn.close()                                                                               # cerrar conexion a la base de datos


print1()                                                                                       # llamar a la funcion print1
