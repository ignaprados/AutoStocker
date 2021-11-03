# Importar librerias
import pandas                                                                                   # importar libreria pandas
import time                                                                                     # importar libreria time
import datetime                                                                                 # importar libreria de fecha y hora
from datetime import datetime                                                                   # importar la libreria de datetime
import os                                                                                       # importar la libreria de os
from termcolor import colored                                                                   # importar la libreria termcolor
import sqlite3                                                                                  # importar libreria sqlite3
os.system('CLS')                                                                                # limpiar la terminal

# Seccion carga de datos desde CSV (base de datos)
"""-----------------------------------------------------------------------------------------------------------------------"""
conn = sqlite3.connect('./database.db')                                                         # conexion a la base de datos
matrixpandas = pandas.read_sql_query("SELECT * FROM productos", conn)                           # carga de datos desde la base de datos de stock
matriz = matrixpandas.values.tolist()                                                           # convertir la matriz a una lista
registros = pandas.read_sql_query("SELECT * FROM registros", conn)                              # carga de datos desde la base de datos de registros
registros = registros.values.tolist()                                                           # convertir la matriz a una lista
"""-----------------------------------------------------------------------------------------------------------------------"""


# Seccion de funciones
"""-----------------------------------------------------------------------------------------------------------------------"""


# funcion para imprimir la matriz de productos
def print_data(matriz):
    os.system('CLS')
    print_matriz = pandas.DataFrame( 
        matriz, columns=["code", "name", "type", "stock", "repos", "price", "last_update"])     # generar la matriz en formato pandas
    print("Imprimiendo matriz de datos...")                                                     # mensaje de impresion
    time.sleep(1)                                                                               # esperar 1 segundo
    print(print_matriz)                                                                         # imprimir la matriz de stock
    print(" ")
    decition = input(
        "Cuando desee regresar al menú principal ingrese cualquier tecla: ")                    # volver al menu principal
    os.system('CLS')                                                                            # limpiar la terminal
    time.sleep(1)                                                                               # esperar 1 segundo


# funcion para imprimir la matriz de registros
def print_registros(registros):
    print_registros = pandas.DataFrame(
        registros, columns=["code", "variacion", "motivo", "timestamp"])                        # generar la matriz en formato pandas
    print("Imprimiendo matriz de datos...")                                                     # mensaje de impresion
    time.sleep(1)                                                                               # esperar 1 segundo
    print(print_registros)                                                                      # imprimir la matriz de registros
    print(" ")
    decition = input(
        "Cuando desee regresar al menú principal ingrese cualquier tecla: ")                    # volver al menu principal
    os.system('CLS')                                                                            # limpiar la terminal
    time.sleep(1)                                                                               # esperar 1 segundo


# funcion para consultar el stock de un producto
def product_stock(matriz):
    os.system("CLS")                                                                            # limpiar la terminal
    founded = False                                                                             # variable para saber si se encontro el producto
    stock = (input("Ingrese el código del producto a consultar stock: ")).upper()               # capturar el codigo del producto a buscar
    os.system('CLS')                                                                            # limpiar la terminal
    for i in range(len(matriz)):                                                                # recorrer la matriz

        if stock == matriz[i][0]:                                                               # si se encontró el codigo del producto en la matriz
            print("El stock actual del producto ", stock, "es: ", matriz[i][3])                 # imprimir el stock del producto
            founded = True                                                                      # cambiar la variable a True
            input("Ingrese cualquier tecla cuando desee volver al menu principal: ")            # volver al menu principal
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal

    if founded == False:                                                                        # si no se encontró el codigo del producto en la matriz
        print("No se encontro el codigo")                                                       # mensaje de error
        time.sleep(1)                                                                           # esperar 1 segundo
        os.system("CLS")                                                                        # limpiar la terminal
        print(colored("- 1.", "blue", attrs=["bold"]), "Volver a intentar ")                    # mensaje de volver a intentar
        print(colored("- 2.", "blue",
                      attrs=["bold"]), "Volver al menú principal")                              # mensaje de volver al menu principal
        choose = (input("Ingrese una opción: ")).upper()                                        # capturar la opcion

        if choose == "1":                                                                       # si la opcion es 1
            product_stock(matriz)                                                               # volver a intentar

        elif choose == "2":                                                                     # si la opcion es 2
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal


