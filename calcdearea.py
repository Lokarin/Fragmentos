# -*- coding: utf-8 -*-

print("Em Funcionamento...\n")
print("1 - Quadrado \n2 - Retângulo\n3 - Triângulo \n4 - Círculo")
forma = input("N° da forma desejada: ")


if forma == "1":
    lados = float(input("Tamanho dos lados: \n"))
    area = lados * lados
    print("\nA área desse Quadrado é: %f"%area)
    
elif forma == "2":
    lados = float(input("Largura do retângulo: "))
    lados2 = float(input("Altura do retângulo: \n"))
    area = lados * lados2
    print("\nA área desse Retângulo é: %f"%area)
    
elif forma == "3":
    lados = float(input("Base do Triângulo: "))
    lados2 = float(input("Altura do Triângulo: "))
    area = (lados * lados2) / 2
    print("\nA área desse Triângulo é: %f"%area)
    
elif forma == "4":
    pi = 3.14
    raio = float(input("Qual é o tamanho do raio?: "))
    area = (raio*raio) * pi
    print("\nA área desse Círculo é de : %f"%area)
    
else:
    print("Operação encerrada, por favor insira um valor válido")
