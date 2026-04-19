("="*30)

print("Bem-vindo! Cadastre os três novos funcionários:")
print("-"*30)

nome1 = input("Informe o nome do primeiro funcionário: ")
cad1 = int(input(f"Digite o cadastro numérico de {nome1}: "))

nome2 = input("Informe o nome do segundo funcionário: ")
cad2 = int(input(f"Digite o cadastro numérico de {nome2}: "))

nome3 = input("Informe o nome do terceiro funcionário: ")
cad3 = int(input(f"Digite o cadastro numérico de {nome3}: "))

print("Você cadastrou todos os funcionários")
print("="*30)
print("Bem-vindo! Informe seus dados para continuar: ")
print("-"*30)

nome = (input("Informe seu nome: "))

if nome == nome1:
    print(f"Olá, {nome}!")
    cadastro = int(input("Digite seu cadastro: "))
    if cadastro == cad1:
        print("Acesso PERMITIDO!")
    else:
        print("Acesso NEGADO")
elif nome == nome2:
    print(f"Olá, {nome2}!")
    cadastro = int(input("Digite seu cadastro: "))
    if cadastro == cad2:
        print("Acesso PERMITIDO!")
    else:
        print("Acesso NEGADO")
elif nome == nome3:
    print(f"Olá, {nome3}!")
    cadastro = int(input("Digite seu cadastro: "))
    if cadastro == cad3:
        print("Acesso PERMITIDO!")
    else:
        print("Acesso NEGADO")
else:
    print("Cadastro não encontrado")

print("="*30)






