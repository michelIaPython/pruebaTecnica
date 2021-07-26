OBTIENE_DATOS_PRODUCTO = '''SELECT * FROM public.producto'''
AGREGA_PRODUCTO = '''INSERT INTO public.producto(
	sku, nombre_producto, precio, cantidad, tipo, marca, id_tienda,stock_seguridad, lote_pedido)
	VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)'''
AGREGAR_TIENDA = '''INSERT INTO public.tienda(
	id_tienda, nombre_tienda, direccion, telefono, ciudad, cp)
	VALUES (%s, %s, %s, %s, %s, %s);''' 
OBTIENE_INVENTARIO = '''SELECT sku,nombre_producto,cantidad,stock_seguridad, lote_pedido FROM producto'''
OBTIENE_TIENDAS = '''SELECT * FROM public.tienda'''