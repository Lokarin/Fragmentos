# -*- coding: utf-8 -*-

print("Em funcionamento...\n")
print("Por favor, digite as 3 notas de suas médias.")

nota1 = float(input("Nota do primeiro trimestre: "))
nota2 = float(input("Nota do segundo trimestre: "))
nota3 = float(input("Nota do terceiro trimestre: "))

print("\n")

mediaFinal = (nota1 + nota2 + nota3) / 3
print("Sua nota de média final é de: %f"%mediaFinal)

if mediaFinal < 7:
   provaFinal = 10 - mediaFinal
   print("Você precisa de %f pontos para passar de ano"%provaFinal)