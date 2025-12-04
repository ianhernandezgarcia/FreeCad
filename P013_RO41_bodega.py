#P0013_RO41_bodega

n = int(input("Número de paquets: "))
pes_maxim = 0
i = 1
while i <= n:
    print("Pes del paquet ",i, " en kg:", end = " ")
    pes = int(input())
    if pes > pes_maxim:
        pes_maxim = pes
    i = i + 1
print("Pes màxim : ", pes_maxim,  " kg")

#for in range

pes_maxim = 0
for i in range (1,n+1):
    print("Pes del paquet ",i, " en kg:", end = " ")
    pes = int(input())
    if pes > pes_maxim:
        pes_maxim = pes
    i = i +1
print("Pes màxim : ", pes_maxim, " kg")