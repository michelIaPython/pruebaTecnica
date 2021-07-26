from flask import Blueprint, render_template
import psycopg2
from .funciones import Funciones
from .querrys import OBTIENE_INVENTARIO

inventarios = Blueprint('inventarios', __name__)

@inventarios.route('/inventario')
def muestra_inventarios():
    """
    Metodo que muestra el inventario

    Args:
        Esta funcion no resibe parametros
    """
    db = Funciones()
    lista_stock = []
    connex = db.abre_conexion()
    inventario = db.ejecuta_selects(OBTIENE_INVENTARIO, connex)
    db.cierra_coneccion(connex)
    for cada_elemento in inventario:
        stock = int(cada_elemento[3]) + int(cada_elemento[4]/2)
        if int(cada_elemento[2]) < stock:
            lista_stock.append(cada_elemento)
    print(lista_stock)
    return render_template("inventarios.html", stocks = lista_stock)