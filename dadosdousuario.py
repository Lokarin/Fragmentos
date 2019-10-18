# -*- coding: utf-8 -*-

name = input("Insira seu nome: ")
name2 = input("Insira seu sobrenome completo: ")
idade = int(input("Insira sua idade: "))
print("\n")

print("Usuário: %s"%name, name2)
print("Idade: %i"%idade)
print("\n")

if idade >= 18:
  print ("Maior de Idade")
elif idade > 0 and idade < 18:
  print ("Menor de Idade")
else:
  print ("Valor Inválido")
