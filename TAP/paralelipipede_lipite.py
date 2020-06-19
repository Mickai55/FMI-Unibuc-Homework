
def create_dex(s):
	dex = {}
	for el in s:
		aux = sorted(el)
		if (aux[0], aux[1]) not in dex:
			dex[(aux[0], aux[1])] = [aux[2]]
		else:
			dex[(aux[0], aux[1])].append(aux[2])

		if (aux[0], aux[2]) not in dex:
			dex[(aux[0], aux[2])] = [aux[1]]
		else:
			dex[(aux[0], aux[2])].append(aux[1])
		
		if (aux[1], aux[2]) not in dex:
			dex[(aux[1], aux[2])] = [aux[0]]
		else:
			dex[(aux[1], aux[2])].append(aux[0])
	
	return dex

def create_set(dex):
	new_list = set()
	l = []
	for ((key1, key2), value) in dex.items():
		l = list(value)
		if len(l) == 1:
			maxim = l[0]
		else:
			first_max = max(l)
			l.remove(first_max)
			second_max = max(l)
			maxim = first_max + second_max
		new_list.add(tuple(sorted((key1, key2, maxim))))
	return new_list

def get_min_tuple(s):
	min_max = s.pop()[0]
	while s:
		aux = s.pop()   
		if min_max < aux[0]:
			min_max = aux[0]
	print(min_max)

s = [(22, 2, 31), (8, 50, 60), (7, 50, 60), (50, 10, 60), (22, 19, 31)]
print(create_dex(s))
print(create_set(create_dex(s)))
get_min_tuple(create_set(create_dex(s)))
