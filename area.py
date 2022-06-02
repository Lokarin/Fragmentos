# -*- coding: utf-8 -*-

def quadrado (lado):
    return lado*lado 

def triangulo (base, altura):
    return base*altura/2 

def retangulo (base, altura):
    return base*altura

def circulo (raio):
    return (raio*raio)*3.14

print("1 - Quadrado \n2 - Retângulo\n3 - Triângulo \n4 - Círculo")
forma = input("Calcular área de um: "); print("\n")

if (forma == "1"):
    l = float(input("Lados do quadrado: "))
    print("A área deste quadrado é: ", quadrado(l))
elif (forma == "2"):
    b = float(input("Base deste retangulo: "))
    h = float(input("Altura desde retangulo: "))
    print("A área deste retangulo é: ", retangulo(b,h))
elif (forma == "3"):
    b = float(input("Base deste triangulo: "))
    h = float(input("Altura desde triangulo: "))
    print("A área deste triangulo é: ", triangulo(b,h))
elif (forma == "4"):
    r = float(input("Raio deste circulo: "))
    print("A área deste circulo é: ", circulo(r))
