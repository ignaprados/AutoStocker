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
            time.sleep(1.5)                                                                     # esperar 1.5 segundos
            os.system('CLS')                                                                    # limpiar la terminal
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
