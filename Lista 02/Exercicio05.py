kilometragem = float(input("Digite a distância da viagem em km: "))

if(kilometragem <= 200):
    print("O valor da passagem é: R$", kilometragem*0.5)
    
else:
    print("O valor da passagem é: R$", kilometragem*0.45)