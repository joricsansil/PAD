import os

def gravar_nome_arquivo(nome):
    # Define o nome do arquivo
    arquivo_nome = 'nome.txt'

    # Verifica se o arquivo já existe
    if os.path.exists(arquivo_nome):
        # Lê o conteúdo do arquivo
        with open(arquivo_nome, 'r') as arquivo:
            nomes_existentes = arquivo.read().strip().split('\n')

        # Adiciona o novo nome à lista de nomes
        nomes_existentes.append(nome)

        # Escreve os nomes de volta no arquivo
        with open(arquivo_nome, 'w') as arquivo:
            for nome in nomes_existentes:
                arquivo.write(f"{nome}\n")
    else:
        # Cria o arquivo e grava o nome
        with open(arquivo_nome, 'w') as arquivo:
            arquivo.write(f"{nome}\n")

    # Imprime uma mensagem de confirmação
    print(f"Seu nome foi gravado no arquivo 'nome.txt'.")

# Solicitando ao usuário para digitar seu nome
nome = input("Digite seu nome: ").strip()
gravar_nome_arquivo(nome)

