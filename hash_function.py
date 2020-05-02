# Função que exibe um MENU
def Menu():
    print(
'''
Bem Vindo!
Escolha sua opção:
1 - Realizar HASH
2 - Sair
''')

# Função que realiza um XOR entre dois blocos de bits
def XOR(direita, esquerda):
    return ''.join('0' if esquerda[i] == direita[i] else '1' for i in range(len(direita))) 

# Função para tirar os espaços e quebras de linha
def Formatar(dados):
    return ''.join(dados.split())

# Função que pega um conjunto e separa em blocos de tamanho N
def Agrupar(dados, tam_bloco):
    return [dados[i:i + tam_bloco] for i in range(0, len(dados), tam_bloco)]

# Função que completa e separa em blocos com tamanho N
def Completar(dados, tam_bloco):
    tam_dados = len(dados)

    # calcula o resto do bloco que não será preenchido pelos dados
    tam_resto = tam_dados % tam_bloco
    
    # preenche esses espaços com 1
    dados = dados + ''.join(['1' for i in range(tam_bloco - tam_resto)])
    
    # separa esses dados em blocos
    return Agrupar(dados, tam_bloco)

# Função que converte string para binário
def ToBin(dados):
    return bin(int.from_bytes(dados.encode(), 'big')).replace('b', '')

# Função que pega N bits do começo e joga para esquerda
def RotacionarEsquerda(bloco, n, tam_bloco):
    rotacao = ''
    num_bits = ''
    for i in range(0, n):
        if(n > 64):
            i = 0
        num_bits = num_bits + str(bloco[i])
    for j in range(n, tam_bloco, 1):
        rotacao = rotacao + str(bloco[j])
    rotacao = rotacao + str(num_bits)
    return rotacao

# Função que concatena os resultados das rotações e gera novos blocos
def Rotacionar(dados, tam_bloco):
    bloco = ''
    resultado = ''
    n = 1
    for dado in dados:
        bloco = RotacionarEsquerda(dado, n, tam_bloco)
        resultado = resultado + str(bloco)
        n += 1
    return Agrupar(resultado, tam_bloco)

# Função Principal que faz o hash
def Hash(dados):
    # tirando os espaços e quebras de linha
    dados = Formatar(dados) 
    
    print('\nEstes são os dados que foram importados do arquivo:\n' + dados + '\n')
    
    # convertendo os dados p/ binário
    dados = ToBin(dados)
    
    # Verificação de tamanho
    if(len(dados) <= 64):
        print('Okay meu consagrado...\nTua entrada não pode ser menor que 9 caracteres...')
        exit()

    print('Os dados convertidos para base binária:\n' + dados)

    # Completando e quebrando em os blocos de 64 bits
    dados = Completar(dados, 64)

    # Fazendo as rotações
    dados = Rotacionar(dados, 64)

    # Variável que receberá o resultado da HASH
    # Primeiramente, ela receberá o primeiro bloco
    resultado = ''

    # Realizando XOR entre os blocos gerados
    for i in range(len(dados)):
        if(resultado == ''):
            resultado = XOR(dados[i], dados[i + 1])
        else:
            resultado = XOR(resultado, dados[i])
    
    # Mostrando o resultado final
    print('\nResultado final:\n' + resultado)

    return resultado
