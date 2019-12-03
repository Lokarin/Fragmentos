# -*- coding: utf-8 -*-

print("Em Funcionamento...")

def transformacaoBinaria(num):
    if num > 1:
        transformacaoBinaria(num // 2)
    print(num % 2, end = '')

print("Qual será o número convertido em binário?")
numero = int(input("Número: "))
#print(numero)
print("\nO Número %i em binário é: "%numero)

transformacaoBinaria(numero)

