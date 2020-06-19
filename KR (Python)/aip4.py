sir = "Candva, demult, acum 1000 de ani traia o printesa intr-un castel. Si printesa intr-o zi auzi cum aparuse pe meleagurile sale un cufar fermecat din care iesea grai omenesc. Printesa curioasa strabatu 7 ulite si 7 piete; ajunse la cufar si vazu ca toti stateau la 100 metri distanta de el si se mirau. Din cufar intr-adevar se auzeau vorbe nedeslusite. Printesa curajoasa se duse sa-i vorbeasca. Il intreba cine e si ce dorinte are. Raspunsul fu: \"Sunt Ion am cazut in cufar si m-am ferecat din gresala. As dori sa ies.\". Printesa deschise cufarul si-l elibera pe Ion. 'Multumesc' spuse Ion. Si astfel, povestea cufarului fermecat a fost deslusita."

#print(len(sir))

def alfa(sir):
    nstr = []
    for i in sir:
        if not i.isalnum() and i != '-' and i not in nstr:
            nstr.append(i)
    return nstr

def punctulC(sir, nAlf):

    nouSir = [cuv.strip(nAlf) for cuv in sir.split()]
    nouSir = list(set(nouSir))

    for i in nouSir:
        i = i.lower()
    return nouSir

def punctulD(sir):
    for i in sir:
        if i.endswith("ul"):
            print(i)

def punctulE(sir):
    for i in sir:
        if i.find('-') != -1:
            print(i)

nAlf = alfa(sir)
Nalf = ""
for i in nAlf:
    Nalf += i

sir = punctulC(sir, Nalf)

# punctulD(sir)
punctulE(sir)






