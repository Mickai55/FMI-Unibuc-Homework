class Tree:
    index = 0
    ok = True
    preorder = []

    def __init__(self, length):
        self.index = length-1

    def div_conq(self, inorder_dict, postorder, left, right):
        if left > right:
            return

        if self.index < 0:
            self.ok = False
            return

        k = postorder[self.index]
        new_index = inorder_dict[k]
        self.index -= 1
        self.div_conq(inorder_dict, postorder, new_index+1, right)     
        self.div_conq(inorder_dict, postorder, left, new_index-1)
        self.preorder.append(k)
    
    def display(self):
        if self.ok:
            print(list(reversed(self.preorder)))
        else: 
            print('nu')


postorder = [4, 1, 2, 3]
inorder = [1, 4, 3, 2]
n = len(inorder)
inorder_dict = {inorder[i]:i for i in range(n)}

x = Tree(n)
x.div_conq(inorder_dict, postorder, 0, n-1)
x.display()
