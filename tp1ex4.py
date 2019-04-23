import math

print ("Veuillez entrer les 3 valeurs de votre trinome")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b*b- 4*a*c

x1 = (-b - math.sqrt(delta))/2*a
x2 = (-b + math.sqrt(delta))/2*a

print ("Les racines sont: x1 = ", x1," et x2 = ", x2)