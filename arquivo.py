import os

def copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino):
    # Verifica se o arquivo de origem existe
    if os.path.exists(nome_arquivo_origem):
        # Abre o arquivo de origem para leitura
        with open(nome_arquivo_origem, 'r') as arquivo_origem:
            conteudo = arquivo_origem.read()

        # Verifica se o arquivo de destino existe ou não
        if not os.path.exists(nome_arquivo_destino):
            # Cria um novo arquivo de destino
            with open(nome_arquivo_destino, 'w') as arquivo_destino:
                arquivo_destino.write(conteudo)
        else:
            # Abre o arquivo de destino para leitura
            with open(nome_arquivo_destino, 'r') as arquivo_destino:
                # Lê o conteudo do arquivo de destino
                conteudo_destino = arquivo_destino.read()

            # Abre o arquivo de destino para escrita
            with open(nome_arquivo_destino, 'w') as arquivo_destino:
                # Escreve o conteúdo do arquivo de origem antes do conteúdo do arquivo de destino
                arquivo_destino.write(conteudo)
                # Escreve o conteúdo do arquivo de destino após o conteúdo do arquivo de origem
                arquivo_destino.write(conteudo_destino)
    else:
        # Mensagem de erro: arquivo de origem não existe
        print(f"O arquivo '{nome_arquivo_origem}' não existe.")

# Solicitando ao usuário para digitar o nome do arquivo de origem e destino
nome_arquivo_origem = input("Digite o nome do arquivo de texto para copiar: ").strip()
nome_arquivo_destino = input("Digite o nome do arquivo onde deseja copiar: ").strip()
copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino)