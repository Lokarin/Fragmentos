# -*- coding: utf-8 -*-
import math

print("Em Funcionamento...")

val1 = float(input("Primeiro Valor: "))
operador = input("Operador(+, -, *, /, **, resto, raiz):")

if operador == "+":
    val2 = float(input("Segundo Valor: "))
    print("\n")
    soma = val1 + val2
    print("Resulatado da Soma: %f"%soma)
elif operador == "-":
    val2 = float(input("Segundo Valor: "))
    print("\n")
    subtracao = val1 - val2
    print("Resulatado da Subtração: %f"%subtracao)
elif operador == "*":
    val2 = float(input("Segundo Valor: "))
    print("\n")
    multiplicacao = val1 * val2
    print("Resulatado da Multiplicação: %f"%multiplicacao)
elif operador == "**":
    val2 = float(input("Segundo Valor: "))
    print("\n")
    elevado = val1 ** val2
    print("Resulatado da Exponenciação: %f"%elevado)
elif operador == "/":
    val2 = float(input("Segundo Valor: "))
    print("\n")
    divisao = val1 / val2
    print("Resulatado da Divisão: %f"%divisao)
elif operador == "resto":
    val2 = float(input("Segundo Valor: "))
    print("\n")
    resto = val1 % val2
    print("O resto é de: %f"%resto)
elif operador == "raiz":
    print("\n")
    raizFinal = math.sqrt(val1)
    print("Raiz desse número é: %f"%raizFinal)
else:
    print("Operação Inválida")
    
