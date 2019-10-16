# -*- coding: utf-8 -*-

val1 = float(input("Digite aqui sua primeira nota: \n"))
val2 = float(input("Digite aqui sua segunda nota(peso 2): \n"))
val2peso = val2 * 2

media = (val1 + val2peso) / 3
print("Sua média é de: %f"%media)

if media >= 6 and media < 10:
	print("Passou")
elif media < 6:
	print("Reprovou")
else:
	print("Valor Inválido")