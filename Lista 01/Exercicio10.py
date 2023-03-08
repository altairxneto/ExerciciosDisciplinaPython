numero = int(input("Digite um numero de 0 até 9999: "))

if(0<= numero <= 9999):
    novo_numero = str(numero)
    quantidade_cactere = len(novo_numero)
    
    if(quantidade_cactere == 4):
        print("Unidade: ", novo_numero[0])
        print("Dezena: ", novo_numero[1])
        print("Centena: ", novo_numero[2])
        print("Milhar: ", novo_numero[3])
    
    elif(quantidade_cactere == 3):
        print("Unidade: ", novo_numero[0])
        print("Dezena: ", novo_numero[1])
        print("Centena: ", novo_numero[2])
    
    elif(quantidade_cactere == 2):
        print("Unidade: ", novo_numero[0])
        print("Dezena: ", novo_numero[1])
        
    elif(quantidade_cactere == 1):
        print("Unidade: ", novo_numero[0])
        
else:
    print("Numero não valido!")
    

