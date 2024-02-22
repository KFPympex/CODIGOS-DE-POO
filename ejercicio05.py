"""
   Nombre: Kevin Francisco Lira Barrera
   Matricula: 1723110397
   Grupo:TI21
   Fecha: 18/01/2023
   Descripcion: Programa que crea un objeto
"""
#Metodos
class Alumno:#define una clase 
    matricula: None#declara la variable matricula
    nombre:None#declara la variable nombre
    def __init__(self, matricula, nombre):#define al metodo init
        self.matricula = matricula#asigna a la variable matricula el valor de la variable matricula
        self.nombre = nombre#asigna a la variable nombre el valor de la variable nombre
        print("Objeto Alumno")#imprime el texto Objeto alumno
    def estudiar(self):#define el metodo estudiar
        print(f"{self.nombre} estudia")#imprime el texto {self.nombre} estudia
    def sumar(self, numero1, numero2):#define el metodo sumar
        suma=numero1 + numero2#asigna a la variable suma el valor de la variable numero1 + numero2, es la operacion
        print(f"La suma de {numero1} + {numero2} = {suma}")#imprime el texto La suma de {numero1} + {numero2} = {suma}
dejah=Alumno(1111, "Dejah")#crea un objeto de la clase Alumno      
dejah.estudiar()#ejecuta el metodo estudiar
dejah.sumar(10,14)#ejecuta el metodo sumar
