from math import sqrt
from copy import deepcopy
import time

class Frunza:
	def __init__(self, ID, x, y, insecte, greutateMaxima, i):
		self.ID = ID
		self.x = x
		self.y = y
		self.insecte = insecte
		self.greutateMaxima = greutateMaxima
		self.index = i
	
	def __str__ (self):
		return "Frunza: id = {}, x = {}, y = {}, insecte = {}, greutateMaxima = {}".format(self.ID, self.x, self.y, self.insecte, self.greutateMaxima)


def distanta(ax, ay, bx, by):
	return sqrt((ax - bx) ** 2 + (ay - by) ** 2)

class Nod:
	def __init__(self, frunze, undeSeAflaBroasca, greutate, insecteMancate):
		self.frunze = frunze
		self.undeSeAflaBroasca = undeSeAflaBroasca
		self.greutate = greutate
		self.info = (frunze, undeSeAflaBroasca, greutate)
		self.h = raza - distanta(self.frunze[self.undeSeAflaBroasca].x, self.frunze[self.undeSeAflaBroasca].y, 0, 0) # raza - distanta pana la centru
		# self.h = greutate
		# self.h = greutate + raza - distanta(self.frunze[self.undeSeAflaBroasca].x, self.frunze[self.undeSeAflaBroasca].y, 0, 0) # raza - distanta pana la centru
		# self.h = 0
		self.insecteMancate = insecteMancate

	def __repr__ (self):
		return f"({self.frunze[self.undeSeAflaBroasca]}, G={self.greutate}, h={self.h})"



class NodParcurgere:
	"""
		O clasa care cuprinde informatiile asociate unui nod din listele open/closed
		Cuprinde o referinta catre nodul in sine (din graf)
		dar are ca proprietati si valorile specifice algoritmului A* (f si g).
		Se presupune ca h este proprietate a nodului din graf
	"""

	def __init__(self, nod_graf, parinte = None, g = 0, f = None):
		self.nod_graf = nod_graf	# obiect de tip Nod
		self.parinte = parinte		# obiect de tip Nod
		self.g = g					# costul drumului de la radacina pana la nodul curent
		self.f = self.g + self.nod_graf.h


	def drum_arbore(self):
		"""
			Functie care calculeaza drumul asociat unui nod din arborele de cautare.
			Functia merge din parinte in parinte pana ajunge la radacina
		"""
		nod_c = self
		drum = [nod_c]
		while nod_c.parinte is not None :
			drum = [nod_c.parinte] + drum
			nod_c = nod_c.parinte
		return drum


	def contine_in_drum(self, nod):
		"""
			Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
			Verificarea se face mergand din parinte in parinte pana la radacina
			Se compara doar informatiile nodurilor (proprietatea info)
			Returnati True sau False.
			"nod" este obiect de tip Nod (are atributul "nod.info")
			"self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
		"""
		nod_curent = self
		while nod_curent:
			if nod_curent.nod_graf.info == nod.info:
				return True
			nod_curent = nod_curent.parinte
		return False

	#se modifica in functie de problema
	def expandeaza(self):
		"""Pentru nodul curent (self) parinte, trebuie sa gasiti toti succesorii (fiii)
		si sa returnati o lista de tupluri (nod_fiu, cost_muchie_tata_fiu),
		sau lista vida, daca nu exista niciunul.
		(Fiecare tuplu contine un obiect de tip Nod si un numar.)
		"""
		frunzaActuala = self.nod_graf.frunze[self.nod_graf.undeSeAflaBroasca] # frunza pe care se afla broasca
		l_succesori = []
		
		# for i in self.nod_graf.frunze:
		# 	print(i)

		for FRUNZA in self.nod_graf.frunze: # luam toate frunzele
			if FRUNZA.ID != frunzaActuala.ID: # nu poate sari pe aceeasi frunza
				for aMancat in range(0, frunzaActuala.insecte + 1):
					nouaGreutate = self.nod_graf.greutate + aMancat

					distantaParcursa = distanta(frunzaActuala.x, frunzaActuala.y, FRUNZA.x, FRUNZA.y)

					if distantaParcursa <= nouaGreutate / 3 and nouaGreutate - 1 < FRUNZA.greutateMaxima:
    						
						vectFrunze = deepcopy(self.nod_graf.frunze)
						vectFrunze[self.nod_graf.undeSeAflaBroasca] = Frunza(frunzaActuala.ID, frunzaActuala.x, frunzaActuala.y, frunzaActuala.insecte - aMancat, frunzaActuala.greutateMaxima, frunzaActuala.index)
						nod_nou = Nod(vectFrunze, FRUNZA.index, nouaGreutate - 1, aMancat)

						l_succesori.append((nod_nou, distantaParcursa))

		return l_succesori


	def test_scop(self):
		poz = self.nod_graf.frunze[self.nod_graf.undeSeAflaBroasca] # luam pozitia curenta a broastei

		if poz.greutateMaxima >= self.nod_graf.greutate + poz.insecte: # daca broasca poate sari la mal din pozitia curenta s-a indeplinit scopul
			return raza - distanta(poz.x, poz.y, 0, 0) <= (self.nod_graf.greutate + poz.insecte) / 3
		
		return False


	def __str__ (self):
		parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
		return f"({self.nod_graf}, f={self.f}, g={self.g})"


