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