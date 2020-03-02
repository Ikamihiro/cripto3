def Menu():
    print('''
Bem Vindo!
Escolha sua opção:
1 - Realizar HASH
2 - Sair
    ''')

def Hash():
    path = str(input('\nDigite o PATH do arquivo: '))
    print(path)

while True:
    Menu() # Exibindo o Menu

    opcao = int(input('Digite sua opção: ')) # Escolhendo a opção

    if(opcao == 2):
        print('\nIsso é um adeus amigo... Mas volte sempre!!\n')
        break

    Hash() # Função Principal