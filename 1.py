import math
import zlib


print("-------------------------------")
print("---- Hallar la raiz-------")
print("-------------------------------")


# input 

x=int(input("Digite el valor del radiacando"))
n=int(input("Digite el valor del indice"))

# processing 

z= pow(x,1/n)


# ouput

print("la raiz de " + str (x) + " con indice " + str(n) + " es igual a "  + str(z))