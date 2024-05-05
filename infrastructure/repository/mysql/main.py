import pymysql
import dotenv
import os

class MySQLManager:
    __instance = None

    def __new__(cls):
        print("MySQLManager.__new__")
        if not cls.__instance:
            cls.__instance = super(MySQLManager, cls).__new__(cls)
            cls.__instance.db = None
            cls.__instance.__connect()
        return cls.__instance

    def __connect(self):
        print("MySQLManager.__connect")
        dotenv.load_dotenv()
        # Parámetros de conexión a la base de datos
        host = os.getenv("MYSQL_HOST")
        user = os.getenv("MYSQL_USERNAME")
        password = os.getenv("MYSQL_PASSWORD")
        database_name = os.getenv("MYSQL_DATABASE")

        # Establecimiento de la conexión
        try:
            self.db = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database_name
            )
        except pymysql.MySQLError as e:
            print(f"Error al conectar a la base de datos: {e}")

    def get_connection(self):
        print("MySQLManager.get_connection")
        if self.db:
            return self.db
        else:
            raise Exception("No se ha establecido conexión a la base de datos")

    def close(self):
        if self.db:
            self.db.close()
            self.db = None




if __name__ == "__main__":
    manager = MySQLManager()

    print("Testing Conexion...")

    want_exit = False
    while(want_exit == False):
        cnx = manager.get_connection()
        print("Conexion:", cnx)

        r = input("Exit? Y/N")

        if (r == "Y" or r == "y"):
            want_exit = True