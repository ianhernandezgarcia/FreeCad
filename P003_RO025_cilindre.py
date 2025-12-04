#P002_RO025_cilindre.py

pi = 3.1416

radi = int(input("Radi = "))
altura = int(input("Altura = "))

print("Àrea i volum d'un cilindre. Dades en cm. ")
#volum = pi * radi * radi * altura
#volum = pi * radi**2 * altura
volum = pi * (pow(radi,2)) * altura

print("Volum = ",volum, "cm3")