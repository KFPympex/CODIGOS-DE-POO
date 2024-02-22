"""
   Nombre: Kevin Francisco Lira Barrera
   Matricula: 1723110397
   Grupo:TI21
   Fecha: 18/01/2023
   Descripcion: Programa que define un objeto con el metodo init
"""
class A:#define una clase de nombre A
    matricula=None#declara la variable matricula
    nombre=None#declara la variable nombre
    def __init__(self, matricula, nombre):#define el constructor de la clase A y define los valores de matricula y nombre
        print("Constuctor de la clase A") #imprime el mensaje
        self.matricula=matricula#asigna a la variable matricula el valor de matricula
        self.nombre=nombre#asigna a la variable nombre el valor de nombre
objetoA=A(1111, "Dejah")#crea un objeto de la clase A
print(objetoA.nombre)#imprime el nombre del objeto