# funcion para filtrar los productos por tipo
def product_type(matriz):
    type_product = input(
        "Ingrese la categoria de producto por el que desea filtrar: ")                          # capturar el tipo de producto para filtrar
    a = len(matriz)                                                                             # obtener la longitud de la matriz
    lista = list()                                                                              # crear una lista
    for i in range(a):                                                                          # recorrer la matriz
        if (matriz[i][2]).upper() == (type_product).upper():                                    # si el tipo de producto es igual al tipo de producto capturado
            lista.append(matriz[i])                                                             # agregar el producto a la lista
    c = pandas.DataFrame(
        lista, columns=["code", "name", "type", "stock", "repos", "price", "last_update"])      # generar la matriz en formato pandas
    os.system('CLS')                                                                            # limpiar la terminal
    print(c)                                                                                    # imprimir la matriz de productos
    print(" ")
    decition = input(
        "Cuando desee regresar al menú principal ingrese cualquier tecla: ")                    # volver al menu principal
    os.system('CLS')                                                                            # limpiar la terminal
    time.sleep(1)                                                                               # esperar 1 segundo


def get_current_time():
    time_update = datetime.now()                                                                # obtener la fecha y hora actual
    now = time_update.strftime("%d/%m/%Y %H:%M:%S")                                             # formatear la fecha y hora actual
    return now                                                                                  # retornar fecha


# funcion para agregar un nuevo producto
def add_new_product(matriz):
    new_product = list()                                                                        # crear una lista para almacenar los datos del nuevo producto
    code = input("Ingresa el codigo del producto que desea agregar: ")                          # capturar el codigo del producto
    name = input("Ingresa el nombre del producto que va a agregar: ")                           # capturar el nombre del producto
    type_product = input("Ingresa la categoria del producto: ")                                 # capturar el tipo de producto
    stock = int(input("Ingresa el stock inicial del producto, puede ser 0: "))                  # capturar el stock inicial del producto
    reposition = int(input("Punto de reposicion del producto: "))                               # capturar el punto de reposicion del producto
    price = input("Ingresa el precio del producto: ")                                           # capturar el precio del producto
    new_product.append(code.upper())                                                            # agregar el codigo al nuevo producto
    new_product.append(name)                                                                    # agregar el nombre al nuevo producto
    new_product.append(type_product)                                                            # agregar el tipo de producto al nuevo producto
    new_product.append(stock)                                                                   # agregar el stock al nuevo producto
    new_product.append(reposition)                                                              # agregar el punto de reposicion al nuevo producto
    new_product.append(price)                                                                   # agregar el precio al nuevo producto
    new_product.append(get_current_time())                                                      # agregar la fecha y hora actual al nuevo producto
    matriz.append(new_product)                                                                  # agregar el nuevo producto a la matriz
    print("El producto " + code + " fue agregado")                                              # mensaje de confirmacion
    time.sleep(2)                                                                               # esperar 2 segundos
    os.system('CLS')                                                                            # limpiar la terminal
    df = pandas.DataFrame(matriz)                                                               # generar la matriz en formato pandas
    df.to_sql('productos', conn, if_exists='replace', index=False)                              # almacenar la matriz de stock en la base de datos
    ajuste = [code, "Se añadio un producto",                                                   
              "Added product", get_current_time()]                                              # crear una lista para almacenar los datos del ajuste

    registros.append(ajuste)                                                                    # agregar el ajuste a la matriz de registros

    df = pandas.DataFrame(registros)                                                            # generar la matriz en formato pandas
    df.to_sql('registros', conn, if_exists='replace', index=False)                              # almacenar la matriz de registros en la base de datos


