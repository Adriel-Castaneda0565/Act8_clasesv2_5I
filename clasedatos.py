class Informacion:
    def mi_lista(self):
        lista_Nomperro=["boby","dollar","fany"]
        for a in lista_Nomperro:
            print(a)

    def mi_tupla(self):
        tupla_razas=("Doberman","Labrador","Pastor Aleman")
        for b in tupla_razas:
            print(b)

    def mi_conjunto(self):
        conjunto_colores={"morado","azul","negro","amarillo"}
        for c in conjunto_colores:
            print(c)

    def mi_dic(self):
        dic_edadP={"boby":"4","Dollar":"10","fany":"2"}
        for d,e in dic_edadP.items():
            print(d,e)


#creando el objeto

datos=Informacion()
print("Listado de nombres de perros")
datos.mi_lista()
print("\nTupla razas de perros")
datos.mi_tupla()
print("\nConjunto de colores")
datos.mi_conjunto()
print("\nDiccionario edades")
datos.mi_dic()