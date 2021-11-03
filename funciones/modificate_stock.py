# fución para modificar el stock de un producto
def modificate_stock(matriz, code_modified):
    time.sleep(0.5)                                                                             # esperar 0.5 segundos
    long = len(matriz)                                                                          # obtener la longitud de la matriz
    os.system("CLS")                                                                            # limpiar la terminal

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
        matriz[pos_change][6] = get_current_time()                                              # cambiar la fecha y hora de modificacion del producto
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
        time.sleep(2)                                                                                               # esperar 2 segundos
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
        matriz[pos_change][6] = get_current_time()                                              # cambiar la fecha de modificacion
        print(
            f"El stock de {code_modified} ha sido modificado, ahora es: {matriz[pos_change][3]}")                   # mensaje de confirmacion de modificacion
        time.sleep(2)                                                                                               # esperar 2 segundos
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
