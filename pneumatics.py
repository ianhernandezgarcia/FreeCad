

n = int(input("Quantitat de pneumàtics: "))
p = int(input("Preu dels pneumàtics: "))


if n > 4:
    p = 0.9 * p
    print("Valor total: ",n * p,)