# funcion para eliminar producto
def delete_product(matriz):
    long = len(matriz)                                                                          # obtener la longitud de la matriz
    eliminated = False                                                                          # variable para saber si se elimino un producto
    code_eliminate = input(
        "Ingresa el codigo del producto que quieres eliminar: ")                                # capturar el codigo del producto a eliminar
    for i in range(long):                                                                       # recorrer la matriz
        try:
            pos = matriz[i][0].index(code_eliminate)                                            # obtener la posicion del codigo capturado
            name1 = matriz[i][1]                                                                # obtener el nombre del producto
            print("El producto ", name1, " fue encontrado, eliminando...")                      # mensaje de código encontrado
            matriz.pop(i)                                                                       # eliminar el producto de la matriz
            time.sleep(1)                                                                       # esperar 1 segundo
            print("El producto fue eliminado")                                                  # mensaje de confirmacion
            eliminated = True                                                                   # cambiar la variable a True

        except:
            continue
    if eliminated == False:                                                                     # si no se eliminó ningun producto
        print("El codigo no es correcto")                                                       # mensaje de error
    df = pandas.DataFrame(matriz)                                                               # generar la matriz en formato pandas
    df.to_sql('productos', conn, if_exists='replace', index=False)                              # almacenar la matriz de stock en la base de datos
    ajuste = "Se borro el producto"
    motivo = "Producto eliminado"
    ajuste = [code_eliminate, ajuste, motivo, get_current_time()]                               # crear una lista para almacenar los datos del ajuste

    registros.append(ajuste)                                                                    # agregar el ajuste a la matriz de registros

    df = pandas.DataFrame(registros)                                                            # generar la matriz de registros en formato pandas
    df.to_sql('registros', conn, if_exists='replace', index=False)                              # almacenar la matriz de registros en la base de datos


