# -*- coding: utf-8 -*-
  
print("Notas com peso?\n 1 - Yes\n 2 - No")
peso = int(input("Resposta: "))


if peso == 1:
  print("Ok, calculando notas com Peso 2")
  
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
    
  
elif peso == 2:
  print("Ok, calculando notas sem Peso")
  
  val1 = float(input("Digite aqui sua primeira nota: \n"))
  val2 = float(input("Digite aqui sua segunda nota: \n"))
  
  media = (val1 + val2) / 2
  print("Sua média é de: %f \n"%media)
  
  if media >= 7 and media < 10:
    print("Passou")
    
  elif media < 6:
    print("Reprovou")
    
  else:
    print("Valores Inválidos")
  
  
else:
  print("Valor Inválido")
  
 
