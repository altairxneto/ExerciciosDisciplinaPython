N1 = int(input("Digite o número: "))

contagem = 0

for numero in range(1, (N1+1)):
    if(N1%numero == 0):
        contagem += 1
        
        print("\033[1;34m", numero, "\033[0;0m")
        
    else:
        print("\033[1;31m", numero, "\033[0;0m")
        
if(contagem==2):
    print("É PRIMO")
    
else:
    print("NÃO É PRIMO")