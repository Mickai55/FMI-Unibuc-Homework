import time
from copy import copy, deepcopy

class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 8
    NR_LINII = 8
    SIMBOLURI_JUC = ['n', 'a']
    JMIN = None
    JMAX = None
    GOL = '.'
    def __init__(self, tabla = None):
        self.matr = tabla or   [['.', '.', '.', '.', '.', '.', '.', '.'],
                                ['.', '.', '.', '.', '.', '.', '.', '.'],
                                ['.', '.', '.', '.', '.', '.', '.', '.'],
                                ['.', '.', '.', 'a', 'n', '.', '.', '.'],
                                ['.', '.', '.', 'n', 'a', '.', '.', '.'],
                                ['.', '.', '.', '.', '.', '.', '.', '.'],
                                ['.', '.', '.', '.', '.', '.', '.', '.'],
                                ['.', '.', '.', '.', '.', '.', '.', '.']]

    def final(self):
    
        locuriLibere = self.nrPiese('.')

        if locuriLibere == 0 or (not verifDacaExistaMutariValide(self.matr, 'a') and not verifDacaExistaMutariValide(self.matr, 'n')):
            pieseAlbe = self.nrPiese('a')
            pieseNegre = self.nrPiese('n')
            
            if pieseAlbe > pieseNegre:
                return 'a'
            elif pieseAlbe < pieseNegre:
                return 'n'
            else:
                return 'Remiza'

        return False

    def mutari(self, jucator):

        l_mutari=[]

        for i in range(self.NR_LINII):
            for j in range(self.NR_COLOANE):
                matr_tabla_noua = deepcopy(self.matr)

                verif = False
                if matr_tabla_noua[i][j] == Joc.GOL:
                    matr_tabla_noua, verif = pozitieValida(matr_tabla_noua, jucator, i, j)

                if verif:
                    l_mutari.append(Joc(matr_tabla_noua))

        return l_mutari

    def nrPiese(self, jucator):
        
        piese = 0
        for i in self.matr:
            for j in i:
                if j == jucator:
                    piese += 1
        
        return piese

    def fct_euristica(self):

        return self.nrPiese(Joc.JMAX) - self.nrPiese(Joc.JMIN)

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == Joc.JMAX :
            return (999+adancime)
        elif t_final == Joc.JMIN:
            return (-999-adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.fct_euristica()


    def __str__(self):
        sir = '  '
        for col in range(self.NR_COLOANE):
            sir += str(col) + ' '
        sir += '\n'

        for lin in range(self.NR_LINII):
            sir += str(lin) + " "
            for col in range(self.NR_COLOANE):
                sir += str(self.matr[lin][col]) + " "
            sir += '\n'
        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        #adancimea in arborele de stari
        self.adancime=adancime

        #scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor=scor

        #lista de mutari posibile din starea curenta
        self.mutari_posibile=[]

        #cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa=None

    def jucator_opus(self):
        if self.j_curent==Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari(self):
        l_mutari=self.tabla_joc.mutari(self.j_curent)

        juc_opus=self.jucator_opus()
        l_stari_mutari=[Stare(mutare, juc_opus, self.adancime-1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari


    def __str__(self):
        sir= str(self.tabla_joc) + "(Juc curent: "+self.j_curent+")\n"
        return sir



""" Algoritmul MinMax """

def min_max(stare):

    if stare.adancime==0 or stare.tabla_joc.final() :
        stare.scor=stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    #calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    #aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor=[min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent==Joc.JMAX :
        #daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        #daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    stare.scor=stare.stare_aleasa.scor
    return stare



def alpha_beta(alpha, beta, stare):
    if stare.adancime==0 or stare.tabla_joc.final() :
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    if alpha >= beta:
        return stare #este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX :
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            #calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if(alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN :
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if(beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break
    
    if stare is not None:
        stare.scor = stare.stare_aleasa.scor

    return stare



def afis_daca_final(stare_curenta):
    # ?? TO DO:
    # de adagat parametru "pozitie", ca sa nu verifice mereu toata tabla,
    # ci doar linia, coloana, 2 diagonale pt elementul nou, de pe "pozitie"

    final = stare_curenta.tabla_joc.final()
    if(final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False

def pozitieValida(tabla, jucator, linie, coloana):

    adversar = 'a' if jucator == 'n' else 'n' # luam adversarul

    valid = False
    
    # linii ->
    nr, nrAdv = 0, 0
    for i in range(coloana + 1, Joc.NR_LINII):
        nr += 1
        if tabla[linie][i] == adversar:
            nrAdv += 1
        if tabla[linie][i] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            for i in range(coloana + 1, i):
                tabla[linie][i] = jucator

            valid = True
            break
    
    # linii <-
    nr, nrAdv = 0, 0
    for i in range(coloana - 1, -1, -1):
        nr += 1
        if tabla[linie][i] == adversar:
            nrAdv += 1
        if tabla[linie][i] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            for i in range(coloana - 1, i, -1):
                tabla[linie][i] = jucator

            valid = True
            break
    
    # coloane \/
    nr, nrAdv = 0, 0
    for i in range(linie + 1, Joc.NR_COLOANE):
        nr += 1
        if tabla[i][coloana] == adversar:
            nrAdv += 1
        if tabla[i][coloana] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            for i in range(linie + 1, i):
                tabla[i][coloana] = jucator

            valid = True
            break
    
    # coloane /\
    nr, nrAdv = 0, 0
    for i in range(linie - 1, -1, -1):
        nr += 1
        if tabla[i][coloana] == adversar:
            nrAdv += 1
        if tabla[i][coloana] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            for i in range(linie - 1, i, -1):
                tabla[i][coloana] = jucator

            valid = True
            break
    
    # diagonale \ jos
    nr, nrAdv = 0, 0
    col = coloana
    for i in range(linie + 1, Joc.NR_COLOANE):
        col += 1
        if col == Joc.NR_COLOANE:
            break
        nr += 1
        if tabla[i][col] == adversar:
            nrAdv += 1
        if tabla[i][col] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            col = coloana
            for i in range(linie + 1, i):
                col += 1
                tabla[i][col] = jucator

            valid = True
            break
    
    #digonale \ sus
    nr, nrAdv = 0, 0
    col = coloana
    for i in range(linie - 1, -1, -1):
        col -= 1
        if col == -1:
            break
        nr += 1
        if tabla[i][col] == adversar:
            nrAdv += 1
        if tabla[i][col] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            col = coloana
            for i in range(linie - 1, i, -1):
                col -= 1
                tabla[i][col] = jucator

            valid = True
            break
    
    # diagonale / jos
    nr, nrAdv = 0, 0
    col = coloana
    for i in range(linie + 1, Joc.NR_COLOANE):
        col -= 1
        if col == -1:
            break
        nr += 1
        if tabla[i][col] == adversar:
            nrAdv += 1
        if tabla[i][col] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            col = coloana
            for i in range(linie + 1, i):
                col -= 1
                tabla[i][col] = jucator

            valid = True
            break
    
    # diagonale / jos
    nr, nrAdv = 0, 0
    col = coloana
    for i in range(linie - 1, -1, -1):
        col += 1
        if col == Joc.NR_COLOANE:
            break
        nr += 1
        if tabla[i][col] == adversar:
            nrAdv += 1
        if tabla[i][col] == jucator and nr - 1 == nrAdv and nrAdv != 0:
            col = coloana
            for i in range(linie - 1, i, -1):
                col += 1
                tabla[i][col] = jucator

            valid = True
            break
    
    if valid:
        tabla[linie][coloana] = jucator

    return tabla, valid

def verifDacaExistaMutariValide(tabla, jucator):

    t = deepcopy(tabla)

    for i in range(Joc.NR_LINII):
        for j in range(Joc.NR_COLOANE):
            if t[i][j] == Joc.GOL:
                x, valid = pozitieValida(t, jucator, i, j)
                if valid:
                    return True
    return False

def main():
    
    raspuns_valid=False
    while not raspuns_valid:
        tip_algoritm=input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1','2']:
            raspuns_valid=True
        else:
            print("Nu ati ales o varianta corecta.")
    tip_algoritm = 2

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        n = input("Adancime maxima a arborelui: ")
        if n.isdigit():
            Stare.ADANCIME_MAX = int(n)
            raspuns_valid = True
        else:
            print("Trebuie sa introduceti un numar natural nenul.")
    Stare.ADANCIME_MAX = 3

    # initializare jucatori
    [s1, s2] = Joc.SIMBOLURI_JUC.copy()  # lista de simboluri posibile
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = str(input("Doriti sa jucati cu {} sau cu {}? ".format(s1, s2)))
        if Joc.JMIN in ["a", "n"]:
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
    Joc.JMAX = s1 if Joc.JMIN == s2 else s2

    #initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    #creare stare initiala
    stare_curenta = Stare(tabla_curenta, Joc.SIMBOLURI_JUC[0], Stare.ADANCIME_MAX)

    linie = -1
    coloana = -1
    while True :
        if (stare_curenta.j_curent == Joc.JMIN):

            if verifDacaExistaMutariValide(stare_curenta.tabla_joc.matr, stare_curenta.j_curent):

                #muta jucatorul
                raspuns_valid = False
                while not raspuns_valid :
                    linie = int(input("linie = "))
                    coloana = int(input("coloana = "))

                    if (linie in range(0, 8) and coloana in range(0, 8)):
                        if stare_curenta.tabla_joc.matr[linie][coloana] == Joc.GOL:
                            stare_curenta.tabla_joc.matr, valid = pozitieValida(stare_curenta.tabla_joc.matr, stare_curenta.j_curent, linie, coloana)
                            if valid:
                                raspuns_valid=True
                            else:
                                print("Pozitia nu e valida")
                        else:
                            print("Exista deja un simbol in pozitia ceruta.")
                    else:
                        print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele 0 - 7).")

                #afisarea starii jocului in urma mutarii utilizatorului
                print("\nTabla dupa mutarea jucatorului")
                print(str(stare_curenta))

            else:
                print("Jucatorul nu poate muta!")

            #testez daca jocul a ajuns intr-o stare finala
            #si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break


            #S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

        #--------------------------------
        else: #jucatorul e JMAX (calculatorul)

            #preiau timpul in milisecunde de dinainte de mutare
            if verifDacaExistaMutariValide(stare_curenta.tabla_joc.matr, stare_curenta.j_curent):
                t_inainte=int(round(time.time() * 1000))
                if tip_algoritm == 1:
                    stare_actualizata = min_max(stare_curenta)
                else: #tip_algoritm==2
                    stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)
                stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
                print("Tabla dupa mutarea calculatorului")
                print(str(stare_curenta))

                #preiau timpul in milisecunde de dupa mutare
                t_dupa=int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de "+str(t_dupa - t_inainte)+" milisecunde.")

            else:
                print("Calculatorul nu poate muta!")

            if (afis_daca_final(stare_curenta)):
                break

                #S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

if __name__ == "__main__" :
        main()