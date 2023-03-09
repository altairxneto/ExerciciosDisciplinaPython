from random import randint

numero_aleatorio = randint(0, 5)

numero_digitado = int(input("Digite um numero entre 0 e 5: "))

if(numero_aleatorio == numero_digitado):
    print("Você advinhou o número!")
else:
    print("Você não advinhou, tente na próxima vez!")