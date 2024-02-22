a = 10
b = 9
c = 8

if a > b:
     print (a)

if a > c:
     print (a)

if b > c:
     print (b)


print("\n" * 2)#


if a > b:
     print (a)

elif a > c:
     print (a)

if b > c:
     print (b)


print("\n" * 2)#







A = 10
B = 9
C = 18


if A > B: #si es verdadero se ejecuta el otro if
     if A > C:
         print (A)

else:
     print (C)


print("\n" * 2)#


if A > B and A > C:
         print (A)

else:
     print (C)


print("\n" * 2)#


if A > B or A > C:
         print (A)

else:
     print (C)


print("\n" * 2)#


if A > B: 
    if A > C:
        print (A)
    if B > C:
        print (C)
else:
        print (B)


print("\n" * 2)#
