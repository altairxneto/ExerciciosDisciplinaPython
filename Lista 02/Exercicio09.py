lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))

if(lado1 < lado2 + lado3):
    print("É um triangulo")
    
elif(lado2 < lado1 + lado3):
    print("É um triangulo")
    
elif(lado3 < lado1 + lado2):
    print("É um triangulo")
    
else:
    print("não é um triangulo")