# fución para modificar el stock de un producto
def modificate_stock(matriz):
    time.sleep(0.5)                                                                             # esperar 0.5 segundos
    long = len(matriz)                                                                          # obtener la longitud de la matriz
    os.system("CLS")                                                                            # limpiar la terminal
    code_modified = (
        input("Ingresa el codigo del producto que quieres modificar el stock: ")).upper()       # capturar el codigo del producto a modificar

    os.system("CLS")                                                                            # limpiar la terminal
    code_founded = False                                                                        # variable para saber si se encontro el codigo
    for i in range(long):                                                                       # recorrer la matriz

        try:
            pos = matriz[i][0].index(code_modified)                                             # obtener la posicion del codigo capturado
            pos_change = i                                                                      # obtener la posicion del producto a modificar
            code_founded = True                                                                 # cambiar la variable a True
            print(f"Se encontro el producto {matriz[pos_change][1]}...")                        # mensaje de confirmacion de encontrado
            time.sleep(2)                                                                       # esperar 2 segundos
            os.system("CLS")                                                                    # limpiar la terminal

        except:
            continue
    print(colored("- 1.", "blue", attrs=["bold"]), "Aumentar stock")                            # mensaje de opcion 1
    print(colored("- 2.", "blue", attrs=["bold"]), "Disminuir stock")                           # mensaje de opcion 2
    print(colored("- 3.", "blue", attrs=["bold"]),                                              # mensaje de opcion 3
          "Ajuste por perdida de stock")
    egressingress = (input("Ingrese una opción: ")).upper()                                                         # capturar la opcion del usuario
    os.system("CLS")                                                                                                # limpiar la terminal
    if egressingress == "1" and code_founded == True or egressingress == "AUMENTAR" and code_founded == True:       # si la opcion es 1 y el codigo fue encontrado
        actual_stock = int(matriz[pos_change][3])                                                                   # obtener el stock actual del producto
        time.sleep(1)                                                                                               # esperar 1 segundo
        print(f"El stock actual de {code_modified} es: ", actual_stock)                         # mensaje de stock actual
        increase = int(
            input(f"Cuanto stock desea agregar al stock de {code_modified}: "))                 # capturar el stock a aumentar
        suma = actual_stock + increase                                                          # sumar el stock actual mas el stock a aumentar
        suma = str(suma)                                                                        # convertir el stock a string
        matriz[pos_change][3] = suma                                                            # cambiar el stock del producto
        matriz[pos_change][5] = get_current_time()                                              # cambiar la fecha de modificacion
        df = pandas.DataFrame(matriz)                                                           # generar la matriz en formato pandas
        df.to_sql('productos', conn, if_exists='replace', index=False)                          # almacenar la matriz de stock en la base de datos
        ajuste = "+" + str(increase)
        motivo = "Ingreso de stock"
        ajuste = [code_modified, ajuste, motivo, get_current_time()]                            # crear una lista para almacenar los datos del ajuste

        registros.append(ajuste)                                                                # agregar el ajuste a la matriz de registros

        df = pandas.DataFrame(registros)                                                        # generar la matriz de registros en formato pandas
        df.to_sql('registros', conn, if_exists='replace', index=False)                          # almacenar la matriz de registros en la base de datos
        time.sleep(2)                                                                           # esperar 2 segundos

        print(
            f"El stock de {code_modified} ha sido modificado, ahora es: {matriz[pos_change][3]}")                   # mensaje de confirmacion de modificacion
        os.system("CLS")                                                                                            # limpiar la terminal
    elif egressingress == "2" and code_founded == True or egressingress == "DISMINUIR" and code_founded == True:    # si la opcion es 2 y el codigo fue encontrado
        actual_stock = int(matriz[pos_change][3])                                                                   # obtener el stock actual del producto
        print(
            f"El stock actual de {code_modified} producto es: ", actual_stock)                  # mensaje de stock actual
        time.sleep(1)                                                                           # esperar 1 segundo
        decrease = int(
            input(f"Cuanto stock desea restar al stock de {code_modified}: "))                  # capturar el stock a disminuir
        resta = actual_stock - decrease                                                         # restar el stock actual menos el stock a disminuir
        resta = str(resta)                                                                      # convertir el stock a string
        matriz[pos_change][3] = resta                                                           # cambiar el stock del producto
        matriz[pos_change][5] = get_current_time()                                              # cambiar la fecha de modificacion
        print(
            f"El stock de {code_modified} ha sido modificado, ahora es: {matriz[pos_change][3]}")                   # mensaje de confirmacion de modificacion
        df = pandas.DataFrame(matriz)                                                                               # generar la matriz en formato pandas
        df.to_sql('productos', conn, if_exists='replace', index=False)                                              # almacenar la matriz de stock en la base de datos
        ajuste = "-" + str(decrease)
        motivo = "Egreso de stock"
        ajuste = [code_modified, ajuste, motivo, get_current_time()]                            # crear una lista para almacenar los datos del ajuste

        registros.append(ajuste)                                                                # agregar el ajuste a la matriz de registros                           

        df = pandas.DataFrame(registros)                                                        # generar la matriz de registros en formato pandas
        df.to_sql('registros', conn, if_exists='replace', index=False)                          # almacenar la matriz de registros en la base de datos
        time.sleep(2)                                                                           # esperar 2 segundos
        os.system("CLS")                                                                        # limpiar la terminal

    elif egressingress == "3" and code_founded == True:                                         # si la opcion es 3 y el codigo fue encontrado
        actual_stock = int(matriz[pos_change][3])                                               # obtener el stock actual del producto
        print(
            f"El stock actual de {code_modified} producto es: ", actual_stock)                  # mensaje de stock actual
        time.sleep(1)                                                                           # esperar 1 segundo
        ajustar = int(input(f"Cuanto stock se extravio de {code_modified}: "))                  # capturar el stock a ajustar
        motivo = input("Motivo del ajuste: ")                                                   # capturar el motivo del ajuste
        os.system("CLS")                                                                                                                        # limpiar la terminal
        print("Vamos a modificar el stock restando lo que se perdio, y lo que tiene que volver a enviar al cliente. ¿Es usted conciente?")      # mensaje de confirmacion
        print(colored("- 1.", "blue", attrs=["bold"]), "Si")                                                                                    # opcion si
        print(colored("- 2.", "blue", attrs=["bold"]), "No")                                                                                    # opcion no
        choose = (input("Ingrese una opción: ")).upper()                                                                                        # capturar la opcion

        if choose == "1":                                                                       # si la opcion es 1
            mod = actual_stock - (ajustar+ajustar)                                              # modificar el stock
            mod = str(mod)                                                                      # convertir el stock a string
            ajuste = "-"+str(ajustar+ajustar)                                                   # crear string del ajuste                                       
            matriz[pos_change][3] = mod                                                         # cambiar el stock del producto
            os.system("CLS")                                                                    # limpiar la terminal
            mod = "-" + mod                                                                     # convertir el stock a string
            ajuste = [code_modified, ajuste, motivo, get_current_time()]                        # crear una lista para almacenar los datos del ajuste

            registros.append(ajuste)                                                            # agregar el ajuste a la matriz de registros
            print(
                f"Ahora el stock de {code_modified} es: ", (matriz[pos_change][3]))             # mensaje de confirmacion de modificacion

            print(f"Ajuste de {code_modified} realizado con exito")                             # mensaje de confirmacion de ajuste
            df = pandas.DataFrame(registros)                                                    # generar la matriz de registros en formato pandas
            df.to_sql('registros', conn, if_exists='replace', index=False)                      # almacenar la matriz de registros en la base de datos
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal
        elif choose == "2":                                                                     # si la opcion es 2
            print("Cancelando...")                                                              # mensaje de cancelacion
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal

    elif code_founded == False:                                                                 # si el codigo no fue encontrado
        print(f"El codigo {code_modified} no se encontro")                                      # mensaje de codigo no encontrado
        print(colored("- 1.", "blue", attrs=["bold"]), "Volver a intentar")                     # opcion 1
        print(colored("- 2.", "blue",
                      attrs=["bold"]), "Volver al menu principal")                              # opcion 2
        choose = (input("Ingrese una opción: ")).upper()                                        # capturar la opcion

        if choose == "1":                                                                       # si la opcion es 1
            modificate_stock(matriz)                                                            # llamar a la funcion modificar stock
        elif choose == "2":                                                                     # si la opcion es 2
            print("Volviendo al menu principal...")                                             # mensaje de volver al menu principal
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal
        else:
            print("No ingreso una opcion correcta, volviendo al menu principal...")             # mensaje de opcion incorrecta
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal
    else:                                                                                       # si no se ingreso una opcion correcta
        print("Usted no ingreso una opcion correcta")                                           # mensaje de opcion incorrecta
        print(colored("- 1.", "blue", attrs=["bold"]), "Volver a intentar")                     # opcion 1
        print(colored("- 2.", "blue",
                      attrs=["bold"]), "Volver al menu principal")                              # opcion 2
        choose = (input("Ingrese una opción: ")).upper()                                        # capturar la opcion
        if choose == "1":                                                                       # si la opcion es 1 
            modificate_stock(matriz)                                                            # llamar a la funcion modificar stock
        elif choose == "2":                                                                     # si la opcion es 2
            print("Volviendo al menu principal...")                                             # mensaje de volver al menu principal
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal
        else:                                                                                   # si la opcion es incorrecta
            print("No ingreso una opcion correcta, volviendo al menu principal...")             # mensaje de opcion incorrecta
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal


