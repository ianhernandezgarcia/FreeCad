#P005_RO025_repte
#resultat dels examens assolits d'una matèria

print("Resultat dels examens assolits d'una matèria sobre 100 punts")
print()

ex_1 = int(input("Nota examen sobre 100: "))
llico_2 = int(input("Nota llico sobre 10: "))
tasca_1 = int(input("Nota tasca 1 sobre 10: "))
tasca_2 = int(input("Nota tasca 2 sobre 10: "))
tasca_3 = int(input("Nota tasca 3 sobre 10: "))



N1 = (ex_1/10) * 0.7
N2 = llico_2 * 0.2
N3 = tasca_1 * 0.033
N4 = tasca_2 * 0.033
N5 = tasca_3 * 0.033

r = (N1 + N2 + N3 + N4 + N5)*10

print()
print ("La teva nota total sobre 100 és:",r)





