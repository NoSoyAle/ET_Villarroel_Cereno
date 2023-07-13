class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito

    def agregar(self, tienda):
        if tienda.codigo not in self.carrito.keys():
            self.carrito[tienda.codigo]={
                "tienda_id":tienda.codigo,
                "descripcion": tienda.descripcion,
                "precio": str(tienda.precio),
                "cantidad": 1,
                "total" : tienda.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key== tienda.codigo:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = tienda.precio
                    value["total"] = value["total"] + tienda.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, tienda):
        id = tienda.codigo
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar (self, tienda):
        for key, value in self.carrito.items():
            if key == tienda.codigo:
                value["cantidad"] = value ["cantidad"] - 1
                value["total"] = int(value["total"]) - tienda.precio
                if value["cantidad"] < 1:
                    self.eliminar(tienda)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified = True
        
