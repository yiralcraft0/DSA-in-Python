from collections import deque

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

    def minValue(this):

        if this.root == None: return 0

        current = this.root
        while current.left is not None:
            current = current.left
        return current.data

    def maxValue(this):

        if this.root == None: return 0

        current = this.root
        while current.right is not None:
            current = current.right
        return current.data

    def delete(this, data):
        return this.deleteHelper(this.root, data)

    def deleteHelper(this, root, data):
        ...

    def treeHeight():
        ...

    def preOrder(this):
        this.preOrderHelper(this.root)

    def preOrderHelper(this, root):
        if root == None:
            return

        print(root.data, end=", ")
        this.preOrderHelper(root.left)
        this.preOrderHelper(root.right)

    def inOrder(this):
        this.inOrderHelper(this.root)

    def inOrderHelper(this, root):
        if root == None:
            return

        this.inOrderHelper(root.left)
        print(root.data, end=", ")
        this.inOrderHelper(root.right)

    def postOrder(this):
        this.postOrderHelper(this.root)

    def postOrderHelper(this, root):
        if root == None:
            return

        this.postOrderHelper(root.left)
        this.postOrderHelper(root.right)
        print(root.data, end=", ")


    def levelOrder(this):
        # Guard clause for an empty tree
        if this.root is None:
            return

        # Use deque for efficient O(1) queue operations
        queue = deque()
        
        # Enqueue the actual node object, not just the data
        queue.append(this.root)
        queue.append(-1) # Marker for the end of the first level

        while queue:
            currentNode = queue.popleft() # Dequeue

            if currentNode == -1:
                print() # Print a newline when a level ends
                if len(queue) == 0:
                    break
                else:
                    queue.append(-1) # Push marker for the next level
            else:
                # Print the data on the same line, separated by a space
                print(currentNode.data, end=" ")
                
                # Check the popped node's children and enqueue the node objects
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)
                


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

# tree.delete(20)

tree.inOrder()
print(f'')
# print(f'{tree.minValue()}')
# print(f'{tree.maxValue()}')
tree.levelOrder()

# tree.preOrder()
# print()
# tree.postOrder()
