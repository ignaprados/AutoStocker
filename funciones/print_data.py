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