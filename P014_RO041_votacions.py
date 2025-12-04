#P014_RO041_votacions

print("Vots a favor = 1")
print("Vots en contra = 2")
print("Qualsevol altre opció és nula")

n = int(input("El teu vot: "))

vots_si = 0
vots_no = 0
vots_nuls = 0

i = 1
while i < n + 1:
    print("vot",i, " =", end = " ")
    vot = int(input())
    if vot == 1:
        vots_si = vots_si + 1
    elif vot == 0:
        vots_no = vots_no + 1
    else:
        print("Opció incorrecte, vot nul")
        vots_nuls = vots_nuls + 1
    i = i + 1
print("Total de vots: ",n)
print("Vots afirmatius",vots_si)
print("Vots negatius",vots_no)
print("Vots nuls", vots_nuls)