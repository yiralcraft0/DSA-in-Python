class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(this):
        this.node = None

    def showLink(this) -> list:
        current = this.node
        while current:
            print(f"[{current.data}]", end="->")
            current = current.next
        print("null")

    def minValue(this) -> int:
        current = this.node
        currentMin = current.data
        while current:
            if current.data < currentMin:
                currentMin = current.data
            current = current.next
        return currentMin

    def maxValue(this) -> int:
        current = this.node
        currentMax = current.data
        while current:
            if current.data > currentMax:
                currentMax = current.data
            current = current.next
        return (currentMax)

    def append(this, data) -> None:
        new_node = Node(data)
        current = this.node

        if this.node is None:
            this.node = new_node
            return

        while current.next:
            current = current.next
        current.next = new_node

    def prepend(this, data) -> None:
        new_node = Node(data)
        new_node.next = this.node
        this.node = new_node

    def length(this) -> int:
        i = 0
        current = this.node
        while current:
            i += 1
            current = current.next
        return i

    def insert(this, data, index: int) -> None:
        new_Node = Node(data)
        try:
            if (index == 0):
                this.prepend(data)
                return

            if (this.node == None):
                print("List is empty")
                return

            if (index > this.length() - 1 or index < 0):
                print("Invalid Index")
                return
        except:
            print("At index, int required")

        try:
            current = this.node
            i = 0
            while current:
                if ((index - 1) == i):
                    prevNode = current
                    break
                i += 1
                current = current.next

            new_Node.next = prevNode.next
            prevNode.next = new_Node
        except Exception as e:
            print(e)

    def removeAt(this, index: int) -> None:
        current = this.node

        try:
            if (index > this.length() - 1 or index < 0):
                print(f'Invalid Index')
                return

            if (index == 0):
                data = this.node.data
                this.node = this.node.next
                return data

            i = 0
            prevNode = current
            while current:
                if (index == i):
                    data = current.data
                    prevNode.next = current.next
                    return data
                i += 1
                prevNode = current
                current = current.next
        except Exception as e:
            print(e)

    def get(this, index: int) -> str:
        if (index > this.length() or index < 0):
            return ("Invalid Index")

        i = 0
        current = this.node
        while current:
            if (index == i):
                return current.data
            i += 1
            current = current.next

    def search(this, data):
        current = this.node

        i = 0
        while current:
            if (data == current.data):
                return i
            i += 1
            current = current.next
        return "not found"

    def __str__(this) -> str:
        if this.node == None:
            return f"[]"

        current = this.node
        result = "["
        while current:
            result += str(current.data) + ", "
            current = current.next
        result = result[:-2]
        result += "]"
        return result


if (__name__ == "__main__"):

    # Create a ListedList Object
    linked_list = LinkedList()

    print(f'{linked_list}')

    # Insert a new node at the end of the linked list.
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)

    # Will add node at front of the list
    linked_list.prepend(5)
    linked_list.prepend(0)

    # Will return minimum value in the LinkedLists
    print(f"Min value is: {linked_list.minValue()}")

    # Will return maximum value in the LinkedLists
    print(f"Max value is: {linked_list.maxValue()}")

    # Will add node at given index
    linked_list.insert(data=15, index=3)
    linked_list.insert(25, 5)
    linked_list.insert(35, 7)

    # Reture length/num of nodes
    print(f"The length is {linked_list.length()} nodes")

    # delete node from start also return the data of the node
    print(f"removed: {linked_list.removeAt(index = 0)}")

    # delete node from end
    linked_list.removeAt(linked_list.length()-1)

    # delete node from given index
    linked_list.removeAt(index=2)

    # Uses __str__() to print the list like a Python list.
    print(linked_list)

    # Reture the data of the given index
    print(f'At first index: {linked_list.get(index = 0)}')

    # Return index of the first occured value
    print(linked_list.search(data=20))
    print(linked_list.search(data=60))

    # Print the linked list in link format.Example: [10] -> [20] -> [30] -> null
    linked_list.showLink()

    # Uses __str__() to print the list like a Python list.
    print(linked_list)


#     node_1         node_2         node_3       node_n
# [data/next]->[data1/next2]->[data2/next3]->... soo on and soo for