# funcion para editar un producto
def update_product(matriz):
    os.system("CLS")                                                                            # limpiar la terminal
    code = (input("Ingrese el codigo del producto que quiere modificar: ")).upper()             # capturar el codigo del producto
    founded = False                                                                             # variable para saber si el codigo fue encontrado
    long = len(matriz)                                                                          # obtener la longitud de la matriz
    try:
        for i in range(long):                                                                   # recorrer la matriz
            if code == matriz[i][0]:                                                            # si el codigo ingresado es igual al codigo de la matriz
                print(" ")
                print(f"El producto {matriz[i][1]} fue encontrado")                             # mensaje de producto encontrado
                pos = i                                                                         # obtener la posicion del producto
                founded = True                                                                  # cambiar la variable a True
                time.sleep(1)                                                                   # esperar 1 segundo
                os.system("CLS")                                                                # limpiar la terminal

    except:
        print("El codigo no es correcto")                                                       # mensaje de codigo incorrecto
        update_product(matriz)                                                                  # llamar a la funcion update product

    if founded == True:                                                                         # si el codigo fue encontrado
        print(" ")
        print(colored("- 1.", "blue", attrs=["bold"]), "Modificar nombre")                      # opcion 1
        print(colored("- 2.", "blue", attrs=["bold"]), "Modificar precio")                      # opcion 2
        print(colored("- 3.", "blue", attrs=["bold"]), "Modificar stock")                       # opcion 3
        print(colored("- 4.", "blue", attrs=["bold"]), "Modificar codigo")                      # opcion 4
        print(colored("- 5.", "blue", attrs=["bold"]), "Modificar categoria")                   # opcion 5
        print(colored("- 6.", "blue",
                      attrs=["bold"]), "Modificar punto de reposicion")                         # opcion 6
        print(" ")
        choose = input("Ingrese una opcion: ")                                                  # capturar la opcion
        time.sleep(1)                                                                           # esperar 1 segundo
        os.system("CLS")                                                                        # limpiar la terminal
        if choose == "1":                                                                       # si la opcion es 1
            name = input("Ingrese el nuevo nombre: ")                                           # capturar el nuevo nombre
            matriz[pos][1] = name                                                               # cambiar el nombre del producto
            print(" ")
            print("El nombre del producto fue modificado")                                      # mensaje de nombre modificado
            print(" ")

        elif choose == "2":                                                                     # si la opcion es 2
            price = input("Ingrese el nuevo precio: ")                                          # capturar el nuevo precio
            matriz[pos][5] = price                                                              # cambiar el precio del producto
            print(" ")
            print("El precio del producto fue modificado")                                      # mensaje de precio modificado
            print(" ")

        elif choose == "3":                                                                     # si la opcion es 3
            modificate_stock(matriz)                                                            # llamar a la funcion modificar stock
        elif choose == "4":                                                                     # si la opcion es 4
            code = input("Ingrese el nuevo codigo del producto: ")                              # capturar el nuevo codigo
            matriz[pos][0] = code                                                               # cambiar el codigo del producto
            print(" ")
            print("El codigo del producto fue modificado")                                      # mensaje de codigo modificado
            print(" ")
        elif choose == "5":                                                                     # si la opcion es 5
            category = input("Ingrese la nueva categoria: ")                                    # capturar la nueva categoria
            matriz[pos][2] = category                                                           # cambiar la categoria del producto
            print(" ")
            print("La categoria del producto fue modificada")                                   # mensaje de categoria modificada
            print(" ")

        elif choose == "6":                                                                     # si la opcion es 6
            repos = input("Ingrese el nuevo punto de reposicion: ")                             # capturar el nuevo punto de reposicion
            matriz[pos][4] = repos                                                              # cambiar el punto de reposicion del producto
            print(" ")
            print("El punto de reposicion del producto fue modificado")                         # mensaje de punto de reposicion modificado
            print(" ")
        os.system("CLS")                                                                        # limpiar la terminal
    else:                                                                                       # si el codigo no fue encontrado
        print("El codigo no se encontro")                                                       # mensaje de codigo no encontrado
        time.sleep(1.5)                                                                         # esperar 1.5 segundos
        os.system("CLS")                                                                        # limpiar la terminal
        update_product(matriz)                                                                  # llamar a la funcion update product


