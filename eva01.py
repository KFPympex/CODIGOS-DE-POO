"""
Programa: eva01.py
Alumno:Kevin Francisco Lira Barrera
Matricula:1723110397
Fecha:29/01/2024
"""

class Profesores:
    id = None
    nombre = ""
    materia = []

    def __init__(self,id,nombre,materia):
        self.id = id
        self.nombre = nombre
        self.materia = [materia]
        print("Constructor objeto" + "Profesor")

    def califica(self):
        print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre,self.materia[0]))

    def pasaAsistencia(self):
        print(f"El profesor {self.nombre} pasa asistencia")

profesor1 = Profesores("111", "Profesor 1", "Materia 1")
profesor1.materia.append("Materia 2")
profesor1.califica()
profesor1.pasaAsistencia()
