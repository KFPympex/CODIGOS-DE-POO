"""
   Nombre: Kevin Francisco Lira Barrera
   Matricula: 1723110397
   Grupo:TI21
   Fecha: 18/01/2023
   Descripcion: Programa que define a un objeto "Alumnos"
"""
class Alumnos:#define una clase de nombre Alumnos
    matricula:None#define una variable de nombre matricula
    nombre:None#define una variable de nombre nombre
    def __init__ (self, matricula, nombre):#define el constructor de la clase A y define los valores de matricula y nombre
        self.matricula = matricula#asigna a la variable matricula el valor de matricula
        self.nombre = nombre#asigna a la variable nombre el valor de nombre
        print("Objeto Alumnos")#imprime el texto objeto Alumnos
objetoAlumnos=Alumnos (111, "Dejah")#crea un objeto de la clase Alumnos y le asigna los valores de 111 y Dejah
objetoAlumno2=Alumnos(nombre="Jhon", matricula=222)#crea un objeto de la clase Alumnos y le asigna los valores de 222 y Jhon
