#Problema misionarilor si canibalilor Voica Mihai Cristian 231 lab5 pb2

class Node():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None

	#daca nu mai sunt nici canibali, nici misionari in stanga, se termina problema
	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	#verificare daca la un moment dat sunt mai multi misionari decat canibali pe orice mal
	#si sa nu existe numere negative
	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		return False

	#functia euristica este reprezentata de numarul total de persoane de pe malul stang
	def heuristic(self):
		return self.cannibalLeft + self.missionaryLeft
	
	def __repr__(self):
		return f'{self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight}'

def expand(cur_state):
	children = []
	if cur_state.boat == 'left':

		## 2 misionari iau barca spre malul drept.
		new_state = Node(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 2 canibali iau barca spre malul drept.
		new_state = Node(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 1 misionar si un canibal iau barca spre malul drept.
		new_state = Node(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 1 misionar ia barca spre malul drept.
		new_state = Node(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 1 canibal ia barca spre malul drept.
		new_state = Node(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:

		## 2 misionari iau barca spre malul stang.
		new_state = Node(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 2 canibali iau barca spre malul stang.
		new_state = Node(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 1 misionar si un canibal iau barca spre malul stang.
		new_state = Node(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 1 misionar ia barca spre malul stang.
		new_state = Node(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

		## 1 canibal ia barca spre malul stang.
		new_state = Node(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)

	return children

def problem():
	
	initial_state = Node(3, 3, 'left', 0, 0)

	#verificam daca state-ul initial este si final
	if initial_state.is_goal():
		return initial_state
	
	#initializam listele open si close
	open = [initial_state]
	closed = []

	while open:
		state = open.pop(0)

		#cand am gasit state-ul final, returnam nodul respectiv
		if state.is_goal():
			return state
		closed.append(state)

		#luam toti copiii valizi al state-ului curent si ii adaugam in open
		children = expand(state)
		for child in children:
			if (child not in closed) or (child not in open):
				open.append(child)

		#sortam lista open astfel incat elementul cu cea mai buna euristica sa fie primul
		open.sort(key=lambda a: a.heuristic())

	return None

def print_solution(solution):
	
	#afisam solutia cu ajutorul atributului 'parent'
	path = []
	path.append(solution)
	parent = solution.parent
	while parent:
		path.append(parent)
		parent = parent.parent

	for i in range(len(path) - 1, -1, -1):
		print(path[i])

def main():
	solution = problem()

	print ("(Canibali Stanga, Misionari Stanga, Barca se afla in, Canibali Dreapta, Misionari Dreapta)")
	print_solution(solution)

if __name__ == "__main__":
    main()