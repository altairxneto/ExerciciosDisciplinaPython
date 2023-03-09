import math

numero1 = float(input("Digite o numero 1: "))
numero2 = float(input("Digite o numero 2: "))
numero3 = float(input("Digite o numero 3: "))

maior = 0;
menor = 0;

if(numero1 < numero2 < numero3):
    maior = numero3
    menor = numero1
    
elif(numero1 < numero3 < numero2):
    maior = numero2
    menor = numero1

elif(numero2 < numero1 < numero3):
    maior = numero3
    menor = numero2

elif(numero2 < numero3 < numero1):
    maior = numero1
    menor = numero2

elif(numero3 < numero1 < numero2):
    maior = numero2
    menor = numero3

elif(numero3 < numero2 < numero1):
    maior = numero1
    menor = numero3
    
print("O maior numero é: ", maior)

print("O menor número é: ", menor)