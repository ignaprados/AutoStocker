import pandas
import time
import datetime
from datetime import datetime
import os
from termcolor import colored

os.system('CLS')

# Seccion carga de datos desde CSV (base de datos)
"""-----------------------------------------------------------------------------------------------------------------------"""
matrixpandas = pandas.read_csv("matrix.csv")
matriz = matrixpandas.values.tolist()
"""-----------------------------------------------------------------------------------------------------------------------"""


# Seccion de funciones
"""-----------------------------------------------------------------------------------------------------------------------"""
#Imprime la matriz que contiene la data
def print_data(matriz):
    os.system('CLS')
    print_matriz = pandas.DataFrame(matriz, columns=["code","name","type","stock","repos","last_update"])
    print("Imprimiendo matriz de datos...")
    time.sleep(1)
    print(print_matriz)
    print(" ")
    decition = input("Cuando desee regresar al menú principal ingrese cualquier tecla: ")
    time.sleep(1)
    os.system('CLS')


# Consultar stock de un producto en particular
def product_stock(matriz):
    pass

# Consultar stock de un tipo de producto (type)
def product_type(matriz):
    type_product = input("Ingrese la categoria de producto por el que desea filtrar: ")
    a = len(matriz)
    lista = list()
    for i in range(a):
        if (matriz[i][2]).upper() == (type_product).upper():
            lista.append(matriz[i])
    c = pandas.DataFrame(lista, columns=["code","name","type","stock","repos","last_update"])
    os.system('CLS')
    print(c)
    print(" ")
    decition = input("Cuando desee regresar al menú principal ingrese cualquier tecla: ")
    os.system('CLS')
    time.sleep(1)
    

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
    new_product.append(code.upper())
    new_product.append(name)
    new_product.append(type_product)
    new_product.append(stock)
    new_product.append(reposition)
    new_product.append(get_current_time())
    matriz.append(new_product)
    print("El producto "+ code +" fue agregado")
    time.sleep(2)
    os.system('CLS')
    df = pandas.DataFrame(matriz)
    df.to_csv("./matrix.csv", sep=',',index=False)


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
    df = pandas.DataFrame(matriz)
    df.to_csv("./matrix.csv", sep=',',index=False)

def modificate_stock(matriz):
    time.sleep(0.5)
    long = len(matriz)
    os.system("CLS")
    code_modified = (input("Ingresa el codigo del producto que quieres modificar el stock: ")).upper()
    
    
    os.system("CLS")
    code_founded = False
    for i in range(long):

        try:
            pos = matriz[i][0].index(code_modified)
            pos_change = i
            code_founded = True
            print(f"Se encontro el producto {matriz[pos_change][1]}...")
            time.sleep(2)
            os.system("CLS")

        except:
            continue
    print (colored("- 1.", "blue",attrs=["bold"]), "Aumentar stock")
    print (colored("- 2.", "blue",attrs=["bold"]),"Disminuir stock")
    egressingress = (input("Ingrese una opción: ")).upper()
    os.system("CLS")
    if egressingress == "1" and code_founded == True or egressingress == "AUMENTAR" and code_founded == True:
        actual_stock = int(matriz[pos_change][3])
        time.sleep(1)
        print(f"El stock actual de {code_modified} es: ", actual_stock)
        increase = int(input(f"Cuanto stock desea agregar al stock de {code_modified}: "))
        suma = actual_stock + increase
        suma = str(suma)
        matriz[pos_change][3] = suma
        matriz[pos_change][5] = get_current_time()
        df = pandas.DataFrame(matriz)
        df.to_csv("./matrix.csv", sep=',',index=False)
        time.sleep(2)
    
        print(f"El stock de {code_modified} ha sido modificado, ahora es: {matriz[pos_change][3]}")
        os.system("CLS")
    elif egressingress == "2" and code_founded == True or egressingress == "DISMINUIR" and code_founded == True:
        actual_stock = int(matriz[pos_change][3])
        print(f"El stock actual de {code_modified} producto es: ", actual_stock)
        time.sleep(1)
        decrease = int(input(f"Cuanto stock desea restar al stock de {code_modified}: "))
        resta = actual_stock - decrease
        resta = str(resta)
        matriz[pos_change][3] = resta
        matriz[pos_change][5] = get_current_time()
        print(f"El stock de {code_modified} ha sido modificado, ahora es: {matriz[pos_change][3]}")
        df = pandas.DataFrame(matriz)
        df.to_csv("./matrix.csv", sep=',',index=False)
        time.sleep(2)
        os.system("CLS")
    
    elif code_founded == False:
        print(f"El codigo {code_modified} no se encontro")
        print (colored("- 1.", "blue",attrs=["bold"]), "Volver a intentar")
        print (colored("- 2.", "blue",attrs=["bold"]),"Volver al menu principal")
        choose = (input("Ingrese una opción: ")).upper()

        if choose == "1":
            modificate_stock(matriz)
        elif choose == "2":
            print("Volviendo al menu principal...")
            time.sleep(1)
            os.system("CLS")
        else:
            print("No ingreso una opcion correcta, volviendo al menu principal...")
            time.sleep(1)
            os.system("CLS")
    else:
        print("Usted no ingreso una opcion correcta")
        print (colored("- 1.", "blue",attrs=["bold"]), "Volver a intentar")
        print (colored("- 2.", "blue",attrs=["bold"]),"Volver al menu principal")
        choose = (input("Ingrese una opción: ")).upper()
        if choose == "1":
            modificate_stock(matriz)
        elif choose == "2":
            print("Volviendo al menu principal...")
            time.sleep(1)
            os.system("CLS")
        else:
            print("No ingreso una opcion correcta, volviendo al menu principal...")
            time.sleep(1)
            os.system("CLS")

       
        
"""-----------------------------------------------------------------------------------------------------------------------"""
    





# Seccion menu principal-programa
"""-----------------------------------------------------------------------------------------------------------------------"""
print()
print (colored("Bienvenido a AutoStocker", "blue",attrs=["bold","underline"]))
date_update = datetime.now()
now = date_update.strftime("%d/%m/%Y")
print (colored("Hoy es " + now, "white"))
print()
o = "INICIAR"

while o != "CERRAR":

    print (colored("--- Menú Principal ---","blue",attrs=["bold"]))
    print (colored("- 1.", "blue",attrs=["bold"]), "Imprimir Data")
    print (colored("- 2.", "blue",attrs=["bold"]),"Agregar Producto")
    print (colored("- 3.", "blue",attrs=["bold"]) ,"Eliminar Producto")
    print(colored("- 4.", "blue",attrs=["bold"]) ,"Modificar Stock")
    print(colored("- 5.", "blue",attrs=["bold"]),"Filtrar por categoria")
    print(colored("- 6.", "blue",attrs=["bold"]) ,"Cerrar")
    o = (input("> Ingrese una opcion: ")).upper()
    if o == "CERRAR" or o == "6":
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
    elif o == "FILTRAR CATEGORIA" or o == "5":
        product_type(matriz)
    else:
        print("No has ingresado un comando valido")
        time.sleep(1)
        os.system("CLS")
"""-----------------------------------------------------------------------------------------------------------------------"""
