def bombom(dinheiro,preco):
    return float(dinheiro)//preco, dinheiro%preco

def maisbombom(dinheiro,preco):
    return preco - bombom(dinheiro,preco)[1]