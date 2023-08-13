import random
bon_nimewo = random.randint(1,30)

nonb_chans = 5
while nonb_chans > 0:
    nonb_chans = nonb_chans-1
    nimewo_chwazi = input("Antre yon nimewo ant 1 a 30 . ")
    nimewo_chwazi = int(nimewo_chwazi)
    if nimewo_chwazi < bon_nimewo:
        print("Nimewo ou chwazi a two piti.")
    elif nimewo_chwazi > bon_nimewo:
        print("Nimewo ou chwazi two gwo.")
    else:
        print()
        break

if nonb_chans > 0:
    print("Bravo! Ou jwenn bon nimewo a ki se "+str(nimewo_chwazi)+" sou",5-nonb_chans,"tantatif.")
else:
    print("Ou fin ak tout 5 chans ou te gen yo, dezole ou pa ret chans anko!")