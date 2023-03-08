nome = input("Digite seu nome:")

print("Nome com todas as letras minusculas: ", nome.lower())

print("Nome com todas as letras maiúsculas: ", nome.upper())

novo_nome = nome.strip();

print("Quantas letras tem no nome: ", len(novo_nome))

primeiro_nome = nome.split(" ")

print("Quantas letras tem o primeiro nome: ", len(primeiro_nome))