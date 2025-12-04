#P008_RO035_bacteris.py

n_bacteris = int(input("Número de bacteris: "))
max_bacteris = int(input("Número maxim de bacteris: "))
dia = 0 #condicions inicials

while n_bacteris <= max_bacteris :
    print("dia", dia, "n_bacteris = ", n_bacteris)
    n_bacteris = n_bacteris * 2
    dia = dia + 1

print("dia", dia, "n_bacteris = ", n_bacteris)