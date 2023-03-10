import random

numero = random.randint(0, 10)

contagem = 0

x = 0

print("Pensei em um número de 0 a 10, me fale qual número eu pensei!")

while x < 1:
    resposta = int(input("Qual o seu palpite? "))
    
    if(resposta < numero):
        print("Mais... Tente mais uma vez")
        contagem += 1
        
    elif(resposta > numero):
        print("Menos... Tente mais uma vez")
        
        contagem += 1
        
    elif(resposta == numero):
        print("Acertoooou, com ", contagem, " tentativas!")
    