nonbNot = input("Antre kantite not ou vle itilize a : ")
nonbNot = int(nonbNot)

somToutNotYo = 0

for i in range(1,nonbNot+1):
    notElev = input("Antre not elev la fe sou 100 : ")
    notElev = int(notElev)
    somToutNotYo = somToutNotYo+notElev

mwayen = somToutNotYo/nonbNot

if mwayen >= 90 :
    print("Ou fe : A")
elif mwayen >= 80 :
    print("Ou fe : B")
elif mwayen >= 70 :
    print("Ou fe : C")
elif mwayen >= 60 :
    print("Ou fe : D")
else :
    mwayen < 60
    print("Ou fe : F")
