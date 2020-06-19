import random
a=-1
b=2
lungime_cromozom=16
populatie=50;
nr_etape=100
rata_mutatie=0.01
probabilitate_recombinare=0.25
precizie=6
random.seed()
numbers=[(random.getrandbits(lungime_cromozom)) for i in range(populatie)]

#print(*numbers,sep='\n')
def f(x) -> float:
    return -(x*x)+x+2 
def base2_to_dec(x):
    return int(x)*(b-a)/(2**lungime_cromozom-1) + a
    rez=0;
    l=lungime_cromozom
    while(x):
        rez+=((b-a)/(2^l-1) + a)
        l-=1
def binary_search(vector,u):
    left=0
    right=len(vector)-1
    while left<=right:
        mid=(left + right)//2
        if vector[mid]<u and mid+1==len(vector):
            return mid
        if vector[mid]<u and vector[mid+1]>u:
            return mid
        elif vector[mid]<u:
            left=mid+1
        else:
            right=mid-1
    return mid
    exit()

def print_evolutie():
    for x in selectie:
        x=round(x,precizie)
    for i in range(len(selectie)):
        print("%d: %s x=%."+str(precizie)+"f" %(i,bin(selectie[i]),selectie[i],f(selectie[i])))
def incrucisaza(x,y):
    punct_taietura=random.randint(0,lungime_cromozom-1)
    print("%s %s punct=%d" % (bin(x),bin(y),punct_taietura))
    x2=int(bin(x)[2:punct_taietura+2]+bin(y)[punct_taietura+2:lungime_cromozom-1+2],2)
    y2=int(bin(y)[2:punct_taietura+2]+bin(x)[punct_taietura+2:lungime_cromozom-1+2],2)
    print("Rezultat %s %s" %(bin(x2),bin(y2)))
    return (x2,y2)
x=[]
for i in numbers:
     x.append(base2_to_dec(i))
(print(bin(i)) for i in x)
numbers_dec=x[:]
#

maxime=[]
for etapa in range(nr_etape):
    for i in range(populatie):
        numbers_dec[i]=base2_to_dec(numbers[i])
    maxim=f(numbers_dec[0])
    suma=0
    for i in numbers_dec:
        suma+=f(i)
        maxim=max(maxim,f(i))
    
    intervale=[f(i)/suma for i in numbers_dec]
    print("Intervale probabilitati selectie")
    
    #intervale.sort()
    intervale.insert(0,0)
    
    for i in range(1,len(intervale)):
        intervale[i]=intervale[i]+intervale[i-1]
    print(intervale)
    print(sum(intervale))
    selectie=[]
    for i in range(populatie):
        u=random.uniform(0,1)
        individ=binary_search(intervale,u)
        #print("u=%f Selectam cromozomul %d" % (u,individ))
        selectie.append(individ)
    #incrucisare
    lista_incrucisat=[]
    for i in range(len(selectie)):
        u=random.uniform(0,1)
        if(u<probabilitate_recombinare):
            lista_incrucisat.append(i)
    random.shuffle(lista_incrucisat)

    for i in range(0,len(lista_incrucisat)//2):
        print("Recombinare dintre cromozomul %d cu cromozomul %d:" %(lista_incrucisat[i],lista_incrucisat[-i-1]))
        x,y= incrucisaza(numbers[selectie[lista_incrucisat[i]]],numbers[selectie[lista_incrucisat[-i-1]]])
        (numbers[selectie[lista_incrucisat[i]]],numbers[selectie[lista_incrucisat[-i-1]]])=(x,y)
        #numbers_dec[selectie[lista_incrucisat[i]]]=base2_to_dec(numbers[selectie[lista_incrucisat[i]]])
        #numbers_dec[selectie[lista_incrucisat[i]]]=base2_to_dec(numbers[selectie[lista_incrucisat[i]]])

    #mutatie
    cromozomi_modificati=[]
    for i_s in range(len(selectie)):
        u=random.uniform(0,1)
        if(u<rata_mutatie):
            cromozomi_modificati.append(i_s)
            bits_to_be_flipped=min(int(rata_mutatie//u+1),lungime_cromozom)
            for i in range(bits_to_be_flipped):
                rand=random.randint(0,lungime_cromozom-1)
                numbers[selectie[i_s]]= numbers[selectie[i_s]] ^ (1 << rand)
    if len(cromozomi_modificati)>0:
        print("Au fost modificati cromozomii: "),
        print(cromozomi_modificati)
    maxime.append(maxim)
    numbers=[numbers[i] for i in selectie]
print(*maxime,sep='\n')