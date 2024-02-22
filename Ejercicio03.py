"""
   Nombre: Kevin Francisco Lira Barrera
   Matricula: 1723110397
   Grupo:TI21
   Fecha: 18/01/2023
   Descripcion: Programa que define a un objeto, pero no llama a nada ya que no esta asignado las variables
"""
class Alumnos:#define una clase de nombre Alumnos
    matricula:None#define una variable de nombre matricula
    nombre:None#define una variable de nombre nombre
    def __init__(self, matricula, nombre):#define el constructor de la clase A y define los valores de matricula y nombre
        self.matricula = matricula#asigna a la variable matricula el valor de matricula
        self.nombre = nombre#asigna a la variable nombre el valor de nombre
        print("Objeto Alumnos")#imprime el texto objeto Alumnos
objetoAlumnos = Alumnos()#crea un objeto de la clase Alumnos
