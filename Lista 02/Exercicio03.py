velocidade = float(input("Digite a velocidade do carro em km/h: "))

if(velocidade > 80):
    print("Você foi multado, a multa é de: R$", (velocidade-80)*7)