"""-----------------------------------------------------------------------------------------------------------------------"""


# Seccion menu principal-programa
"""-----------------------------------------------------------------------------------------------------------------------"""
print()
print(colored("Bienvenido a AutoStocker", "blue", attrs=["bold", "underline"]))                 # mensaje de bienvenida
date_update = datetime.now()                                                                    # obtener la fecha actual
now = date_update.strftime("%d/%m/%Y")                                                          # convertir la fecha actual a string
print(colored("Hoy es " + now, "white"))                                                        # imprimir la fecha actual
print()
o = "INICIAR"                                                                                   # opcion iniciar

while o != "7":                                                                            # mientras la opcion no sea cerrar

    print(colored("--- Menú Principal ---", "blue", attrs=["bold"]))                            # imprimir el menu principal
    print(colored("- 1.", "blue", attrs=["bold"]), "Imprimir Data")                             # opcion 1
    print(colored("- 2.", "blue", attrs=["bold"]), "Agregar Producto")                          # opcion 2
    print(colored("- 3.", "blue", attrs=["bold"]), "Eliminar Producto")                         # opcion 3
    print(colored("- 4.", "blue", attrs=["bold"]), "Modificar producto")                        # opcion 4
    print(colored("- 5.", "blue", attrs=["bold"]), "Filtrar por categoria")                     # opcion 5
    print(colored("- 6.", "blue", attrs=["bold"]),
          "Consultar stock del producto")                                                       # opcion 6
    print(colored("- 7.", "blue", attrs=["bold"]), "Cerrar")                                    # opcion 7
    print(colored("- 8.", "blue", attrs=["bold"]), "Imprimir registros")                        # opcion 8
    o = (input("> Ingrese una opcion: ")).upper()                                               # capturar la opcion
    if o == "CERRAR" or o == "7":                                                               # si la opcion es cerrar o 7
        print("Guardando datos en la base de datos...")                                         # mensaje de guardando datos
        df = pandas.DataFrame(matriz)                                                           # convertir la matriz en un dataframe
        df.to_sql('productos', conn, if_exists='replace', index=False)                          # guardar los datos en la base de datos

        time.sleep(1)                                                                           # esperar 1 segundo
        print("Cerrando AutoStocker...")                                                        # mensaje de cerrando AutoStocker
        time.sleep(1)                                                                           # esperar 1 segundo
    elif o == "PRINT_DATA" or o == "1":                                                         # si la opcion es imprimir data o 1
        print_data(matriz)                                                                      # llamar a la funcion print data
    elif o == "AGREGAR PRODUCTO" or o == "2":                                                   # si la opcion es agregar producto o 2
        add_new_product(matriz)                                                                 # llamar a la funcion agregar producto
    elif o == "ELIMINAR PRODUCTO" or o == "3":                                                  # si la opcion es eliminar producto o 3
        delete_product(matriz)                                                                  # llamar a la funcion eliminar producto
    elif o == "MODIFICAR PRODUCTO" or o == "4":                                                 # si la opcion es modificar producto o 4
        update_product(matriz)                                                                  # llamar a la funcion modificar producto
    elif o == "FILTRAR CATEGORIA" or o == "5":                                                  # si la opcion es filtrar categoria o 5
        product_type(matriz)                                                                    # llamar a la funcion filtrar categoria
    elif o == "CONSULTAR STOCK" or o == "6":                                                    # si la opcion es consultar stock o 6
        product_stock(matriz)                                                                   # llamar a la funcion consultar stock
    elif o == "8":                                                                              # si la opcion es 8
        print_registros(registros)                                                              # llamar a la funcion imprimir registros
    else:                                                                                       # si la opcion no es ninguna de las anteriores
        print("No has ingresado un comando valido")                                             # mensaje de comando invalido 
        time.sleep(1)                                                                           # esperar 1 segundo
        os.system("CLS")                                                                        # limpiar la terminal

"""-----------------------------------------------------------------------------------------------------------------------"""
conn.close()                                                                                    # cerrar la conexion con la base de datos
