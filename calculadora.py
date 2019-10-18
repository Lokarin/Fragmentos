# -*- coding: utf-8 -*-

val1 = float(input("Primeiro Valor: "))
operador = input("Operador(+, -, *, /, **):" )
val2 = float(input("Segundo Valor: "))
print("\n")

if operador == "+":
    soma = val1 + val2
    print("Resulatado da Soma: %f"%soma)
elif operador == "-":
    subtracao = val1 - val2
    print("Resulatado da Subtração: %f"%subtracao)
elif operador == "*":
    multiplicacao = val1 * val2
    print("Resulatado da Multiplicação: %f"%multiplicacao)
elif operador == "**":
    elevado = val1 ** val2
    print("Resulatado da Exponenciação: %f"%elevado)
elif operador == "/":
    divisao = val1 / val2
    print("Resulatado da Divisão: %f"%divisao)
else:
    print("Operação Inválida")
    
