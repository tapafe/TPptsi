n = int(input("Rentrer un nombre entre 0 et 15 compris: "))

i = n

x1 = x2 = x3 = x4 = 0

print(i, n)

while i != 0:
    if i >= 8:
        x1 = 1
        i = i - 8
    elif i >= 4:
        x2 = 1
        i = i - 4
    elif i >= 2:
        x3 = 1
        i = i - 2
    elif i >= 1:
        x4 = 1
        i = i - 1

y1 = x4
y2 = x3
y3 = x2
y4 = x1

n2 = y1*8 + y2*4 + y3*2 + y4*1

print("Votre nombre", n, "vaut en base 2: ", x1, x2, x3, x4, ". Le mirroir binaire vaut: ", y1, y2, y3, y4,
      "ce qui correspond à: ", n2, "en décimal")
