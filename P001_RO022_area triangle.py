# P001_RO022_area triangle.py

from math import *

print("Càlcul de l'àrea d'un triangle. Costats en cm, àrea en cm2")

a = int(input("costat d'a = "))
b = int(input("costat de b = "))
c = int(input("costat de c = "))

semiperimetre = (a + b + c)/2
t = semiperimetre #meitat del perímetre
s = sqrt(t*(t-a)*(t-b)*(t-c))

print("Semiperímetre = ",t, "cm")
print("Àrea = ",s, "cm2")
#print(cos(s))