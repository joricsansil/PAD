import random

def lançar_dado():
    return random.randint(1, 6)

resultado = lançar_dado()
print(f"O lado que saiu foi: {resultado}")