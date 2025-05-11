from conexion import Conexion
from producto import Producto

class GestionInventarioDAO:
    #Creamos las querys que usaremos en el programa
    SELECCIONAR = "SELECT * FROM producto ORDER BY nombre"
    INSERTAR = "INSERT INTO producto(nombre, precio, categoria, cantidad) VALUES(%s, %s, %s, %s)"
    ACTUALIZAR = "UPDATE producto SET precio=%s, cantidad=%s WHERE nombre =%s"
    ELIMINAR = "DELETE FROM producto WHERE nombre =%s"

    @classmethod
    #Creamos metodo para mostar por pantalla la lista de productos
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            #selecionamos todos los productos
            cursor.execute(cls.SELECCIONAR)

            #Seleccionamos todos los registros de productos y los comvertirá en objetos
            # de tipo producto
            registros = cursor.fetchall()

            #Mapeo de clase-tabla prducto
            productos = []
            for registro in registros:
                #Recuperamos cada producto con sus atributos, creando un objeto tipo producto
                producto = Producto(registro[0], registro[1], registro[2], registro[3])
                #Añadimos cada producto a la lista de productos
                productos.append(producto)

            #Recuperamos la lista de productos
            return productos
        
        except Exception as e:
            print(f"Ocurrio un error al seleccionar productos: {e}")

        finally:
            if conexion is not None:
                #liberamos la conexion despues de usarlo
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    #Añadimos metodo para añadir los nuevos productos a la base de datos
    def insertar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            #Creamos tupla para indicar los atributos que vamos a introducir en la bd
            valores = (producto.get_nombre(), producto.get_precio(), producto.get_categoria(), producto.get_cantidad() )

            #Ejecutamos la consulta de insertar
            cursor.execute(cls.INSERTAR, valores)

            #Guardamos los cambios en la bd
            conexion.commit()

            #Indicamos cuantos valores se registraron
            return cursor.rowcount
        
        except Exception as e:
            print(f"Ocurrio un error al añadir producto: {e}")

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    #Creamos metodo para que el usuario pueda escribir los datos del nuevo producto
    def pedir_datos_producto(self):
        while True:
            nombre = input("Introduce el nombre del nuevo producto: ").strip().lower()
            if not nombre:
                print("No debe estar vacío. Pruebe de nuevo.")
                continue
            break

        while True:
            try:
                precio = float(input("Introduce el precio: "))
                if precio > 0:
                    break
                else:
                    print("Introduce un precio correcto, debe ser un número positivo.")
            except ValueError:
                print("Introduce un número válido.")

        while True:
            categoria = input("Introduce la categoría del nuevo producto: ").strip().lower()
            if not categoria:
                print("No debe estar vacío. Pruebe de nuevo.")
                continue
            break

        while True:
            try:
                cantidad = int(input("Introduce la cantidad: "))
                if cantidad >= 0:
                    break
                else:
                    print("Introduce una cantidad igual o mayor a cero.")
            except ValueError:
                print("Introduce un número válido.")

        return Producto(nombre, precio, categoria, cantidad)

    @classmethod
    #Creamos metodo para actualizar precio y cantidad de los productos creados
    def actualizar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            #Los valores van en este orden, viene dado por la query ACTUALIZAR
            valores = (producto.get_precio(), producto.get_cantidad(), producto.get_nombre())
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            
            return cursor.rowcount
        
        except Exception as e:
            print(f"Ocurrio un error al actualizar el producto: {e}")

        finally:
            if conexion is not None:
                #liberamos la conexion despues de usarlo
                cursor.close()
                Conexion.liberar_conexion(conexion)

           
    #Creamos un método para actualizar el precio y/o la cantidad
    def actualizar_producto_por_nombre(self):
        #Pedimos al usuario que escriba el nombre del producto
        nombre_producto = input("Introduce el nombre del producto que deseas actualizar: ").strip().lower()

        #Recorremos la lista de productos del inventario para ver si alguno coincide con el nombre introducido por el usuario
        #Si hay coincidencia, con next conseguimos añadirlo a producto_encontrado. Si no hay coincidencia producto_encontrado estaría vacio
        productos = GestionInventarioDAO.seleccionar()
        producto_encontrado = next((p for p in productos if p.get_nombre() == nombre_producto), None)

        #Si no está, indicamos al usuario que no se ha actualizado
        if not producto_encontrado:
            print("No se ha encontrado el producto. Volviendo al menú principal")
            return
        
        #Actualizamos precio si el producto está en el inventario
        while True:
            try:
                #Solicitamos nuevo precio, asegurando que introduce un precio correcto
                nuevo_precio = float(input(f'Precio actual:{producto_encontrado.get_precio()}€. Introduce el nuevo precio: '))
                if nuevo_precio > 0:
                    break
                else:
                    print("El nuevo precio debe ser un numero positivo. Prueba de nuevo")
            except ValueError:
                print("El nuevo precio debe ser un numero positivo. Prueba de nuevo")
        
        #Actualizamos cantidad si el producto está en el inventario
        while True:
            try:
                #Solicitamos nueva cantidad, asegurando que introduce un número correcto
                nueva_cantidad = int(input(f'Cantidad actual: {producto_encontrado.get_cantidad()} unidades. Introduce la nueva cantidad: '))
                if nueva_cantidad >= 0:
                    break
                else:
                    print("La nueva cantidad no puede ser negativa. Prueba de nuevo")
            except ValueError:
                print("La nueva cantidad debe ser un numero igual o mayor a cero. Prueba de nuevo")

        #Creamos un objeto del producto actualizado
        producto_actualizado = Producto(producto_encontrado.get_nombre(), nuevo_precio, producto_encontrado.get_categoria(), nueva_cantidad)

        #Llamamos al metodo actualizar para cambiar la base de datos
        filas_afectadas = GestionInventarioDAO.actualizar(producto_actualizado)

        if filas_afectadas:
            print(f"Producto actualizado correctamente: {producto_actualizado}")
        else:
            print("No se pudo actualizar el producto.")

    @classmethod
    #Creamos metodo para elimimar productos
    def eliminar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            #Terminar con una , para que sea una tupla
            valores = (producto.get_nombre(),)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrio un error al eliminar el producto: {e}")

        finally:
            if conexion is not None:
                #liberamos la conexion despues de usarlo
                cursor.close()
                Conexion.liberar_conexion(conexion)

    #Creamos metodo para eliminar producto por nombre
    def eliminar_por_nombre(self):
        #Pedimos al usuario que escriba el nombre del producto
        nombre_producto = input("Introduce el nombre del producto que deseas eliminar: ").strip().lower()   
        
        #Buscamos el producto en la bd
        productos = GestionInventarioDAO.seleccionar()
        producto_encontrado = next((p for p in productos if p.get_nombre() == nombre_producto), None)

        #Si no está, indicamos al usuario que no se ha encontrado
        if not producto_encontrado:
            print("No se ha encontrado el producto. Volviendo al menú principal")
            return
        
        filas_afectadas = GestionInventarioDAO.eliminar(producto_encontrado)

        if filas_afectadas:
            print(f"Producto eliminado correctamente: {producto_encontrado}")
        else:
            print("No se pudo actualizar el producto.")
        
        
    #Creamos metodo para buscar un producto
    def buscar_producto(self):
        #Pedimos al usuario que escriba el nombre del producto
        nombre_producto = input("Introduce el nombre del producto que deseas buscar: ").strip().lower()   
        
        #Buscamos el producto en la bd
        productos = GestionInventarioDAO.seleccionar()
        producto_encontrado = next((p for p in productos if p.get_nombre() == nombre_producto), None)

        #Si no está, indicamos al usuario que no se ha encontrado
        if not producto_encontrado:
            print("No se ha encontrado el producto. Volviendo al menú principal")
            return
        if producto_encontrado:
            print(producto_encontrado)






