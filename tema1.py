litere=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
relatii=['<','>','^','~']
############################################
# < - SAU
# > - IMPLICA
# ^ - SI
# ~ - NOT
############################################
i=0
def vp(p):
    #p=propozitia
    global i
    if p[i]=="~":
        if p[i+1] in litere and p[i+2]==")":
            i=i+2
            return 1
        elif p[i+1]=="(":
            i=i+2
            if vp(p) and p[i]==")":
                if i+1<len(p):
                    # Trebuie sa verific daca la returnare unde vom avea conditia p[i]==")" va exista i-ul respectiv. De exemplu: pentru propozitia (A<(A<B) lipseste ultima paranteza, insa asta nu poate fi verificat deoarece sirul se tarmina la ultima paranteza. In acest caz, programul ar fi dat eroare.
                    i=i+1
                    return 1
                else:
                    return 0
    if p[i] in litere:
        if p[i+1] in relatii:
            if p[i+2] in litere:
                if i+3<len(p):
                    i=i+3
                    return 1
                else:
                    return 0
            if p[i+2]=="(":
                i=i+3
                if vp(p) and p[i]==")":
                    if i+1<len(p):
                        i=i+1
                        return 1
                    else:
                        return 0
    elif p[i]=="(":
        i=i+1
        if vp(p):
            if p[i+1] in relatii:
                if p[i+2] in litere:
                    if i+3<len(p):
                        i=i+3
                        return 1
                    else:
                        return 0
                if p[i+2]=="(":
                    i=i+3
                    if vp(p) and p[i]==")":
                        if i+1<len(p):
                            i=i+1
                            return 1
                        else:
                            return 0
            elif p[i]==")":
                if i+1<len(p):
                    i=i+1
                    return 1
                else:
                    return 0
            

propozitia=input('Introduceti propozitia:')
if propozitia in litere:
    print("Corect!")
elif propozitia[i]=="(":
    i=i+1
    if vp(propozitia) and propozitia[i]==")" and i==len(propozitia)-1:
        # Am pus ultima conditie pentru a verifica daca porpozitia se termina sau nu. De exemplu: pentru propozitia (A<B)<B programul afisa mesajul "Corect" fara ultima conditie deoarece el a verificat prima paranteza doar.
        print("Corect!")
    else:
        print("Gresit!")
else:
    print("Gresit!")


