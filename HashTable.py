class HashTable:

    def __init__(this, size: int = 10):
        this.size = size
        this.hashtable = [[] for _ in range(size)]
        this.length = 0

    def hash_function(this, data: int | str) -> None:
        data = str(data)
        sum_of_chars = 0
        for char in data:
            sum_of_chars += ord(char)

        return sum_of_chars % this.size

    def add(this, data: str) -> None:
        if this.contains(data):
            return
        try:
            loadfactor = this.loadFactor()
            if loadfactor > 0.75:
                    this.rehash()
        except Exception as e:
            print(f'{e}')
            
        index = this.hash_function(data)
        this.hashtable[index].append(data)
        this.length += 1

    def rehash(this):
        oldTable = this.hashtable
        this.size *= 2

        this.hashtable = [[] for _ in range(this.size)]

        for bucket in oldTable:
            for data in bucket:
                index = this.hash_function(data)
                this.hashtable[index].append(data)



    def loadFactor(this) -> int:
            return this.length / this.size
    
    def indexOf(this, data) -> tuple:
        index = this.hash_function(data)
        for j, i in enumerate(this.hashtable[index]):
            if (i == data):
                return index, j
        return None

    def remove(this, data = None) -> int | str:
        index = this.indexOf(data)
        if (index == None):
            return f"{data} Not Found"
        outIndx, inIndx = index
        this.length -= 1
        return this.hashtable[outIndx].pop(inIndx)

    def display(this) -> None:
        for index, bucket in enumerate(this.hashtable):
            if (bucket):
                print(f'{index}-> {bucket}')

    def contains(this, data : int | str) -> bool:
        return this.indexOf(data) is not None


H1 = HashTable()
print(H1.hashtable)
H1.add("a")
H1.add("b")
H1.add("c")
H1.add("d")
H1.add("e")
H1.add("f")
H1.add("g")
H1.add("h")
H1.add("i")
H1.add("j")
H1.add("k")
H1.add("l")
H1.add("m")
H1.add("n")
H1.add("o")
H1.add("p")
H1.add("q")
H1.add("r")
H1.add("s")
H1.add("u")
H1.add("v")
H1.add("w")
H1.add("x")
H1.add("y")
H1.add("z")

H1.display()
print(H1.hashtable)
