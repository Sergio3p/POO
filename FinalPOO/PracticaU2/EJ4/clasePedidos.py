class Pedidos:
    __patente: str
    __id_pedidos: int
    __comida: str
    __tiempo_estimado: int
    __tiempo_real: int
    __precio_pedido: float

    def __init__(self,patente,id_pedidos,comida,tiempo_estimado,tiempo_real,precio_pedido):
        self.__patente = patente
        self.__id_pedidos = id_pedidos
        self.__comida = comida
        self.__tiempo_estimado = tiempo_estimado
        self.__tiempo_real = tiempo_real
        self.__precio_pedido = precio_pedido
    
    def get_patente(self):
        return self.__patente
    
    def get_id_pedidos(self):
        return self.__id_pedidos
    
    def get_comida(self):
        return self.__comida
    
    def get_tiempo_estimado(self):
        return self.__tiempo_estimado
    
    def get_tiempo_real(self):
        return self.__tiempo_real
    
    def get_precio_pedido(self):
        return self.__precio_pedido
    
    def set_tiempo_real(self, value):
        self.__tiempo_real = value
    
    def __lt__(self,other):
        return self.__patente < other.get_patente()

    def __str__(self):
        return f"Patente: {self.__patente}, ID Pedidos: {self.__id_pedidos}, Comida: {self.__comida}, Tiempo Estimado: {self.__tiempo_estimado} min, Tiempo Real: {self.__tiempo_real} min, Precio Pedido: ${self.__precio_pedido}"