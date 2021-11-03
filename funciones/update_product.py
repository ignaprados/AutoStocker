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
                time.sleep(2)                                                                   # esperar 2 segundos
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
            matriz[pos][6] = get_current_time()                                                 # cambiar la fecha y hora de modificacion del producto
            print(" ")
            print("El nombre del producto fue modificado")                                      # mensaje de nombre modificado
            time.sleep(1.5)                                                                     # esperar 1.5 segundos
            print(" ")

        elif choose == "2":                                                                     # si la opcion es 2
            price = input("Ingrese el nuevo precio: ")                                          # capturar el nuevo precio
            matriz[pos][5] = price                                                              # cambiar el precio del producto
            matriz[pos][6] = get_current_time()                                                 # cambiar la fecha y hora de modificacion del producto
            print(" ")
            print("El precio del producto fue modificado")                                      # mensaje de precio modificado
            time.sleep(1.5)                                                                     # esperar 1.5 segundos
            print(" ")

        elif choose == "3":                                                                     # si la opcion es 3
            modificate_stock(matriz, code)                                                            # llamar a la funcion modificar stock
        elif choose == "4":                                                                     # si la opcion es 4
            code = input("Ingrese el nuevo codigo del producto: ")                              # capturar el nuevo codigo
            matriz[pos][0] = code                                                               # cambiar el codigo del producto
            matriz[pos][6] = get_current_time()                                                 # cambiar la fecha y hora de modificacion del producto
            print(" ")
            print("El codigo del producto fue modificado")                                      # mensaje de codigo modificado
            time.sleep(1.5)                                                                     # esperar 1.5 segundos
            print(" ")
        elif choose == "5":                                                                     # si la opcion es 5
            category = input("Ingrese la nueva categoria: ")                                    # capturar la nueva categoria
            matriz[pos][2] = category                                                           # cambiar la categoria del producto
            matriz[pos][6] = get_current_time()                                                 # cambiar la fecha y hora de modificacion del producto
            print(" ")
            print("La categoria del producto fue modificada")                                   # mensaje de categoria modificada
            time.sleep(1.5)                                                                     # esperar 1.5 segundos
            print(" ")

        elif choose == "6":                                                                     # si la opcion es 6
            repos = input("Ingrese el nuevo punto de reposicion: ")                             # capturar el nuevo punto de reposicion
            matriz[pos][4] = repos                                                              # cambiar el punto de reposicion del producto
            matriz[pos][6] = get_current_time()                                                 # cambiar la fecha y hora de modificacion del producto
            print(" ")
            print("El punto de reposicion del producto fue modificado")                         # mensaje de punto de reposicion modificado
            time.sleep(1.5)                                                                     # esperar 1.5 segundos
            print(" ")
        os.system("CLS")                                                                        # limpiar la terminal
    else:                                                                                       # si el codigo no fue encontrado
        print("El codigo no se encontro")                                                       # mensaje de codigo no encontrado
        time.sleep(1.5)                                                                         # esperar 1.5 segundos
        os.system("CLS")                                                                        # limpiar la terminal
        update_product(matriz)
    
    df = pandas.DataFrame(matriz)                                                               # convertir la matriz en un dataframe
    df.to_sql('productos', conn, if_exists='replace', index=False)                              # guardar los datos en la base de datos
