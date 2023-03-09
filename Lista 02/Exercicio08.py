salario = float(input("Digite o valor do seu salário: "))

if(salario > 1250):
    print("O aumento no seu salário será de: R$", salario*10/100)
    
elif(salario <= 1250):
    print("O aumento no seu salário será de: R$", salario*15/100)