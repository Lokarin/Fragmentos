# -*- coding: utf-8 -*-
import math

valx = float(input("Valor de x ao quadrado: "))
valx2 = float(input("Valor de x: "))
val = float(input("Valor de c: "))

delta = (valx2 ** 2) - (4*valx*val)
#print(delta)


if delta < 0:
    print("A equação não possuí solução")
elif delta == 0:
    x1 = (-valx2+math.sqrt(delta))/2*valx
    print("Valor de Delta: %f"%delta)
    print("Resolução: %f"%x1)
else:
    x1 = (-valx2+math.sqrt(delta))/2*valx
    x2 = (-valx2-math.sqrt(delta))/2*valx
    print("Valor de Delta: %f"%delta)
    print("Resolução 1: %f"%x1)
    print("Resolução 2: %f"%x2)
