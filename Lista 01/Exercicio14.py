nome = input("Digite seu nome: ")

nome_splitado = nome.split(" ")

print("Primeiro nome: ", nome_splitado[0], ", último nome: ", nome_splitado[len(nome_splitado)-1])