class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
 
    def preorder(self):
        print(self.key, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
 
 
def construct_btree(postord, inord):
    if postord == [] or inord == []:
        return None
    key = postord[-1]
    node = BinaryTree(key)
    index = inord_dict[key]

    #print(index, " ")
    node.left = construct_btree(postord[:index], inord[:index])
    node.right = construct_btree(postord[index:-1], inord[index + 1:])
    return node
 
 
postord = [4, 1, 2, 3]
inord = [1, 4, 3, 2]
inord_dict = {inord[i]:i for i in range(len(inord))}
# postord = [4, 2, 1, 3]
# inord = [1, 4, 3, 2]

btree = construct_btree(postord, inord)

print('Pre-order traversal: ', end='')
btree.preorder()
print()