from hash_function import Hash, Menu

while True:
    Menu() # Exibindo o Menu

    opcao = str(input('Digite sua opção: ')) # Escolhendo a opção

    # Se o Usuário desejar sair
    if(opcao == '2'):
        print('\nIsso é um adeus amigo... Mas volte sempre!!\n')
        break
    if(opcao == '1'):
        path = str(input('\nDigite o PATH do arquivo: '))
        try:
            arquivo = open(path, 'r') # abrindo o arquivo
            dados = arquivo.read() # lendo os dados dentro do arquivo
            dados = Hash(dados) # Chamando a função principal
            saida = open('hash.txt','w')
            saida.write(dados) # escrevendo o resultado no arquivo de saída
            print('\nO resultado do HASH está disponível no arquivo "hash.txt"!')
            print('\nSe divirta :)\n')
        except FileNotFoundError:
            # Exceção caso o arquivo não seja encontrado
            # Ou ocorra algum erro em sua abertura
            print('\nNão foi possível abrir o arquivo!\n')
        finally:
            arquivo.close
            saida.close
    else:
        print('\nOpção errada amigo!\nTente novamente...\n')