cadena = "dejah@gmail.com"

for i in cadena:
    print(i)

print("\n" * 2)

#Sopas 2
for i in range (0, len(cadena), 2):#En Python, la función len() es una función incorporada que se utiliza para obtener la longitud o el tamaño de un objeto iterable, como una cadena de texto, una lista, una tupla o un diccionario. Devuelve el número de elementos o caracteres que contiene el objeto
    print (cadena[i])

print ("\n" * 2)

for i in range (1, len(cadena), 2):
    print (cadena[i])

print ("\n" * 3)








#Axel
for i in range (0, 14, 2):
    print (cadena[i])

print ("\n" * 2)

for i in range (1, 14, 2):
    print (cadena[i])

print ("\n" * 2)







#Chayote
for i in range (len(cadena)):
    if i % 2 != 0:
        print(cadena [i])


print ("\n" * 2)




for i in range (1):
    print (cadena[0:14:2])