""" Algoritmul A* """


def str_info_noduri(l):
	"""
		o functie folosita strict in afisari - poate fi modificata in functie de problema
	"""
	sir="["
	for x in l:
		sir+=str(x)+"  "
	sir+="]"
	return sir


def afis_succesori_cost(l):
	"""
		o functie folosita strict in afisari - poate fi modificata in functie de problema
	"""
	sir=""
	for (x, cost) in l:
		sir+="\nnod: "+str(x)+", cost arc:"+ str(cost)

	return sir


def in_lista(l, nod):
	"""
	lista "l" contine obiecte de tip NodParcurgere
	"nod" este de tip Nod
	"""
	for i in range(len(l)):
		if l[i].nod_graf.info == nod.info:
			return l[i]
	return None


def a_star(index):
	"""
		Functia care implementeaza algoritmul A-star
	"""
	ok = False


	output = open(f"E:/Informatica/output{index}.txt", "w")

	nod_start = Nod(frunzeInit, primaFrunza.index, greutateInitiala, 0)
	rad_arbore = NodParcurgere(nod_start)

	fr = nod_start.frunze[nod_start.undeSeAflaBroasca]
	print(f"Broscuta se afla pe frunza initiala, {fr.ID}({fr.x}, {fr.y}), Greutate Broscuta: {greutateInitiala}.")
	output.write(f"Broscuta se afla pe frunza initiala, {fr.ID}({fr.x}, {fr.y}), Greutate Broscuta: {greutateInitiala}.\n")

	listaOpen = [rad_arbore]  # open va contine elemente de tip NodParcurgere
	closed = []  # closed va contine elemente de tip NodParcurgere

	while len(listaOpen) > 0 :
    		
		nod_curent = listaOpen.pop(0)	# scoatem primul element din lista open
		closed.append(nod_curent)	# si il adaugam la finalul listei closed

		print(nod_curent)

		#testez daca nodul extras din lista open este nod scop (si daca da, ies din bucla while)
		if nod_curent.test_scop():
			ok = True
			break

		l_succesori = nod_curent.expandeaza()	# contine tupluri de tip (Nod, numar)
		for (nod_succesor, cost_succesor) in l_succesori:
			# "nod_curent" este tatal, "nod_succesor" este fiul curent

			# daca fiul nu e in drumul dintre radacina si tatal sau (adica nu se creeaza un circuit)
			if (not nod_curent.contine_in_drum(nod_succesor)):

				# calculez valorile g si f pentru "nod_succesor" (fiul)
				g_succesor = nod_curent.g + cost_succesor # g-ul tatalui + cost muchie(tata, fiu)
				f_succesor = g_succesor + nod_succesor.h # g-ul fiului + h-ul fiului

				#verific daca "nod_succesor" se afla in closed
				# (si il si sterg, returnand nodul sters in nod_parcg_vechi
				nod_parcg_vechi = in_lista(closed, nod_succesor)

				if nod_parcg_vechi is not None:	# "nod_succesor" e in closed
					# daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
					# 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista closed)
					# atunci actualizez parintele, g si f
					# si apoi voi adauga "nod_nou" in lista open
					if (f_succesor < nod_parcg_vechi.f):
						closed.remove(nod_parcg_vechi)	# scot nodul din lista closed
						nod_parcg_vechi.parinte = nod_curent # actualizez parintele
						nod_parcg_vechi.g = g_succesor	# actualizez g
						nod_parcg_vechi.f = f_succesor	# actualizez f
						nod_nou = nod_parcg_vechi	# setez "nod_nou", care va fi adaugat apoi in open

				else :
					# daca nu e in closed, verific daca "nod_succesor" se afla in open
					nod_parcg_vechi = in_lista(listaOpen, nod_succesor)

					if nod_parcg_vechi is not None:	# "nod_succesor" e in open
						# daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
						# 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista open)
						# atunci scot nodul din lista open
						# 		(pentru ca modificarea valorilor f si g imi va strica sortarea listei open)
						# actualizez parintele, g si f
						# si apoi voi adauga "nod_nou" in lista open (la noua pozitie corecta in sortare)
						if (f_succesor < nod_parcg_vechi.f):
							listaOpen.remove(nod_parcg_vechi)
							nod_parcg_vechi.parinte = nod_curent
							nod_parcg_vechi.g = g_succesor
							nod_parcg_vechi.f = f_succesor
							nod_nou = nod_parcg_vechi

					else: # cand "nod_succesor" nu e nici in closed, nici in open
						nod_nou = NodParcurgere(nod_graf = nod_succesor, parinte = nod_curent, g = g_succesor)
						# se calculeaza f automat in constructor

				if nod_nou:
					# inserare in lista sortata crescator dupa f
					# (si pentru f-uri egale descrescator dupa g)
					i=0
					while i < len(listaOpen):
						if listaOpen[i].f < nod_nou.f:
							i += 1
						else:
							while i < len(listaOpen) and listaOpen[i].f == nod_nou.f and listaOpen[i].g > nod_nou.g:
								i += 1
							break

					listaOpen.insert(i, nod_nou)

	if(len(listaOpen) == 0):
		if ok: # daca poate sari din prima
			print("Broscuta a sarit direct la mal!")
			output.write("Broscuta a sarit direct la mal!\n")
		else:
			print("Broscuta s-a innecat!!")
			output.write("Broscuta s-a innecat!!\n")
	else:
		
		drum = nod_curent.drum_arbore()
		for i in range(len(drum) - 1):
			fr1 = drum[i].nod_graf.frunze[drum[i].nod_graf.undeSeAflaBroasca]  
			fr2 = drum[i + 1].nod_graf.frunze[drum[i + 1].nod_graf.undeSeAflaBroasca]

			# if i != len(drum) - 2:
			# 	catAMancat = drum[i + 2].nod_graf.greutate - drum[i + 1].nod_graf.greutate + 1

			print(f"Broscuta a sarit de la {fr1.ID}({fr1.x, fr1.y}) la {fr2.ID}({fr2.x, fr2.y}).", end = "")
			output.write(f"Broscuta a sarit de la {fr1.ID}({fr1.x, fr1.y}) la {fr2.ID}({fr2.x, fr2.y}).")
			# print(f" A mancat {catAMancat} insecte. Greutate broscuta: {drum[i + 1].nod_graf.greutate + catAMancat}.")
			if i != len(drum) - 2:
				print(f" A mancat {drum[i + 2].nod_graf.insecteMancate}. Greutate broscuta: {drum[i + 1].nod_graf.greutate + drum[i + 2].nod_graf.insecteMancate}.")
				output.write(f" A mancat {drum[i + 2].nod_graf.insecteMancate}. Greutate broscuta: {drum[i + 1].nod_graf.greutate + drum[i + 2].nod_graf.insecteMancate}.\n")
			else:
				print(f" A mancat {fr2.insecte}. Greutate broscuta: {drum[i + 1].nod_graf.greutate + fr2.insecte}.")
				output.write(f" A mancat {fr2.insecte}. Greutate broscuta: {drum[i + 1].nod_graf.greutate + fr2.insecte}.\n")

		print(f"Broscuta a ajuns la mal in {len(drum)} sarituri.")
		output.write(f"Broscuta a ajuns la mal in {len(drum)} sarituri.\n")

if __name__ == "__main__":
    	
	index = 0
	
	# for i in ['E:/Informatica/broscuta exemplul0.txt', 'E:/Informatica/broscuta exemplul1.txt', 'E:/Informatica/broscuta exemplul2.txt', 'E:/Informatica/broscuta exemplul3.txt']:
	for i in ['E:/Informatica/broscuta exemplul0.txt']:
   		
		print(f"\nFisierul: '{i}' -------------------------------------------------------------------------------------------------------------------\n")

		file = open(i)


		raza = int(file.readline())
		greutateInitiala = int(file.readline())
		frunzeInit = []

		idPrimaFrunza = str(file.readline().strip())
		i = 0

		for x in file.readlines():
			x = x.split()
			frunzeInit.append(Frunza(str(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), i))
			i += 1

		primaFrunza = next(x for x in frunzeInit if x.ID == idPrimaFrunza.strip())


		t_inainte = int(round(time.time() * 1000))
		a_star(index)
		t_dupa = int(round(time.time() * 1000))

		print("Calculatorul a \"gandit\" timp de "+str(t_dupa - t_inainte)+" milisecunde.\n")

		index += 1