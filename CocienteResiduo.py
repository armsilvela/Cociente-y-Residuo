'''
Escriba un programa que pida al usiario dos datos númericos enteros y muestre
por pantalla "<n> entre <m> da un cociente <c> y un resto <r>", donde <n> y <m>
son los números introducidos por el usuario, y <c> y <r> son el cociente y el
resto respectivamente.
'''
n = int(input("Ingrese un numero entero: "))
m = int(input("Ingrese un numero entero: "))
c = n / m
r = n % m

print(str(n) + " entre " + str(m) + " da un cociente de " + str(c) + " y un resto de " +
str(r))
print(f"{n} entre {m} da un cociente de {c} y un resto de {r}")
