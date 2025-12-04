#P009_RO032_conversio-temp.py
tf = 0
t = float(input("temperatura = "))
print("Conversió a ºC = 1")
print("Conversió a ºF = 2")
conversio = int(input("Prem 1 o 2 segons la conversió que vols: "))

if conversio == 1:
    tc = (5/9) * (t-32)
    
elif conversio == 2:
    tf = (32+9) * (t/5)
    
print(t,"ªC ",tf, "ºF")

