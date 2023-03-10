valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))

x = 0

while x < 1:
    print("[1] SOMAR")
    print("[2] SUBTRAIR")
    print("[3] MULTIPLICAR")
    print("[4] DIVIDIR")
    print("[5] SAIR DO PROGRAMA")
    
    resposta = int(input("Digita a opção que deseja: "))
    
    if(resposta == 1):
        print("A soma é ", valor1+valor2)
        
    elif(resposta == 2):
        print("A subtração do valor 1 menos o valor 2 é ", valor1-valor2)
        
    elif(resposta == 3):
        print("A multiplicação é ", valor1*valor2)
        
    elif(resposta == 4):
        print("A divisão do valor 1 pelo 2 é ", valor1/valor2)
        
    elif(resposta == 5):
        print("Até mais!")
        
        x += 1