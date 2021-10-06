
import pandas
import time
import datetime
from datetime import datetime
# Seccion carga de datos desde CSV (base de datos)
"""-----------------------------------------------------------------------------------------------------------------------"""
matrixpandas = pandas.read_csv("matrix.csv")
matriz = matrixpandas.values.tolist()
"""-----------------------------------------------------------------------------------------------------------------------"""



# Seccion de funciones
"""-----------------------------------------------------------------------------------------------------------------------"""
#Imprime la matriz que contiene la data
def print_data(matriz):
    print_matriz = pandas.DataFrame(matriz)
    print(print_matriz)

# Consultar stock de un producto en particular
def product_stock(matriz):
    pass

# Consultar stock de un tipo de producto (type)
def product_type(matriz):
    pass

# Agregar nuevo producto, su stock inicial y demas
def add_new_product(matriz):
    new_product = list()
    code = input("Ingresa el codigo del producto que desea agregar: ")
    name = input("Ingresa el nombre del producto que va a agregar: ")
    type_product = input("Ingresa la categoria del producto: ")
    stock = int(input("Ingresa el stock inicial del producto, puede ser 0: "))
    reposition = int(input("Punto de reposicion del producto: "))
    time_update = datetime.now()
    dt_string = time_update.strftime("%d/%m/%Y %H:%M:%S")
    new_product.append(code)
    new_product.append(name)
    new_product.append(type_product)
    new_product.append(stock)
    new_product.append(reposition)
    new_product.append(dt_string)
    matriz.append(new_product)

    




    



"""-----------------------------------------------------------------------------------------------------------------------"""





# Seccion menu principal-programa
"""-----------------------------------------------------------------------------------------------------------------------"""

o = "INICIAR"

while o != "CERRAR":
    o = (input("Inicie la operacion que desea realizar: ")).upper()
    if o == "CERRAR":
        print("Guardando datos en la base de datos...")
        df = pandas.DataFrame(matriz)
        df.to_csv("./matrix.csv", sep=',',index=False)

        time.sleep(1)
        print("Cerrando AutoStocker...")
        time.sleep(1)
    elif o == "PRINT_DATA":
        print_data(matriz)
    elif o == "AGREGAR PRODUCTO":
        add_new_product(matriz)
"""-----------------------------------------------------------------------------------------------------------------------"""