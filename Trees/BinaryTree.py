class Node:
    def __init__(this, data):
        this.data = data
        this.left = None
        this.right = None

class Tree:
    def __init__(this):
        this.root = None

    def insert(this, data):
        ...

    def search(this, data):
        ...

    def delete(this, data):
        ...

    def treeHeight():
        ...

    def preOrder(this, node):
        if node == None:
            return
        
        print(node.data , end = "->")
        this.preOrder(node.left)
        this.preOrder(node.right)

    def inOrder(this, node):
        if node == None:
            return
        
        this.inOrder(node.left)
        print(node.data, end = "->")
        this.inOrder(node.right)

    def postOrder(this, node):
        
        if node == None:
            return

        this.postOrder(node.left)
        this.postOrder(node.right)
        print(node.data , end = "->")

    def levelOrder(this, node):
        current = node
        queue = []
        ...
        



root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)
n14 = Node(14)
n15 = Node(15)



root.left = n2
root.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n4.left = n8
n4.right = n9

n5.left = n10
n5.right = n11

n6.left = n12 
n6.right =  n13

n7.left =  n14
n7.right = n15

tree = Tree()

tree.preOrder(root)
print()
tree.inOrder(root)
print()
tree.postOrder(root)
print()
tree.levelOrder(root)


    
