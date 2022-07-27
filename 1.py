from cmath import pi
import math



# input

radio=int(input("Digite el valor del radio : "))

# processing

area= math.pi*radio*radio
perimetro= 2*math.pi*radio

# output

print(" El area con radio de " + str(radio) + " es igual a: " + str(area) + " y el perimetro es igual a: "  + str(perimetro))