from flask import Blueprint, render_template
from .funciones import Funciones
import psycopg2
from .querrys import OBTIENE_DATOS_PRODUCTO, OBTIENE_TIENDAS
import asyncio

views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    """
    Metodo de la pantalla principal muestra la informacion de los productos
    en la pantalla principal

    Args:
        No recibe argumentos
    """
    db = Funciones()
    connex = db.abre_conexion()
    todos_datos = db.ejecuta_selects(OBTIENE_DATOS_PRODUCTO, connex)
    todas_tiendas = db.ejecuta_selects(OBTIENE_TIENDAS, connex)
    db.cierra_coneccion(connex)
    print(todos_datos)
    return render_template("electronica.html", productos_todos = todos_datos, 
                            tiendas = todas_tiendas)

