from conexion import Conexion

class Ventas(Conexion):
    
    productos = []

    def __init__(self):
        self.conectar('localhost', 27017, 'pos', 'registros')

    def registrar_producto(self, item, quantity, value, cedula = 00000000):
        
        print(value)

        iva = value * 0.19
        print(iva)
        
        total = float(iva) + float(value) 
        print(total)

        self.productos.append(
            {
            'Producto': item,
            'Producto': quantity,
            'Cedula': cedula, 
            'Valor': value,
            'IVA': iva,
            'TOTAL': total
            }
        )
    
    def __del__(self):
        
        self.guardar( self.productos )


        


