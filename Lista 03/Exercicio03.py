soma = 0
contagem = 0

for numero in range(0, 501, 3):
    if(numero%2!=0):
        soma += numero
        
        contagem += 1
    
print("A soma de todos os ", contagem, " valores é ", soma)