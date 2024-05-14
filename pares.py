def lista(n):
    if n%2 == 0:
        return list(range(2, n+1, 2))
    else:
        return list(range(2, n , 2))
    