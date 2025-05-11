from mysql.connector import pooling
from mysql.connector import Error


class Conexion:
    host = "localhost"
    username = "root"
    password = "admin"
    database = "inventario_db"
    db_port = "3306"
    pool_size = 5
    pool_name = "inventario_pool"
    pool = None 

    @classmethod
    #Añadimos metodo para crear el pool de conexiones si no esta creado
    def obtener_pool(cls):
        if cls.pool is None: 
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.pool_name,
                    pool_size = cls.pool_size,
                    host = cls.host,
                    port = cls.db_port,
                    database = cls.database,
                    user = cls.username,
                    password = cls.password
                )
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al obtener pool: {e}")

        else: 
            return cls.pool        

    @classmethod
    #Metodo para crear las conexiones
    def obtener_conexion(cls):
            return cls.obtener_pool().get_connection()
    
    @classmethod
    #Metodo para cerrar las conexiones cuando el usuario termine de conectarse a la bd
    def liberar_conexion(cls, conexion):
         conexion.close()

if __name__ == "__main__":
    #Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    #Creamos un objeto tipo conexion
    conexion1 = pool.get_connection()
    print(conexion1)
    #Liberamos el objeto conexion creado
    Conexion.liberar_conexion(conexion1)
    print("Se ha liberado la conexion1")

    