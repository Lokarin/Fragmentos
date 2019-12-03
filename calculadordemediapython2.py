# -*- coding: utf-8 -*-

print("Em Funcionamento...")
print("(Notas com Peso 2)")
val1 = float(input("Digite aqui sua primeira nota: \n"))
val2 = float(input("Digite aqui sua segunda nota: \n"))
val2peso = val2 * 2
val1peso = val1 * 2

media = (val1peso + val2peso) / 4
print("Sua média é de: %f \n"%media)

if media >= 7 and media < 10:
	print("Passou")
elif media < 6:
	print("Reprovou")
else:
	print("Valores Inválidos")
