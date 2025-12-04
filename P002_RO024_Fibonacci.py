#P003_RO024_Fibonacci.py
anterior = 0
fibonacci = 1
maxim = 100

print("Sèrie de Fibonacci dels ", maxim , "primers nombres/n")
print(0, fibonacci, end = " ")

while fibonacci < maxim:
    x = fibonacci # x -- variable intermitja
    fibonacci = fibonacci + anterior
    anterior = x
    print(fibonacci)
