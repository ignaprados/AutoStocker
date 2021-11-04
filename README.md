![banner](https://raw.githubusercontent.com/IgnacioPrados/AutoStocker/master/banner.png)
# Documentación AutoStocker
---

## Developers:

* Ocampo Denise - _Chief information Officer_ :iphone:
* Endendyk Victoria - _Client-based_ program tester 🛠️
* Prados Ignacio - _Chief Technology Officer_ :computer:
* Pedaccio Facundo - _Database Engineer and Technoking_ :rocket:



## Indice:
1. Introducción
2. Librerías utilizadas
3. Interfaz de usuario
4. Estructura de almacenamiento de datos
5. Carga de datos
6. Estructura general del programa
7. Funciones



---

### 1. Introduccion:
Autostocker es un programa basado en consola que utiliza una base de datos SQL. Este programa tiene una interfaz sencilla, rápida e intuitiva para el manejo de la información. Lo que buscamos es que el potencial cliente que decida adquirir este producto pueda tener un fácil manejo del sistema con funciones enfocadas a sus necesidades, y así obtener un crecimiento exponencial dentro de su empresa/negocio.
>[Ver Documentación en la web](https://autostocker.vercel.app)





---

### 2. Librerias utilizadas:


#### SQLite3:
[Documentación oficial SQLite3](https://docs.python.org/es/3/library/sqlite3.html)

> SQL es un lenguaje de consulta estructurada, diseñado para manejar sistemas de bases de datos relacionales. SQL es muy popular por su facilidad de uso y efectividad para convertir grandes volúmenes de datos en información útil.


> SQLite es una biblioteca de C que provee una base de datos ligera basada en disco que no requiere un proceso de servidor y permite acceder a la base de datos utilizando una variación del lenguaje de querys de SQL.


> SQLite3 brinda una interfaz de SQLite dentro de Python. Nos permite conectarnos a una base de datos, ejecutar consultas (querys) con la sintaxis de SQLite. Esta librería no requiere instalación ya que es nativa de Python.


#### Pandas:
[Documentación oficial Pandas](https://pandas.pydata.org/docs/)
> Es una biblioteca escrita como extensión de Numpy para manipulación y análisis de datos para el lenguaje de programación Python. Decidimos utilizarlo en nuestro código ya que podemos acceder  al DataFrame, el cual es una estructura de datos con filas y columnas ordenadas. 
> En este programa fue utilizado para convertir las tablas almacenadas en nuestra base de datos a un objeto DataFrame de Pandas. Ese objeto DataFrame luego es convertido a una lista de listas de Python. También utilizamos DataFrame para mostrar las matrices de datos cuando el usuario lo requiera. Sera explicado en la sección **_carga de datos_**.
##### Instalación:

Pandas deberá ser instalado usando el siguiente comando en el símbolo del sistema (CMD).
```
pip install numpy
```
Previamente instalando Numpy con el siguiente comando:

```
pip install pandas
```


#### Datetime:
[Documentación oficial Datetime](https://docs.python.org/es/3/library/datetime.html)
> La librería datetime permite manipular fechas y horas. Es utilizado en este programa para obtener la fecha y hora en el momento que se ejecute algún cambio en la matriz de datos o para mostrar el horario en el menú principal. Explicaremos su funcionamiento en la sección de funciones. Esta librería no requiere instalación ya que es nativa de Python.

#### Os:
[Documentación oficial OS](https://docs.python.org/3/library/os.html)
> Os es una librería nativa de Python que te permite interactuar con el sistema operativo. En este programa es utilizado para limpiar la terminal donde el usuario va haciendo pedidos y viendo data. De esta forma se logra una interfaz de usuario en consola más limpia.


#### Time: 
[Documentación oficial Time](https://docs.python.org/es/3/library/time.html)

> Time es un modulo que proporciona varias funciones relacionadas con el tiempo. La más utilizada en nuestro código es el método sleep(secs) que sirve para pausar la ejecución del hilo de llamada durante el número de segundos proporcionados en el argumento secs. Por lo tanto, necesitamos llamar al método time.sleep() para hacer que el programa se duerma durante un tiempo especifico.


#### Termcolor:
[Documentación oficial Termcolor](https://pypi.org/project/termcolor/)

> Esta librería lo que nos permite hacer es cambiar el color del texto. Nosotros importamos colored de termcolor, esto es más que nada para la estética del programa, logrando destacar los números de nuestro programa principal.

##### Instalación:

Termcolor deberá ser instalado usando el siguiente comando en el símbolo del sistema (CMD)

```
pip install termcolor
```

---

### 3. Interfaz de usuario:
La interfaz de usuario que desarrollamos para este programa es una command line based UI. Es decir que es una interfaz en la terminal. 


Elegimos este tipo de interfaz por su sencillez y rapidez. La interfaz es fácil de memorizar, y así agilizar el uso repetitivo en el día a día del usuario. También agregamos colores, mensajes que responden a lo que se está haciendo, y pequeños delays para que los movimientos dentro de la interfaz sean más suaves.

![](https://i.imgur.com/NbnCy3B.png)


---
### 4. Estructura de almacenamiento de datos:

Optamos por usar un modelo de base de datos relacional que cuenta con dos tablas (productos, registros) 

#### Matriz de Productos:
![](https://i.imgur.com/MEa1glP.png)

> Para AutoStocker decidimos registrar para cada producto el nombre, tipo de producto, número de stock, de reposición, última fecha de actualización de la carga del los datos y el precio de los productos.

#### Matriz de Registros:
![](https://i.imgur.com/BYmj60w.png)
> En la parte de registros, optamos por almacenar en cada uno de los ajustes el código del producto, la variación del stock, el motivo por el cual se realiza el cambio, y la fecha y hora de actualización (timestamp).
> 
---
### 5. Carga y guardado de datos:

En el programa la carga de datos se realiza desde el archivo de la base de datos (database.db) hacia el programa con el siguiente código:
```py
conn = sqlite3.connect('./database.db')                                                         
matrixpandas = pandas.read_sql_query("SELECT * FROM productos", conn)                           
matriz = matrixpandas.values.tolist()                                                           
registros = pandas.read_sql_query("SELECT * FROM registros", conn)                         
registros = registros.values.tolist()  
```

Es decir que utilizamos la librería sqlite3 para conectarnos a la base de datos, luego usamos pandas para ejecutar el pedido SQL ("SELECT * FROM productos") con el método de pandas "pandas.read_sql_query" que convierte toda la matriz en un archivo DataFrame. Y por último convertimos ese DataFrame a una lista de listas de Python con el "matrixpandas.values.tolist()".
Para guardar los datos desde el programa hacia la base de datos primero convertimos la matriz (lista de listas) en un objeto DataFrame de pandas. Y después utilizamos el método ("df.to_sql") para guardar ese objeto DataFrame en la base de datos. 

---
### 6. Estructura general del programa:
<img src="https://raw.githubusercontent.com/IgnacioPrados/AutoStocker/master/Flowchart%20AutoStocker%20(1).png">

---
### 7. Funciones:


#### Función para imprimir la matriz de productos:

> Esta función sirve para imprimir la matriz de los productos que decida incorporar el usuario dentro de la base de datos. La matriz es guardada e impresa como  dataframe de pandas y el formato de impresión sera visto luego en el menú principal del programa al presionar la opción 1 que es la que permite imprimir la data completa.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/print_data.py)

#### Función para imprimir la matriz de registros:

> Esta función sirve para imprimir la matriz de registros donde se podra visualizar los ajustes realizados dentro de la base de datos. Al igual que en la función para imprimir los productos, la matriz es impresa y guardada como un dataframe de pandas.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/print_registros.py)

#### Función para consultar el stock de un producto:

> Esta función sirve para que el usuario pueda consultar el stock actual de un producto. La función se encarga de buscar el producto y determinar si se encontró o no dentro de la matriz. Si se encontró el código, imprime el stock del producto y vuelve al menú principal al presionar cualquier letra. Si no se encontró el código, devuelve un mensaje de error.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/product_stock.py)


#### Función para filtrar los productos por tipo:

> Esta función sirve para filtrar los productos por categoría. La función se encarga de recorrer la matriz y comparar si el tipo de producto que aparece en cada fila es igual al tipo de producto capturado. Si es así, se crea una lista vacía en donde se van a ir agregando todos aquellos productos relacionados a la categoría que ingreso el usuario para luego imprimir la matriz en formato pandas mostrando los productos según como se quiera filtrar.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/product_type.py)

#### Función para agregar la fecha y hora de ultima actualizacion:
> Esta función se encarga de, a partir de una función de la librería datetime, tomar el horario y fecha actual de la computadora y retornarla. Se la llama a esta función para visualizar la fecha y hora en la que se han hecho movimientos o cambios dentro de la matriz de productos o de registros. 
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/get_current_time.py)

#### Función para agregar un nuevo producto:
> Esta función sirve para agregar un nuevo producto. La función crea una lista para almacenar los datos del nuevo producto agregando el nombre, tipo de producto, stock inicial, punto de reposición y el precio. Una vez que se tienen todos los datos del nuevo producto, con un append agregamos la lista a la matriz de la base de datos.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/add_new_product.py)


#### Función para eliminar producto:
> Esta función se encarga de eliminar un producto a partir del código de producto que ingresa el usuario como input. La función con un index obtiene la posición del código que se desea eliminar, y si lo encuentra, lo elimina avisando con anterioridad que el código ha sido encontrado y se guarda la nueva matriz en la base de datos como un dataframe. Si no se encuentra el código, devuelve un mensaje de que el código no es correcto.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/delete_product.py)



#### Función para editar un producto: 
> Esta función se encarga de editar el producto que el usuario desee modificar. Una vez que el programa reconoce el código y lo compara con la matriz para ver si se encuentra, devuelve que el producto ha sido encontrado. Cuando finalmente se encuentra se puede modificar el nombre, precio, stock, código, categoría y punto de reposición. Si no se encuentra, la función devuelve que el código no se encontró y limpia la terminal.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/update_product.py) 

#### Función para modificar el stock de un producto:
> Esta función sirve para modificar el stock de un producto a partir del código del producto del usuario. Realiza comprobaciones de si el código existe. Esta función forma parte de la función para editar un producto.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/modificate_stock.py)

#### Función para alertar sobre los productos a reponer:

>Esta función imprime los códigos y las filas donde el stock sea menor o igual al punto de reposición.
>> [Ver código](https://github.com/IgnacioPrados/AutoStocker/blob/master/funciones/alert.py)



<footer style="text-align: center; margin-top: 60px; font-weight: 600;">
    <div style="background-color: #614ad9; border-radius: 15px; padding-top: 10px;padding-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1)">
        <p style="margin:0;color: #FFF !important">© 2021 | AutoStocker </p>
    </div>
</footer>
