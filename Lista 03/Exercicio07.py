variavel = 0

while variavel < 1:
    sexo = str(input("informe seu sexo [M/F]: "))
    
    if(sexo == "M" or sexo == "F"):
        print("Sexo ", sexo, "registrado com sucesso")
        
        variavel += 1
        
    else:
        print("Dados invalidos.")