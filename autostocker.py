import pandas
import time
import datetime
from datetime import datetime
import os
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

def get_current_time():
    time_update = datetime.now()
    now = time_update.strftime("%d/%m/%Y %H:%M:%S")
    return now

# Agregar nuevo producto, su stock inicial y demas
def add_new_product(matriz):
    new_product = list()
    code = input("Ingresa el codigo del producto que desea agregar: ")
    name = input("Ingresa el nombre del producto que va a agregar: ")
    type_product = input("Ingresa la categoria del producto: ")
    stock = int(input("Ingresa el stock inicial del producto, puede ser 0: "))
    reposition = int(input("Punto de reposicion del producto: "))
    new_product.append(code)
    new_product.append(name)
    new_product.append(type_product)
    new_product.append(stock)
    new_product.append(reposition)
    new_product.append(get_current_time())
    matriz.append(new_product)
    print("El producto "+ code +" fue agregado")
    time.sleep(2)
    os.system('CLS')


def delete_product(matriz):
    long = len(matriz)
    eliminated = False
    code_eliminate = input("Ingresa el codigo del producto que quieres eliminar: ")
    for i in range(long):
        try:
            pos = matriz[i][0].index(code_eliminate)
            name1 = matriz[i][1]
            print("El producto ", name1, " fue encontrado, eliminando...")
            matriz.pop(i)
            time.sleep(1)
            print("El producto fue eliminado")
            eliminated = True

        except:
            continue
    if eliminated == False:
        print("El codigo no es correcto")


def modificate_stock(matriz):
    long = len(matriz)
    code_modified = input("Ingresa el codigo del producto que quieres modificar el stock: ")
    egressingress = (input("Desea aumentar o disminuir el stock?: ")).upper()
    code_founded = False
    for i in range(long):

        try:
            pos_change = i
            pos = matriz[i][0].index(code_modified)
            code_founded = True
        except:
            continue
    if egressingress == "AUMENTAR" and code_founded == True:
        actual_stock = int(matriz[pos_change][3])
        print("El stock actual del producto es: ", actual_stock)
        time.sleep(1)
        increase = int(input("Cuanto stock desea agregar al stock del producto: "))
        suma = actual_stock + increase
        suma = str(suma)
        matriz[pos_change][3] = suma
        matriz[pos_change][5] = get_current_time()
        print("El stock de "+ code_modified +" ha sido modificado")
    
    elif egressingress == "DISMINUIR" and code_founded == True:
        actual_stock = int(matriz[pos_change][3])
        print("El stock actual del producto es: ", actual_stock)
        time.sleep(1)
        decrease = int(input("Cuanto stock desea disminuir al stock del producto: "))
        resta = actual_stock - decrease
        resta = str(resta)
        matriz[pos_change][3] = resta
        matriz[pos_change][5] = get_current_time()
        print("El stock de "+ code_modified +" ha sido modificado")






"""-----------------------------------------------------------------------------------------------------------------------"""





# Seccion menu principal-programa
"""-----------------------------------------------------------------------------------------------------------------------"""
print()
print("Bienvenido a AutoStocker")
date_update = datetime.now()
now = date_update.strftime("%d/%m/%Y")
print("Hoy es " + now)
print()
o = "INICIAR"

while o != "CERRAR":

    print("--- Menú Principal ---")
    print("- 1. Imprimir Data")
    print("- 2. Agregar Producto")
    print("- 3. Eliminar Producto")
    print("- 4. Modificar Stock")
    print("- 5. Cerrar")
    
    o = (input("> Ingrese una opcion: ")).upper()
    if o == "CERRAR" or o == "5":
        print("Guardando datos en la base de datos...")
        df = pandas.DataFrame(matriz)
        df.to_csv("./matrix.csv", sep=',',index=False)

        time.sleep(1)
        print("Cerrando AutoStocker...")
        time.sleep(1)
    elif o == "PRINT_DATA" or o == "1":
        print_data(matriz)
    elif o == "AGREGAR PRODUCTO" or o == "2":
        add_new_product(matriz)
    elif o == "ELIMINAR PRODUCTO" or o == "3":
        delete_product(matriz)
    elif o == "MODIFICAR STOCK" or o == "4":
        modificate_stock(matriz)
"""-----------------------------------------------------------------------------------------------------------------------"""