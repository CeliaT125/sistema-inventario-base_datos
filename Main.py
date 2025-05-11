from gestioninventarioDAO import GestionInventarioDAO


#Creamos el menu interactivo
def menu():

    dao = GestionInventarioDAO()

    while True:
        print(""" 
              ---MENU DEL INVENTARIO---
              
              1. Agregar un producto
              2. Mostrar lista del inventario
              3. Buscar un producto
              4. Actualizar un producto
              5. Eliminar un producto
              6. Salir""")

        opcion = input("""
              Elija una opción (del 1 al 5): """)
        
        if opcion == "1":
            producto = dao.pedir_datos_producto() 
            productos_insertados = dao.insertar(producto)
            print(f"Producto añadido: {productos_insertados}")

        elif opcion == "2":
            productos = dao.seleccionar()
            #Mostramos los productos por pantalla
            for producto in productos:
                print(producto) 
            if not productos:
                print("No hay productos en el inventario.")
    
        elif opcion == "3":
            dao.buscar_producto()

        elif opcion == "4":
            dao.actualizar_producto_por_nombre()

        elif opcion == "5":
            dao.eliminar_por_nombre()

        elif opcion == "6":
            print("Salimos del programa")
            break
                
        else:
            print("Introduce una opción válida.")


if __name__ == "__main__":
    menu()