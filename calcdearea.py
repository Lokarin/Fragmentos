# -*- coding: utf-8 -*-

print("1 - Quadrado \n2 - Retângulo\n3 - Triângulo")
forma = input("N° da forma desejada: ")

if forma == "1":
    lados = float(input("Tamanho dos lados: \n"))
    area = lados * lados
    print("A área desse Quadrado é: %f"%area)
elif forma == "2":
    lados = float(input("Largura do retângulo: "))
    lados2 = float(input("Altura do retângulo: \n"))
    area = lados * lados2
    print("A área desse Retângulo é: %f"%area)
elif forma == "3":
    lados = float(input("Base do Triângulo: "))
    lados2 = float(input("Altura do Triângulo: "))
    area = (lados * lados2) / 2
    print("A área desse Triângulo é: %f"%area)
else:
    print("Operação encerrada, por favor insira um valor válido")
