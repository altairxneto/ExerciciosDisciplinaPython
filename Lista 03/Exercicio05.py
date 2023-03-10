primeiro_termo = int(input("Digite o primeiro termo: "))

razao = int(input("Digite a razao da PA: "))

soma = primeiro_termo

for numero in range(0, 10):
    print(soma)
    
    soma += razao
    
print("Acabou")