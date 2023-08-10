#Enteraksyon ak itilizate a
nonb = input("Rantre yon nonb soti nan 1 pou rive nan 10.  ")

#jenere tab miltiplikasyon an
for tab in range(1,11):
    tab*int(nonb)
    print(str(nonb)," x ",str(tab), " = ",tab*int(nonb))

nouvoTab = input("Peze 'w' si ou vle jenere yon tab anko, si non peze 'n'.")
while nouvoTab =="w":
    nonb = input("Rantre yon nonb soti nan 1 pou rive nan 10.  ")
    for tab in range(1,11) :   
        tab*int(nonb)
        print(str(nonb)," x ",str(tab), " = ",tab*int(nonb))
    nouvoTab = input("Peze 'w' si ou vle jenere yon tab anko, si non peze 'n'.")
if nouvoTab =="n":
    print("Mese paske ou te itilize pwogram nou an, orevwa!")
else:
    print("Ou dwe peze 'w' oubyen 'n' selman")
