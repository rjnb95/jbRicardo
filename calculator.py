nonbNot = input("Antre kantite not ou vle itilize a : ")
nonbNot = int(nonbNot)

somToutNotYo = 0

for i in range(1,nonbNot+1):
    notElev = input("Antre not elev la fe sou 100 : ")
    notElev = int(notElev)
    somToutNotYo = somToutNotYo+notElev

mwayen = somToutNotYo/nonbNot

print("Bonjour, mwayen elev sa se : "+str(mwayen)+" sou 100.")