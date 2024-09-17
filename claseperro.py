
print("Clase version 2 el constructor")
class Perro:
    #Funcion contructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    #funciones creadas por el usuario
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"Chat perro: {mensaje}")
    def chatperra(self,mensajep):
        print(f"Chat perra: {mensajep}")
    def datos(self):
        print(f"Color: {self.color}, edad: {self.edad}")
#llamadas a funciones
chihuas=Perro("Negro",2)
#llamada a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperra("Hola canina")
chihuas.chatperro("Hola boby")
chihuas.chatperro("Quieres ser mi guaoguao??")
chihuas.chatperra("grru......")