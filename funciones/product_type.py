# funcion para filtrar los productos por tipo
def product_type(matriz):
    type_product = input(
        "Ingrese la categoria de producto por el que desea filtrar: ")                          # capturar el tipo de producto para filtrar
    a = len(matriz)                                                                             # obtener la longitud de la matriz
    lista = list()                                                                              # crear una lista
    for i in range(a):                                                                          # recorrer la matriz
        if (matriz[i][2]).upper() == (type_product).upper():                                    # si el tipo de producto es igual al tipo de producto capturado
            lista.append(matriz[i])                                                             # agregar el producto a la lista
    if len(lista) != 0:                                                           
        c = pandas.DataFrame(
            lista, columns=["code", "name", "type", "stock", "repos", "price", "last_update"])  # generar la matriz en formato pandas
        os.system('CLS')                                                                        # limpiar la terminal
        print(c)                                                                                # imprimir la matriz de productos
        print(" ")
        decition = input(
            "Cuando desee regresar al menú principal ingrese cualquier tecla: ")                # volver al menu principal
        os.system('CLS')                                                                        # limpiar la terminal
        time.sleep(1)                                                                           # esperar 1 segundo
    else:
        print("No se encontraron productos con ese tipo")                                       # mensaje de error
        time.sleep(1)                                                                           # esperar 1 segundo
        os.system("CLS")                                                                        # limpiar la terminal
        print(colored("- 1.", "blue", attrs=["bold"]), "Volver a intentar ")                    # mensaje de volver a intentar
        print(colored("- 2.", "blue",
                      attrs=["bold"]), "Volver al menú principal")                              # mensaje de volver al menu principal
        choose = (input("Ingrese una opción: ")).upper()                                        # capturar la opcion

        if choose == "1":                                                                       # si la opcion es 1
            product_type(matriz)                                                                # volver a intentar

        elif choose == "2":                                                                     # si la opcion es 2
            time.sleep(1)                                                                       # esperar 1 segundo
            os.system("CLS")                                                                    # limpiar la terminal