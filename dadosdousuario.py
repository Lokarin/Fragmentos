# -*- coding: utf-8 -*-

name = input("Insira seu nome: ")
name2 = input("Insira seu sobrenome completo: ")
idade = float(input("Insira sua idade: \n"))

print("Usuário: %s"%name, name2)
print("Idade: %i"%idade)

if idade < 18:
   print("Menor de Idade, Permissão Negada")
else:
   print("Permissão Concedida")
