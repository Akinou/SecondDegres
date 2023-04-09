import math

a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))

delta = b**2 - 4*a*c

if delta < 0:
    print("L'équation n'a pas de solution réelle.")
elif delta == 0:
    x = -b / (2*a)
    print("La solution de l'équation est x =", x)
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("Les solutions de l'équation sont x1 =", x1, "et x2 =", x2)
