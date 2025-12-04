#P021_RO044_exemple1

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

r = 0
n = 10
i  = 0

while not ((a < b) or (c <= b)) and (i <= n):
    print("i = ", i, end = " ")
    if b % 2 == 0:
        b = b - 1
        print("b = ",b)
    else:
        r = r + c
        b = b - c
        print("b = ",b, "r = ",r)
        
    i = i + 1
    
print("r = ",r)
 
    