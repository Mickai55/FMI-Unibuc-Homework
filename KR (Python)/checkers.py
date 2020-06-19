import time


#ADD VERIFICARE DACA NU MAI POT FACE NICIO MISCARE => WIN/LOSE
# VERIFICARE DACA ESTI CU ALB MUTARI!!! (REGI SUS)
adancime = 0
class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 8
    NR_LINII = 8
    JMIN = None
    JMAX = None
    GOL = '.'

    #mutarile sunt concepute astfel incat calculatorul poate muta doar in jos(cand are regi ei pot merge in orice directie) iar jucatorul in sus
    def __init__(self, tabla = None):
        if tabla is None:
            # self.matr = ['.', self.JMAX, '.', self.JMAX, '.', self.JMAX, '.', self.JMAX,
            #             self.JMAX, '.', self.JMAX, '.', self.JMAX, '.', self.JMAX, '.',
            #             '.', self.JMAX, '.', self.JMAX, '.', self.JMAX, '.', self.JMAX,
            #             '.', '.', '.', '.', '.', '.', '.', '.',
            #             '.', '.', '.', '.', '.', '.', '.', '.',
            #             self.JMIN, '.', self.JMIN, '.', self.JMIN, '.', self.JMIN, '.',
            #             '.', self.JMIN, '.', self.JMIN, '.', self.JMIN, '.', self.JMIN,
            #             self.JMIN, '.', self.JMIN, '.', self.JMIN, '.', self.JMIN, '.']
            self.matr = ['.', '.', '.', '.', '.', '.', '.', '.',
                        self.JMIN, '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', self.JMAX.upper(), '.',
                        '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.',]
        else:
            self.matr = tabla

    def final(self):

        if self.nrMutariJucatorMAX() == 0:
            return Joc.JMIN # JMIN a castigat
        elif self.nrMutariJucatorMIN() == 0:
            return Joc.JMAX # JMIN a castigat
        

        pieseMIN = 0
        pieseMAX = 0

        for i in range(len(self.matr)):
            if self.matr[i] == Joc.JMIN or self.matr[i] == Joc.JMIN.upper():
                pieseMIN += 1
            elif self.matr[i] == Joc.JMAX or self.matr[i] == Joc.JMAX.upper():
                pieseMAX += 1
        
        if pieseMAX == 0:
            return Joc.JMIN # JMIN a castigat
        elif pieseMIN == 0:
            return Joc.JMAX # JMAX a castigat

        return False

    def mutari(self, jucator):
        
        l_mutari = []


        for i in range(len(self.matr)):
            if self.matr[i] == jucator:
            #mutari normale pentru ambii jucatori (MAX in jos si MIN in sus)


                # daca jucatorul este MAX (muta in jos)
                if self.matr[i] == Joc.JMAX:

                    if (i < 56): # adica nu ne aflam pe ultima linie
                        #mutare in jos la stanga
                        if i % 8 != 0:
                            if self.matr[i + 7] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 7] = Joc.JMAX
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i + 9] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 9] = Joc.JMAX
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))

                    if i < 48: # adica nu ne aflam pe ultimele 2 linii
                        #mutare in jos la stanga cu capturare
                        if i % 8 != 0 and (i - 1) % 8 != 0:
                            if self.matr[i + 14] == Joc.GOL and (self.matr[i + 7] == Joc.JMIN or self.matr[i + 7] == Joc.JMIN.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 14] = Joc.JMAX
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i + 7] = Joc.GOL # dispare adversarul
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta cu capturare
                        if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                            if self.matr[i + 18] == Joc.GOL and (self.matr[i + 9] == Joc.JMIN or self.matr[i + 9] == Joc.JMIN.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 18] = Joc.JMAX
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i + 9] = Joc.GOL # dispare adversarul
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))

                # jucatorul este MIN (muta in sus)
                elif self.matr[i] == Joc.JMIN:

                    if i > 7: # adica nu ne aflam pe prima linie
                        #mutare in sus la stanga
                        if i % 8 != 0:
                            if self.matr[i - 9] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 9] = Joc.JMIN
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in sus la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i - 7] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 7] = Joc.JMIN
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))
                    
                    if i > 15: # adica nu ne aflam pe primele 2 linii    
                        #mutare in sus la stanga cu capturare
                        if i % 8 != 0 and (i - 1) % 8 != 0:
                            if self.matr[i - 18] == Joc.GOL and (self.matr[i - 9] == Joc.JMAX or self.matr[i - 9] == Joc.JMAX.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 18] = Joc.JMIN
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i - 9] = Joc.GOL # dispare adversarul
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta cu capturare
                        if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                            if self.matr[i - 14] == Joc.GOL and (self.matr[i - 7] == Joc.JMAX or self.matr[i - 7] == Joc.JMAX.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 14] = Joc.JMIN
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i - 7] = Joc.GOL # dispare adversarul
                                matr_tabla_noua = transformare(matr_tabla_noua, jucator)
                                self.matr = transformare(self.matr, jucator)
                                l_mutari.append(Joc(matr_tabla_noua))       

                # daca ajung la final pot merge si inapoi (cu regii)!!!

                # mutari pentru piesele regi (pentru ambele tabere)

                # in directia normala (doar ca sunt regi piesele)

                # daca jucatorul este MAX (muta in jos)
                if self.matr[i] == Joc.JMAX.upper():

                    print("dadada")

                    if (i < 56): # adica nu ne aflam pe ultima linie
                        #mutare in jos la stanga
                        if i % 8 != 0:
                            if self.matr[i + 7] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 7] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i + 9] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 9] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))

                    if i < 48: # adica nu ne aflam pe ultimele 2 linii
                        #mutare in jos la stanga cu capturare
                        if i % 8 != 0 and (i - 1) % 8 != 0:
                            if self.matr[i + 14] == Joc.GOL and (self.matr[i + 7] == Joc.JMIN or self.matr[i + 7] == Joc.JMIN.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 14] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i + 7] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta cu capturare
                        if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                            if self.matr[i + 18] == Joc.GOL and (self.matr[i + 9] == Joc.JMIN or self.matr[i + 9] == Joc.JMIN.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 18] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i + 9] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))

                # jucatorul este MIN (muta in sus)
                elif self.matr[i] == Joc.JMIN.upper():

                    if i > 7: # adica nu ne aflam pe prima linie
                        #mutare in sus la stanga
                        if i % 8 != 0:
                            if self.matr[i - 9] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 9] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in sus la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i - 7] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 7] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))
                    
                    if i > 15: # adica nu ne aflam pe primele 2 linii    
                        #mutare in sus la stanga cu capturare
                        if i % 8 != 0 and (i - 1) % 8 != 0:
                            if self.matr[i - 18] == Joc.GOL and (self.matr[i - 9] == Joc.JMAX or self.matr[i - 9] == Joc.JMAX.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 18] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i - 9] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta cu capturare
                        if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                            if self.matr[i - 14] == Joc.GOL and (self.matr[i - 7] == Joc.JMAX or self.matr[i - 7] == Joc.JMAX.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 14] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i - 7] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))
        
                # mutari inverse pentru regi

                # daca jucatorul este MAX (muta in sus)
                if self.matr[i] == Joc.JMAX.upper():

                    if i > 7: # adica nu ne aflam pe prima linie
                        #mutare in sus la stanga
                        if i % 8 != 0:
                            if self.matr[i - 9] == Joc.GOL:
                                print("da")
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 9] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))

                        #mutare in sus la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i - 7] == Joc.GOL:
                                print("da")
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 7] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))
                    
                    if i > 15: # adica nu ne aflam pe primele 2 linii    
                        #mutare in sus la stanga cu capturare
                        if i % 8 != 0 and (i - 1) % 8 != 0:
                            if self.matr[i - 18] == Joc.GOL and (self.matr[i - 9] == Joc.JMIN or self.matr[i - 9] == Joc.JMIN.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 18] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i - 9] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta cu capturare
                        if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                            if self.matr[i - 14] == Joc.GOL and (self.matr[i - 7] == Joc.JMIN or self.matr[i - 7] == Joc.JMIN.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i - 14] = Joc.JMAX.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i - 7] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))


                # jucatorul este MIN (muta in sus)
                elif self.matr[i] == Joc.JMIN.upper():

                    if (i < 56): # adica nu ne aflam pe ultima linie
                        #mutare in jos la stanga
                        if i % 8 != 0:
                            if self.matr[i + 7] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 7] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i + 9] == Joc.GOL:
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 9] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                l_mutari.append(Joc(matr_tabla_noua))

                    if i < 48: # adica nu ne aflam pe ultimele 2 linii
                        #mutare in jos la stanga cu capturare
                        if i % 8 != 0 and (i - 1) % 8 != 0:
                            if self.matr[i + 14] == Joc.GOL and (self.matr[i + 7] == Joc.JMAX or self.matr[i + 7] == Joc.JMAX.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 14] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i + 7] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))
                        #mutare in jos la dreapta cu capturare
                        if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                            if self.matr[i + 18] == Joc.GOL and (self.matr[i + 9] == Joc.JMAX or self.matr[i + 9] == Joc.JMAX.upper()):
                                matr_tabla_noua = self.matr.copy()
                                matr_tabla_noua[i + 18] = Joc.JMIN.upper()
                                matr_tabla_noua[i] = Joc.GOL
                                matr_tabla_noua[i + 9] = Joc.GOL # dispare adversarul
                                l_mutari.append(Joc(matr_tabla_noua))
                    
        # for i in l_mutari:
        #     print(i)

        return l_mutari

    def nrPiese(self, jucator):

        piese = 0

        for i in range(len(self.matr)):
            if self.matr[i] == jucator or self.matr[i] == jucator.upper():
                piese += 1
        
        return piese

    def nrMutariJucatorMAX(self):

        mutari = 0
        for i in range(len(self.matr)):

            if self.matr[i] == Joc.JMAX or self.matr[i] == Joc.JMAX.upper():

                if (i < 56): # adica nu ne aflam pe ultima linie
                    #mutare in jos la stanga
                    if i % 8 != 0:
                        if self.matr[i + 7] == Joc.GOL:
                            mutari += 1
                    #mutare in jos la dreapta
                    if (i + 1) % 8 != 0:
                        if self.matr[i + 9] == Joc.GOL:
                            mutari += 1

                if i < 48: # adica nu ne aflam pe ultimele 2 linii
                    #mutare in jos la stanga cu capturare
                    if i % 8 != 0 and (i - 1) % 8 != 0:
                        if self.matr[i + 14] == Joc.GOL and (self.matr[i + 7] == Joc.JMIN or self.matr[i + 7] == Joc.JMIN.upper()):
                            mutari += 1
                    #mutare in jos la dreapta cu capturare
                    if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                        if self.matr[i + 18] == Joc.GOL and (self.matr[i + 9] == Joc.JMIN or self.matr[i + 9] == Joc.JMIN.upper()):
                            mutari += 1

            if self.matr[i] == Joc.JMAX.upper():
    
                if i > 7: # adica nu ne aflam pe prima linie
                    #mutare in sus la stanga
                    if i % 8 != 0:
                        if self.matr[i - 9] == Joc.GOL:
                            mutari += 1

                    #mutare in sus la dreapta
                    if (i + 1) % 8 != 0:
                        if self.matr[i - 7] == Joc.GOL:
                            mutari += 1
                
                if i > 15: # adica nu ne aflam pe primele 2 linii    
                    #mutare in sus la stanga cu capturare
                    if i % 8 != 0 and (i - 1) % 8 != 0:
                        if self.matr[i - 18] == Joc.GOL and (self.matr[i - 9] == Joc.JMIN or self.matr[i - 9] == Joc.JMIN.upper()):
                            mutari += 1
                    #mutare in jos la dreapta cu capturare
                    if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                        if self.matr[i - 14] == Joc.GOL and (self.matr[i - 7] == Joc.JMIN or self.matr[i - 7] == Joc.JMIN.upper()):
                            mutari += 1
        return mutari

    def nrMutariJucatorMIN(self):
    
        mutari = 0
        for i in range(len(self.matr)):

            if self.matr[i] == Joc.JMIN or self.matr[i] == Joc.JMIN.upper():

                if i > 7: # adica nu ne aflam pe prima linie
                        #mutare in sus la stanga
                        if i % 8 != 0:
                            if self.matr[i - 9] == Joc.GOL:
                                mutari += 1
                        #mutare in sus la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i - 7] == Joc.GOL:
                                mutari += 1
                    
                if i > 15: # adica nu ne aflam pe primele 2 linii    
                    #mutare in sus la stanga cu capturare
                    if i % 8 != 0 and (i - 1) % 8 != 0:
                        if self.matr[i - 18] == Joc.GOL and (self.matr[i - 9] == Joc.JMAX or self.matr[i - 9] == Joc.JMAX.upper()):
                            mutari += 1
                    #mutare in jos la dreapta cu capturare
                    if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                        if self.matr[i - 14] == Joc.GOL and (self.matr[i - 7] == Joc.JMAX or self.matr[i - 7] == Joc.JMAX.upper()):
                            mutari += 1

            if self.matr[i] == Joc.JMIN.upper():
    
                if (i < 56): # adica nu ne aflam pe ultima linie
                        #mutare in jos la stanga
                        if i % 8 != 0:
                            if self.matr[i + 7] == Joc.GOL:
                                mutari += 1
                        #mutare in jos la dreapta
                        if (i + 1) % 8 != 0:
                            if self.matr[i + 9] == Joc.GOL:
                                mutari += 1

                if i < 48: # adica nu ne aflam pe ultimele 2 linii
                    #mutare in jos la stanga cu capturare
                    if i % 8 != 0 and (i - 1) % 8 != 0:
                        if self.matr[i + 14] == Joc.GOL and (self.matr[i + 7] == Joc.JMAX or self.matr[i + 7] == Joc.JMAX.upper()):
                            mutari += 1
                    #mutare in jos la dreapta cu capturare
                    if (i + 1) % 8 != 0 and (i + 2) % 8 != 0:
                        if self.matr[i + 18] == Joc.GOL and (self.matr[i + 9] == Joc.JMAX or self.matr[i + 9] == Joc.JMAX.upper()):
                            mutari += 1

        return mutari


    def fct_euristica(self):

        # return self.nrPiese(Joc.JMAX) - self.nrPiese(Joc.JMIN)
        return self.nrMutariJucatorMAX() - self.nrMutariJucatorMIN()

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
        sir = '    '
        for i in range(97, 105):
            sir += chr(i) + ' '

        sir += '\n   ----------------'

        sir += '\n'

        for lin in range(self.NR_LINII):
            k = lin * self.NR_COLOANE
            sir += (str(lin) + " | " + " ".join([str(x) for x in self.matr[k : k + self.NR_COLOANE]]) + "\n")
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
        self.adancime = adancime

        #scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        #lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        #cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent==Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari(self):
        l_mutari=self.tabla_joc.mutari(self.j_curent)

        juc_opus=self.jucator_opus()
        l_stari_mutari=[Stare(mutare, juc_opus, adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari


    def __str__(self):
        sir= str(self.tabla_joc) + "(Juc curent: "+self.j_curent+")\n"
        return sir



""" Algoritmul MinMax """

def min_max(stare):

    if stare.adancime==0 or stare.tabla_joc.final() or len(stare.mutari()) == 0:
        stare.scor=stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    #calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile=stare.mutari()

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
    if stare.adancime == 0 or stare.tabla_joc.final() or len(stare.mutari()) == 0:
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

    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    # ?? TO DO:
    # de adagat parametru "pozitie", ca sa nu verifice mereu toata tabla,
    # ci doar linia, coloana, 2 diagonale pt elementul nou, de pe "pozitie"

    final = stare_curenta.tabla_joc.final()
    if(final):
        if (final=="remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False

def miscareValida(tabla, jucator, i, directia, susjos):
    
    if jucator == Joc.JMIN:
        jucatorOpus = Joc.JMAX
    else:
        jucatorOpus = Joc.JMIN

    if i >= 0 and i <= 7 and susjos == 's': # pe linia de sus nu se mai poate muta in sus
        return False
    
    if i >= 56 and i <= 63 and susjos == 'j': # pe linia de jos nu se mai poate muta in jos
        return False
    

    if tabla[i].islower():#tabla[i] este n mic
        
        if susjos == 'j':
            return False
        if directia == 's': # directia = stanga

            if i % 8 == 0:
                return False
            if (i - 1) % 8 == 0 and tabla[i - 9] != Joc.GOL:
                return False
            if tabla[i - 9] == jucatorOpus:
                if tabla[i - 18] != Joc.GOL:
                    return False
            elif tabla[i - 9] != Joc.GOL:
                return False

        elif directia == 'd':

            if (i + 1) % 8 == 0:
                return False
            if (i + 2) % 8 == 0 and tabla[i - 7] != Joc.GOL:
                return False
            if tabla[i - 7] == jucatorOpus:
                if tabla[i - 14] != Joc.GOL:
                    return False
            elif tabla[i - 7] != Joc.GOL:
                return False

    else:#tabla[i] este n mare
        if directia == 's': # directia = stanga

            if i % 8 == 0:
                return False
            if (i - 1) % 8 == 0 and tabla[i + 7] != Joc.GOL:
                return False
            if tabla[i + 7] == jucatorOpus:
                if tabla[i + 14] != Joc.GOL:
                    return False
            elif tabla[i + 7] != Joc.GOL:
                return False

        elif directia == 'd':

            if (i + 1) % 8 == 0:
                return False
            if (i + 2) % 8 == 0 and tabla[i - 7] != Joc.GOL:
                return False
            if tabla[i + 9] == jucatorOpus:
                if tabla[i + 18] != Joc.GOL:
                    return False
            elif tabla[i + 9] != Joc.GOL:
                return False
    
    return True


def playerMove(tabla, jucator, i, directia, susjos, capturare):

    capturare = False

    if susjos == 's':

        if tabla[i].islower():

            if directia == 's': # directia = stanga

                #mutare in sus la stanga
                if tabla[i - 9] == Joc.GOL and i % 8 != 0:
                    tabla[i - 9] = Joc.JMIN
                    tabla[i] = Joc.GOL
                #mutare in sus la stanga cu capturare
                if tabla[i - 18] == Joc.GOL and i % 8 != 0 and (i - 1) % 8 != 0 and tabla[i - 9] == Joc.JMAX:
                    tabla[i - 18] = Joc.JMIN
                    tabla[i] = Joc.GOL
                    tabla[i - 9] = Joc.GOL # dispare adversarul
                    capturare = True

            else: # directia = dreapta

                #mutare in sus la dreapta
                if tabla[i - 7] == Joc.GOL and (i + 1) % 8 != 0:
                    tabla[i - 7] = Joc.JMIN
                    tabla[i] = Joc.GOL
                    
                #mutare in sus la dreapta cu capturare
                if tabla[i - 14] == Joc.GOL and (i + 1) % 8 != 0 and (i + 2) % 8 != 0 and tabla[i - 7] == Joc.JMAX:
                    tabla[i - 14] = Joc.JMIN
                    tabla[i] = Joc.GOL
                    tabla[i - 7] = Joc.GOL # dispare adversarul
                    capturare = True

        else: # daca jucatorul este rege, trebuie sa-l facem rege din nou dupa ce captureaza

            if directia == 's': # directia = stanga

                #mutare in sus la stanga
                if tabla[i - 9] == Joc.GOL and i % 8 != 0:
                    tabla[i - 9] = Joc.JMIN.upper()
                    tabla[i] = Joc.GOL
                #mutare in sus la stanga cu capturare
                if tabla[i - 18] == Joc.GOL and i % 8 != 0 and (i - 1) % 8 != 0 and tabla[i - 9] == Joc.JMAX:
                    tabla[i - 18] = Joc.JMIN.upper()
                    tabla[i] = Joc.GOL
                    tabla[i - 9] = Joc.GOL # dispare adversarul
                    capturare = True

            else: # directia = dreapta

                #mutare in sus la dreapta
                if tabla[i - 7] == Joc.GOL and (i + 1) % 8 != 0:
                    tabla[i - 7] = Joc.JMIN.upper()
                    tabla[i] = Joc.GOL
                    
                #mutare in sus la dreapta cu capturare
                if tabla[i - 14] == Joc.GOL and (i + 1) % 8 != 0 and (i + 2) % 8 != 0 and tabla[i - 7] == Joc.JMAX:
                    tabla[i - 14] = Joc.JMIN.upper()
                    tabla[i] = Joc.GOL
                    tabla[i - 7] = Joc.GOL # dispare adversarul
                    capturare = True

    else: # piesa este rege sigur (si se deplaseaza in jos) 

        if directia == 's': # directia = stanga

            #mutare in jos la stanga
            if tabla[i + 7] == Joc.GOL and i % 8 != 0:
                tabla[i + 7] = Joc.JMIN.upper()
                tabla[i] = Joc.GOL
            #mutare in jos la stanga cu capturare
            if tabla[i + 14] == Joc.GOL and i % 8 != 0 and (i - 1) % 8 != 0 and tabla[i + 7] == Joc.JMAX:
                tabla[i + 14] = Joc.JMIN.upper()
                tabla[i] = Joc.GOL
                tabla[i + 7] = Joc.GOL # dispare adversarul
                capturare = True

        else: # directia = dreapta

            #mutare in jos la dreapta
            if tabla[i + 9] == Joc.GOL and (i + 1) % 8 != 0:
                tabla[i + 9] = Joc.JMIN.upper()
                tabla[i] = Joc.GOL
                
            #mutare in jos la dreapta cu capturare
            if tabla[i + 18] == Joc.GOL and (i + 1) % 8 != 0 and (i + 2) % 8 != 0 and tabla[i + 9] == Joc.JMAX:
                tabla[i + 18] = Joc.JMIN.upper()
                tabla[i] = Joc.GOL
                tabla[i + 9] = Joc.GOL # dispare adversarul
                capturare = True

    return tabla, capturare

def transformare(tabla, jucator): # transforma piesele ajunse la capat in regi
    if jucator == Joc.JMIN:
        for i in range(8):
            if tabla[i] == jucator:
                tabla[i] = tabla[i].upper()

    if jucator == Joc.JMAX:
        for i in range(56, 64):
            if tabla[i] == jucator:
                tabla[i] = tabla[i].upper()
    return tabla

def main():
    
    raspuns_valid=False
    while not raspuns_valid:
        tip_algoritm=input("Algorimul folosit? (Alegeti: 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1','2']:
            raspuns_valid=True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        diff = input("Dificultate (usor / mediu / greu) (Alegeti: u / m / g): ")
        if diff in ['u', 'm', 'g']:
            if diff == 'u':
                Stare.ADANCIME_MAX = 1
                adancime = 1
            elif diff == 'm':
                Stare.ADANCIME_MAX = 3
                adancime = 3
            elif diff == 'm':
                Stare.ADANCIME_MAX = 5
                adancime = 5
            raspuns_valid = True
        else:
            print("Error.")


    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        print("***NEGRU INCEPE MEREU***")
        Joc.JMIN = str(input("Doriti sa jucati cu alb sau cu negru? (Alegeti: 'a' sau 'n'): "))
        if (Joc.JMIN in ['a', 'n']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie 'a' sau 'n'.")
    Joc.JMAX = 'n' if Joc.JMIN == 'a' else 'a'


    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    #creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'n', Stare.ADANCIME_MAX)

    linie = -1
    coloana = -1
    while True :
        # print(stare_curenta.tabla_joc.nrMutariJucatorMAX(), stare_curenta.tabla_joc.nrMutariJucatorMIN(), Joc.JMAX, Joc.JMAX.upper())
        if (stare_curenta.j_curent == Joc.JMIN):
            #muta jucatorul
            raspuns_valid=False
            while not raspuns_valid:
                try:
                    linie = int(input("Linia = "))
                    coloana = str(input("Coloana = "))
                    coloana = ord(coloana) - 97
                    directia = str(input("Directia (stanga / dreapta) introduceti: s / d = "))
                    SusJos = str(input("Directia (sus / jos) introduceti: s / j = "))

                    if 0 <= linie and linie < Joc.NR_LINII:
                        if 0 <= linie and linie < Joc.NR_COLOANE:

                            ind = linie * 8 + coloana

                            if stare_curenta.tabla_joc.matr[ind] not in [stare_curenta.j_curent, stare_curenta.j_curent.upper()]: # daca e in ['n', 'N']
                                print("Nu ati ales o piesa corespunzatoare. (", stare_curenta.tabla_joc.matr[ind], ")")
                               
                            else:
                                if miscareValida(stare_curenta.tabla_joc.matr, Joc.JMIN, ind, directia, SusJos) == False:
                                    print("Nu ati ales o miscare valida!")
                                else:# miscarea jucatorului (sigur e valida)
                                    capturare = False
                                    stare_curenta.tabla_joc.matr, capturare = playerMove(stare_curenta.tabla_joc.matr, Joc.JMIN, ind, directia, SusJos, capturare)

                                    # daca o piesa a ajuns la final, o transformam in rege
                                    stare_curenta.tabla_joc.matr = transformare(stare_curenta.tabla_joc.matr, Joc.JMIN)

                                    if capturare == False:
                                        raspuns_valid = True
                                    else: # daca a capturat, va mai muta o data
                                        print("\nTabla dupa mutarea jucatorului")
                                        print(str(stare_curenta))

                                
                        else:
                            print("Coloana invalida (trebuie sa fie o litera intre a si h))")
                    else:
                        print("Linie invalida (trebuie sa fie un numar intre 0 si {}).".format(Joc.NR_COLOANE - 1))

                except ValueError:
                    print("Coloana trebuie sa fie un numar intreg.")

            #afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            #testez daca jocul a ajuns intr-o stare finala
            #si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break

            #S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

        # --------------------------------
        else: #jucatorul e JMAX (calculatorul)
        #Mutare calculator
            nr1 = stare_curenta.tabla_joc.nrPiese(Joc.JMIN)

            #preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))

            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else: #tip_algoritm==2
                stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)

            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc

            # daca o piesa a ajuns la final, o transformam in rege
            stare_curenta.tabla_joc.matr = transformare(stare_curenta.tabla_joc.matr, Joc.JMAX)


            nr2 = stare_curenta.tabla_joc.nrPiese(Joc.JMIN)

            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            #preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de "+str(t_dupa - t_inainte)+" milisecunde.")

            if (afis_daca_final(stare_curenta)):
                break

            #S-a realizat o mutare. Schimb jucatorul cu cel opus
            # print(nr1, nr2)
            if nr1 == nr2: # daca a capturat, va mai muta o data
                stare_curenta.j_curent = stare_curenta.jucator_opus()

if __name__ == "__main__" :
        main()