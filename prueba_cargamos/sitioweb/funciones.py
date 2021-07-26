import psycopg2
import asyncio
import asyncpg

class Funciones():
    def ejecuta_selects(self, query, conn):
        
        """
        Metodo que ejecuta consulta selects en la base de datos

        Args:
            :param arg1: Consulta de SQL
            :param arg2: Conexion a la base de datos ya abierta
        """
        cursor = conn.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    
    def ejecuta_inserts(self, query, conn , valores):
        
        """
        Metodo que ejecuta consulta inserts en la base de datos

        Args:
            :param arg1: Consulta de SQL
            :param arg2: Conexion a la base de datos ya abierta
            :param arg3: Valores que se van a insertar en la base

        """
        
        cursor = conn.cursor()
        cursor.execute(query, valores)
        conn.commit()
        conn.close()
        
    def abre_conexion(self):
        
        """
        Metodo que abre conexion a la vase de datos de postgres

        Args:
            No recibe argumentos
        """
        conexion = psycopg2.connect(dbname = "electronica",
                                user = "postgres" ,
                                password = "123",
                                host ="localhost",
                                port = "5432")
        return conexion
    
    async def cierra_coneccion(self, conexion):
        await conexion.close()
        