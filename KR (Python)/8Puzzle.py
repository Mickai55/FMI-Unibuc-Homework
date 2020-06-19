#Problema 8puzzle Voica Mihai Cristian 231 lab5 pb1

class Node:
    def __init__(self, data, gval, fval):
        """ Initializeaza cu numerele din matrice, g-ul, si f-ul """
        self.data = data
        self.gval = gval
        self.fval = fval

    def generate_child(self):
        """ Generam copiii mutand spatiul in cele 4 pozitii: sus, jos, stanga, dreapta """
        x, y = self.find(self.data, '_')
        
        pos_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in pos_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child,self.gval + 1, 0)
                children.append(child_node)
        return children
            
    def shuffle(self, puz, x1, y1, x2, y2):
        """ Verificam daca pozitia indicata este valida, si mutam spatiul in directia respectiva, in caz afirmativ """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        """ Copiaza matricea in temp """
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
                
    def find(self, puz, x):
        """ Gaseste spatiul ('_') """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j

class Problem:

    def __init__(self,size):
        """ Initializam dimensiunea puzzle-ului, si listele open si close """
        self.n = size
        self.open = []
        self.closed = []
        
    def f(self, start, goal):
        """ Functia heuristica f(x) = h(x) + g(x) """
        return self.h(start.data, goal) + start.gval

    def h(self, start, goal):
        """ Calculeaza cate pozitii sunt diferite din cele 2 matrici date """
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def solvable (self, mat):
        """ Verifica daca puzzle-ul se poate rezolva (nr inversiuni % 2)"""
        arr = []
        nr = 0

        for i in mat:
            for j in i:
                arr.append(j)
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] != '_' and arr[j] != '_' and arr[i] > arr[j]:
                    nr += 1

        return False if nr % 2 else True

    def process(self):
        """ Configuratiile: initiala si finala"""

        start = [[2, 4, 3],
                [8, 7, 5],
                [1, '_', 6]]

                
        goal = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, '_']]

        if self.solvable(start) == False or self.solvable(goal) == False:
            print("Not solvable")
            return
        else:
            print("Solvable")
                
        start = Node(start, 0, 0)
        start.fval = self.f(start,goal)
        
        self.open.append(start)
        print("\n")

        # print(self.h(start.data, goal))

        k = 0

        while True:
            
            cur = self.open.pop(0)
            print("")
            print("  | ")
            print("  | ")
            print(" \\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")

            if(self.h(cur.data, goal) == 0): #Am ajuns la configuratia finala
                break

            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            self.open.sort(key = lambda x : x.fval)

def main():
    puz = Problem(3)
    puz.process()

if __name__ == "__main__":
    main()