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
