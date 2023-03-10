contagem = 0
soma = 0

for numero in range (1, 7):
    valor = int(input("Digite o valor: "))
    
    if(valor%2==0):
        contagem += 1
        
        soma += valor
        
print("Voce informou ", contagem, " numeros pares e a soma foi ", soma)