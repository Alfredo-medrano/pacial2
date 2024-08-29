class producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
    def act_Stock(self,cantidad):
        
        self.cantidad -= cantidad