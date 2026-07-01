class Stack:

    def __init__(this):
        this.stack = []

    def push(this, value):  # Push Values in Stack
        this.stack.append(value)

    def pop(this):
        if this.isEmpty():
            return "Stack is empty"
        return this.stack.pop()

    def peek(this):  # Return the Value which is at the top of the Stack
        return this.stack[-1]

    def isEmpty(this):  # Tells if  the Stack is empty or not
        return not bool(this.stack)

    def size(this):  # Cheak The Size of Stack
        return len(this.stack)

    def show(this):
        return this.stack


class Queues():

    def __init__(this):
        this.queues = []

    def Enqueue(this, value):
        this.queues.append(value)

    def Dequeue(this):
        return this.queues.pop(0)
    
    def peek(this):
        return this.queues[0]
    
    def isEmpty(this) -> bool:
        return not bool(this.queues)

    def size(this):
        return len(this.queues)

    def show(this):
        return this.queues



a = [1]

print(bool(a))