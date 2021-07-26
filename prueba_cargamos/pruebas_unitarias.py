from sitioweb import deploy_app
import unittest
from werkzeug.wrappers import response

app = app = deploy_app()


class FlaskTest(unittest.TestCase):
    """
        Clase que realiza pruebas unitarias a Flask

        Args:
            No recibe argumentos
    """
    
    def test_electronica(self):
        respuesta_test = app.test_client(self)
        respuesta = respuesta_test.get('/', content_type = 'html/text')
        self.assertEqual(respuesta.status_code, 200)
    
    def test_electronica_load(self):
        respuesta_test = app.test_client(self)
        respuesta = respuesta_test.get('/', content_type = 'html/text')
        self.assertTrue(b'Agregar' in respuesta.data)
    
    def test_agrega_producto(self):
        respuesta_test = app.test_client(self)
        respuesta = respuesta_test.post('/agregar', data=dict(sku = 999, nombre_producto = 'prueba', precio_unitario=1, cantidad=1, tipo_producto='prueba', marca= 'prueba', tienda= 5555,stock_seguridad=10, lote_pedido = 1),
                                        follow_redirects = True)
        print(respuesta)
        #self.assertIn(b'AGREGAR NUEVO',  respuesta.data)
    
    def test_stok(self):
        respuesta_test = app.test_client(self)
        respuesta = respuesta_test.get('/inventario', content_type = 'html/text')
        self.assertTrue(b'Productos' in respuesta.data)
        
if __name__ == '__main__':
    unittest.main()