class Node:
    def __init__(this, data):
        this.data = data
        this.left = None
        this.right = None

class Tree:
    def __init__(this):
        this.root = None

    def insert(this, data):
        this.root = this.insertHelper(this.root, data)

    def insertHelper(this, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = this.insertHelper(root.left, data)
        elif data > root.data:
            root.right = this.insertHelper(root.right, data)

        return root

    def search(this, data):
        return this.searchHelper(this.root, data)

    def searchHelper(this, root, data):
        if root is None:
            return False
        
        if root.data == data:
            return True
        
        
        if data > root.data:
            return this.searchHelper(root.right, data)

        elif data < root.data:
            return this.searchHelper(root.left, data)


    def delete(this, data):
        this.root = this.deleteHelper(this.root, data)
        
    def deleteHelper(this, root, data):
            if data == None:
                return root
            
            if data == root.data:
                root = None

            if data < root.data:
                root.left = this.deleteHelper(root.left , data)
            if data > root.data:
                root.right = this.deleteHelper(root.right , data) 
            
    def treeHeight():
        ...

    def preOrder(this):
        this.preOrderHelper(this.root)
    
    def preOrderHelper(this, root):
        if root == None:
            return
        
        print(root.data , end = " ,")
        this.preOrderHelper(root.left)
        this.preOrderHelper(root.right)

    def inOrder(this):
        this.inOrderHelper(this.root)

    def inOrderHelper(this, root):
        if root == None:
            return
                
        this.inOrderHelper(root.left)
        print(root.data, end = " ,")
        this.inOrderHelper(root.right)

    def postOrder(this):
        this.postOrderHelper(this.root)

    def postOrderHelper(this, root):
        if root == None:
            return

        this.postOrderHelper( root.left)
        this.postOrderHelper( root.right)
        print( root.data , end = " ,")

    def levelOrder(this):
        ...


tree = Tree()

tree.insert(100)
tree.insert(60)
tree.insert(80)
tree.insert(50)
tree.insert(95)
tree.insert(50)
tree.insert(20)

tree.inOrder()
print(f'')
tree.delete(95)


# tree.preOrder()
# print()
# tree.postOrder()