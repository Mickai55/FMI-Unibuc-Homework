#Problema blocurilor Voica Mihai Cristian 231 lab4 pb1

class Cuburi:
	def __init__(self, stive):
		self.stive = stive

	def pozitii(self):
		# returneaza pozitia unei litere (stiva i, pozitia j)
		pozitii = {}
		for i, stiva in enumerate(self.stive):
			for j, cub in enumerate(stiva):
				pozitii[cub] = (i, j)
		return pozitii

	def euristica(self):
    		
		#calculeaza diferenta dintre un state si state-ul final
		global pozitii_finale
		distanta = 0

		pozitii = self.pozitii()

		for cub in cuburi:
			if pozitii[cub] != pozitii_finale[cub]:
				distanta += 1

		return distanta

	def __eq__(self, other):
		return self.stive == other.stive

	def __repr__(self):
		return f'{self.stive}'

### datele de intrare

N = 3
cuburi = ['a', 'b', 'c', 'd']

M = len(cuburi)

configuratie_initiala = Cuburi([
							['a'],
							['b', 'c'],
							['d'],
						])

configuratie_finala = Cuburi([
							['b', 'c'],
							[],
							['d', 'a'],
						])

pozitii_finale = configuratie_finala.pozitii()

""" definirea problemei """
class Nod:
	def __init__(self, configuratie):
		self.info = configuratie
		self.h = configuratie.euristica()

	def __str__ (self):
		return "({}, h = {})".format(self.info, self.h)
	def __repr__ (self):
		return f"({self.info}, h = {self.h})"


# class Arc:
# 	def __init__(self, capat, varf):
# 		self.capat = capat
# 		self.varf = varf
# 		self.cost = 1 # toate mutările au cost 1

class Problema:
	def __init__(self):
		self.noduri = [
			Nod(configuratie_initiala)
		]
		self.arce = []
		self.nod_start = self.noduri[0]
		self.nod_scop = configuratie_finala

	def cauta_nod_nume(self, info):
		"""Stiind doar informatia "info" a unui nod,
		trebuie sa returnati fie obiectul de tip Nod care are acea informatie,
		fie None, daca nu exista niciun nod cu acea informatie."""
		for nod in self.noduri:
			if nod.info == info:
				return nod
		# la capătul funcției dă return None implicit

""" Sfarsit definire problema """

""" Clase folosite in algoritmul A* """

class NodParcurgere:
	"""O clasa care cuprinde informatiile asociate unui nod din listele open/closed
		Cuprinde o referinta catre nodul in sine (din graf)
		dar are ca proprietati si valorile specifice algoritmului A* (f si g).
		Se presupune ca h este proprietate a nodului din graf
	"""

	problema = None		# atribut al clasei

	def __init__(self, nod_graf, parinte=None, g=0, f=None):
		self.nod_graf = nod_graf	# obiect de tip Nod
		self.parinte = parinte		# obiect de tip Nod
		self.g = g					# costul drumului de la radacina pana la nodul curent
		if f is None :
			self.f = self.g + self.nod_graf.h
		else:
			self.f = f

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

	# def contine_in_drum(self, nod):
	# 	"""
	# 		Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
	# 		Verificarea se face mergand din parinte in parinte pana la radacina
	# 		Se compara doar informatiile nodurilor (proprietatea info)
	# 		Returnati True sau False.
	# 		"nod" este obiect de tip Nod (are atributul "nod.info")
	# 		"self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
	# 	"""
	# 	nod_curent = self
	# 	while nod_curent:
	# 		if nod_curent.nod_graf.info == nod.info:
	# 			return True
	# 		nod_curent = nod_curent.parinte
	# 	return False

	#se modifica in functie de problema
	def expandeaza(self):
		"""Pentru nodul curent (self) parinte, trebuie sa gasiti toti succesorii (fiii)
		si sa returnati o lista de tupluri (nod_fiu, cost_muchie_tata_fiu),
		sau lista vida, daca nu exista niciunul.
		(Fiecare tuplu contine un obiect de tip Nod si un numar.)
		"""
		configuratie = self.nod_graf.info
		succesori = []
		
		for stiva_sursa in range(N):
			for stiva_destinatie in range(N):
    				
				#nu se poate muta un cub pe aceeasi stiva
				if stiva_sursa == stiva_destinatie:
					continue 
				
				#stiva este vida
				if not configuratie.stive[stiva_sursa]:
					continue 

				cub_de_mutat = configuratie.stive[stiva_sursa][-1]

				#punem cubul in stiva noua
				stive_noi = []
				for i in range(N):
					if i == stiva_sursa:
						stiva_noua = configuratie.stive[i][:-1]
					elif i == stiva_destinatie:
						stiva_noua = configuratie.stive[i] + [cub_de_mutat]
					else:
						stiva_noua = configuratie.stive[i]

					stive_noi.append(stiva_noua)

				configuratie_noua = Cuburi(stive_noi)

				#adaugam solutia daca nu a mai fost gasita
				succesor = problema.cauta_nod_nume(configuratie_noua)
				if not succesor:
					nod_nou = Nod(configuratie_noua)
					problema.noduri.append(nod_nou)
					succesor = nod_nou

				cost = 1
				succesori.append((succesor, cost))

		return succesori


	#se modifica in functie de problema
	def test_scop(self):
		return self.nod_graf.info == self.problema.nod_scop


	def __str__ (self):
		return f"({self.nod_graf}, f = {self.f}, g = {self.g})"

""" Algoritmul A* """


def str_info_noduri(l):
	"""
		o functie folosita strict in afisari - poate fi modificata in functie de problema
	"""
	sir = "["

	for x in l:
		sir += "\n" + str(x) +"  "

	sir += "]"

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


def a_star():
	rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)
	open = [rad_arbore]
	closed = []	

	while open:
		
		#initializam listele open si closed
		nod_curent = open.pop(0)
		closed.append(nod_curent)

		if nod_curent.test_scop():
			break

		for succesor, cost in nod_curent.expandeaza():
			g_nou = nod_curent.g + cost

			#cautam nodul in listele open si close
			#daca il gasim, verificam f-ul daca este mai bun decat cel curent
			#altfel, facem un nod nou cu aceste valori
			nod_open = in_lista(open, succesor) 
			nod_closed = in_lista(closed, succesor)
			if nod_open:
				if g_nou < nod_open.g:
					nod_open.g = g_nou
					nod_open.f = g_nou + nod_open.nod_graf.h
					nod_open.parinte = nod_curent

			elif nod_closed:
				f_nou = g_nou + nod_closed.nod_graf.h

				if f_nou < nod_closed.f:
					nod_closed.g = g_nou
					nod_closed.f = f_nou + nod_closed.nod_graf.h
					nod_closed.parinte = nod_curent

					open.append(nod_closed)
			else:
				nod_nou = NodParcurgere(nod_graf = succesor, parinte = nod_curent, g = g_nou)

				open.append(nod_nou)

		#lista open este sortata dupa f
		open.sort(key=lambda nod: nod.f)

	print("\n------------------ Concluzie -----------------------")

	if(len(open) == 0):
		print("Lista open e vida, nu avem drum de la nodul start la nodul scop")
	else:
		print("Drum de cost minim: " + str_info_noduri(nod_curent.drum_arbore()))


if __name__ == "__main__":
	problema = Problema()
	NodParcurgere.problema = problema
	a_star()
	