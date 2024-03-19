# Definindo as variáveis
numeros = [12, 3, 22, 16]
frase = "socorro subi num onibus em marrocos."
palavra = "ineficaz"

# Calculando a média aritmética
media = sum(numeros) / len(numeros)
print("Média aritmética dos números:", media)

# Calculando o quadrado de um dos números
num_quadrado = numeros[0]
quadrado = num_quadrado ** 2 #Ele vezes ele mesmo
print("Quadrado de", num_quadrado, ":", quadrado)

# Calculando o dobro de um dos números
num_dobro = numeros[1]
dobro = num_dobro * 2
print("Dobro de", num_dobro, ":", dobro)

# Contando a quantidade de letras da palavra
qtd_letras_palavra = len(palavra)
print("Quantidade de letras da palavra:", qtd_letras_palavra)

# Contando a quantidade de espaços em branco na frase
qtd_espacos_branco = frase.count(" ")
print("Quantidade de espaços em branco na frase:", qtd_espacos_branco)

# Verificando se o primeiro número é maior que o segundo
primeiro_maior_segundo = numeros[0] > numeros[1]
print("O primeiro número é maior que o segundo?", primeiro_maior_segundo)

# Encontrando o maior número
maior_numero = max(numeros)
print("O maior número é:", maior_numero)