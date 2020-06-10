#-*- coding: utf-8 -*-

print("Em funcionamento...")
print("São quantos valores? [De 2 a 5]")
n_valores = int(input("Resposta: "))

if n_valores == 2:
    print("Trabalhando com 2 valores.\n")

    val1 = float(input("Valor 1:\n"))
    val2 = float(input("Valor 2: \n"))

    media = (val1 + val2) / 2

    print("Média: %f \n"%media)

elif n_valores == 3:
    print("Trabalhando com 3 valores.\n")
    
    val1 = float(input("Valor 1:\n"))
    val2 = float(input("Valor 2: \n"))
    val3 = float(input("Valor 3: \n"))
    
    media = (val1 + val2 + val3) / 3
    
    print("Média: %f \n"%media)

elif n_valores == 4:
    print("Trabalhando com 4 valores.\n")

    val1 = float(input("Valor 1: \n"))
    val2 = float(input("Valor 2: \n"))
    val3 = float(input("Valor 3: \n"))
    val4 = float(input("Valor 4: \n"))
    
    media = (val1 + val2 + val3 + val4) / 4

    print("Média: %f \n"%media)

elif n_valores == 5:
    print("Trabalhando com 5 valores.\n")

    val1 = float(input("Valor 1: \n"))
    val2 = float(input("Valor 2: \n"))
    val3 = float(input("Valor 3: \n"))
    val4 = float(input("Valor 4: \n")) 
    val5 = float(input("Valor 5: \n"))
    
    media = (val1 + val2 + val3 + val4 + val5) / 5

    print("Média: %f \n"%media)

elif n_valores == 10:
    print("Trabalhando com 10 valores.\n")

    val1 = float(input("Valor 1: \n"))
    val2 = float(input("Valor 2: \n"))
    val3 = float(input("Valor 3: \n"))
    val4 = float(input("Valor 4: \n")) 
    val5 = float(input("Valor 5: \n"))
    val6 = float(input("Valor 6: \n"))
    val7 = float(input("Valor 7: \n"))
    val8 = float(input("Valor 8: \n"))
    val9 = float(input("Valor 9: \n"))
    val10 = float(input("Valor 10: \n"))
   
    media = (val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9 + val10) / 10

    print("Média: %f \n"%media)

