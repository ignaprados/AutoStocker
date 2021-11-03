# funcion para alertar si hay que reponer un producto
def alert(matriz):
    time.sleep(0.2)                                                                                                             # esperar 0.2 segundos
    os.system("CLS")                                                                                                            # limpiar la terminal                   
    to_repos = list()                                                                                                           # crear una lista para los productos a reponer
    codes_to_repos = list()                                                                                                     # crear una lista para los codigos de los productos a reponer
    for i in range(len(matriz)):                                                                                                # recorrer la matriz
        if int(matriz[i][3]) <= int(matriz[i][4]):                                                                              # si el stock es menor o igual al reposicion
            to_repos.append(matriz[i])                                                                                          # agregar el producto a la lista
            codes_to_repos.append(matriz[i][0])                                                                                 # agregar el codigo del producto a la lista
    to_repos = pandas.DataFrame(to_repos, columns=["code", "name", "type", "stock", "repos", "price", "last_update"])           # generar la matriz en formato pandas
               
    if len(codes_to_repos) > 0:                                                                 # si hay productos a reponer
        print("Los codigos a reponer son: ")                                                    # mensaje de los codigos a reponer
        for i in codes_to_repos:                                                                # recorrer la lista de codigos a reponer
            print(i, end=" ")                                                                   # imprimir los codigos a reponer
        print("")
        print("-----------------------------")
        print(" ")
        print(to_repos)                                                                         # imprimir la matriz de productos a reponer
        print(" ")
        a = input("Ingrese una tecla cuando desee volver al menu principal: ")                  # volver al menu principal
        os.system('CLS')                                                                        # limpiar la terminal
    else:
        print("No hay ningun codigo a reponer por el momento.")                                 # mensaje de error
        os.system('CLS')                                                                        # limpiar la terminal
