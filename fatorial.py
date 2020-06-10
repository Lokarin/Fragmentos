#-*- coding: utf-8 -*-

n = int(input("Número para o fatorial: "))
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
      
print ("O fatorial é igual a: ",end="") 
print (fact) 
