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
    ajuste = [code, "Se añadió un producto",                                                   
              "Producto agregado", get_current_time()]                                          # crear una lista para almacenar los datos del ajuste

    registros.append(ajuste)                                                                    # agregar el ajuste a la matriz de registros

    df = pandas.DataFrame(registros)                                                            # generar la matriz en formato pandas
    df.to_sql('registros', conn, if_exists='replace', index=False)                              # almacenar la matriz de registros en la base de datos

