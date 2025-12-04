#PO04_RO025_Paritmetica_03.py
""" cometes llargues = comentari similiar al del #
"""

a1 = -203
an = 902.5 #terme enèssim
d = 16.5

n = ((an - a1) / d ) + 1
print("n = ",n)
print()

k = n

n = 1
s = 0

print("n            a              s          ")

while n < k+1:
    a = a1 + (n-1) * d
    s = a + s
    print(n,"     ",a,"        ",      s)
    n = n + 1