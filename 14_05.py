def procurar_nome_arquivo(nomes, numero):
    # Abre o arquivo para leitura
    with open(nomes.txt, 'r') as arquivo:
        # Lê o conteúdo do arquivo linha por linha
        for linha in arquivo:
            # Remove espaços em branco no início e no final da linha
            nome = linha.strip()
            # Verifica se o nome corresponde ao número procurado
            if int(numero) in nome:
                # Imprime o nome encontrado
                print(nome)

# Solicitando ao usuário para digitar o número que deseja procurar
numero = input("Digite o número que deseja procurar no arquivo: ").strip()
procurar_nome_arquivo('nomes.txt', numero)

