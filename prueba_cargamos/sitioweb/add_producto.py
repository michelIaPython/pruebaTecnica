from flask import Blueprint, render_template, request, flash
import psycopg2
from .funciones import Funciones
from .querrys import AGREGA_PRODUCTO, AGREGAR_TIENDA

add_producto = Blueprint('add_producto', __name__)

@add_producto.route('/agregar', methods=['GET','POST'])
def nuevo_producto():
    """
        Metodo que agrega un producto a la base

        Args:
            No recibe argumentos
    """
    if request.method == 'POST':
        valores = ()
        lista_valores = []
        db = Funciones()
        sku = request.form.get('sku')
        nompre_producto = request.form.get('nombre_p')
        precio_unitario = request.form.get('precio_u')
        cantidad = request.form.get('cantidad')
        tipo_producto = request.form.get('tipo_prod')
        marca = request.form.get('marca')
        tienda = request.form.get('tienda')
        stock_seguridad = request.form.get('stock_seguridad')
        lote_pedido = request.form.get('lote_pedido')
        lista_valores = [sku,nompre_producto,precio_unitario,cantidad,
                        tipo_producto,marca,tienda,stock_seguridad, lote_pedido]
        valores = tuple(lista_valores)
        if sku == '':
            flash("Debe estar lleno el campo SKU", category = "error")
        elif nompre_producto == '':
            flash("Debe estar lleno el campo NOMBRE PRODUCTO", 
                  category = "error")
        elif precio_unitario == '':
            flash("Debe estar lleno el campo PRECIO UNITARIO", 
                  category = "error")
        elif cantidad == '':
            flash("Debe estar lleno el campo CANTIDAD", category = "error")
        elif tipo_producto == '':
            flash("Debe estar lleno el campo TIPO PRODUCTO", category = "error")
        elif marca == '':
            flash("Debe estar lleno el campo MARCA", category = "error")
        elif tienda == '':
            flash("Debe estar lleno el campo TIENDA", category = "error")
        else:
            connex = db.abre_conexion()
            todos_datos = db.ejecuta_inserts(AGREGA_PRODUCTO, connex , valores)
            db.cierra_coneccion(connex)    
            flash("Producto agregado correctamente", category = "success")
        
    return render_template("productos.html")


@add_producto.route('/agregar_tienda', methods=['GET','POST'])
def nueva_tienda():
    
    """
        Metodo que agrega una tienda a la base

        Args:
            No recibe argumentos
    """
    
    if request.method == 'POST':
            valores = ()
            lista_valores = []
            db = Funciones()
            id_tienda = request.form.get('id_tienda')
            nompre_tienda = request.form.get('tienda')
            dirreccion = request.form.get('direccion')
            telefono = request.form.get('telefono')
            ciudad = request.form.get('ciudad')
            cp = request.form.get('tienda_cp')
            lista_valores = [id_tienda,nompre_tienda,dirreccion,telefono,
                             ciudad,cp]
            valores = tuple(lista_valores)
            if id_tienda == '':
                flash("Debe estar lleno el campo SKU", category = "error")
            elif nompre_tienda == '':
                flash("Debe estar lleno el campo NOMBRE PRODUCTO", 
                      category = "error")
            elif dirreccion == '':
                flash("Debe estar lleno el campo PRECIO UNITARIO", 
                      category = "error")
            elif telefono == '':
                flash("Debe estar lleno el campo CANTIDAD", category = "error")
            elif ciudad == '':
                flash("Debe estar lleno el campo TIPO PRODUCTO", 
                      category = "error")
            elif cp == '':
                flash("Debe estar lleno el campo MARCA", category = "error")
            else:
                connex = db.abre_conexion()
                todos_datos = db.ejecuta_inserts(AGREGAR_TIENDA, connex , 
                                                valores)
                db.cierra_coneccion(connex)
                flash("Producto agregado correctamente", category = "success")    
    return render_template("tiendas.html")

