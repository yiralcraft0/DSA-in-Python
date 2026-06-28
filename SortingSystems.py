import time

start_time = time.perf_counter()

array = [9, 8, 7, 4, 5, 0, 6, 1, 2, 3,]

# Exchange sort-----------------------


def ExchangeSort(array):
    for i in range(len(array)-1):
        for j in range(i + 1, len(array)):
            if (array[i] > array[j]):
                array[i], array[j] = array[j], array[i]
# ExchangeSort(array)

# Bubble sort---------------------------------------------------------------
# 1️⃣ Bubble Sort 🫧

    # 💡 Idea
        # pairs of adjacent elements are compared, and the elements swapped if they are not in order.
        # Keep comparing neighbors and swap if they are in wrong order.
        # Big number slowly goes to the end (like bubbles rising).

    # 🧠 Think like:
        # “Keep fixing adjacent pairs again and again.”

    # ⚙️ How it works
        # Compare 0 & 1 → swap if needed
        # Compare 1 & 2 → swap if needed
        # Repeat whole list multiple times

    # ⏱️ Complexity
        # Best: O(n) (if already sorted + optimized version)
        # Worst: O(n²)
        # Space: O(1)


def BubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
# BubbleSort(array)

# selection sort----------------------------------------------------------------
# 2️⃣ Selection Sort 🎯
    # 💡 Idea
        # Find the smallest number and put it at the front.

    # 🧠 Think like:
        # “Pick minimum and place it in correct position.”

    # ⚙️ How it works
        # Scan whole array
        # Find smallest value
        # Swap with first unsorted position
        # Repeat

    # ⏱️ Complexity
        # Best / Worst (Time): O(n²)
        # Space: O(1)

    # ⚠️ Important
        # Fewer swaps
        # But still slow because it scans again and again


def SelectionSort(array):
    for i in range(len(array) - 1):
        minIndex = i
        for j in range(i + 1, len(array)):
            if (array[minIndex] > array[j]):
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]

# SelectionSort(array)

# Insertion Sort--------------------------------------------------------------
# 3️⃣ Insertion Sort 🃏
    # 💡 Idea
        # Build sorted part slowly (like arranging playing cards in hand)

    # 🧠 Think like:
        # “Take one element and insert it into correct place on left side.”

    # ⚙️ How it works
        # Take element
        # Compare with left side
        # Shift bigger elements right
        # Insert it in correct position

    # ⏱️ Complexity
        # Best: O(n) (already sorted)
        # Worst: O(n²)
        # Space: O(1)

    # ⭐ Best for
        # Small arrays
        # Almost sorted data


def InsertionSort(array):
    for i in range(1, len(array)):
        tempValue = array[i]
        j = i - 1
        while (j >= 0 and tempValue < array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = tempValue

# InsertionSort(array)

# Merge Sort-------------------------------------------------------------------
# 4️⃣ Merge Sort 🧩
    # 💡 Idea
        # Break array into halves → sort → merge back

    # 🧠 Think like:
        # “Break problem into small pieces, solve, then combine.”

    # ⚙️ How it works
        # Split array into 2 parts
        # Keep splitting until single elements
        # Merge sorted parts step by step

    # ⏱️ Complexity
        # Best / Worst: O(n log n)
        # space: O(n)

    # ⚠️ Important
        # Very stable and reliable
        # Uses extra memory


def MergeSort(anArray):
    arrLen = len(anArray)
    if (arrLen <= 1):
        return
    middle = arrLen//2
    leftArray = []
    rightArray = []

    for i in range(len(anArray)):
        if (i < middle):
            leftArray.append(anArray[i])
        else:
            rightArray.append(anArray[i])

    MergeSort(leftArray)
    MergeSort(rightArray)
    merge(leftArray, rightArray, anArray)


def merge(leftArray, rightArray, anArray):
    leftSize = len(leftArray)
    rightSize = len(rightArray)

    i = 0
    l = 0
    r = 0

    while (l < leftSize and r < rightSize):
        if (leftArray[l] < rightArray[r]):
            anArray[i] = leftArray[l]
            i += 1
            l += 1
        else:
            anArray[i] = rightArray[r]
            i += 1
            r += 1

    while (l < leftSize):
        anArray[i] = leftArray[l]
        i += 1
        l += 1

    while (r < rightSize):
        anArray[i] - rightArray[r]
        i += 1
        r += 1

# MergeSort(array)


# Quick Sort---------------------------------------------------------------------------
# 5️⃣ Quick Sort ⚡
    # 💡 Idea
        # Pick a pivot → put smaller value left, bigger right → repeat

    # 🧠 Think like:
        # “Middle point divides everything into small and big.”

    # ⚙️ How it works
        # Choose pivot (last element)
        # Move smaller value to left
        # Bigger to right
        # Repeat for both sides
    # ⏱️ Complexity
        # Best / Average: O(n log n)
        # Worst: O(n²) (bad pivot)
        # Space: O(log n)
    # ⚠️ Important
        # Very fast in real life
        # But pivot choice matters

def QuickSort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, startIndex, endIndex):
    if startIndex >= endIndex:
        return

    pivotIndex = partition(array, startIndex, endIndex)

    quick_sort_helper(array, startIndex, pivotIndex - 1)
    quick_sort_helper(array, pivotIndex + 1, endIndex)


def partition(array, startIndex, endIndex):
    pivot = array[endIndex]
    i = startIndex - 1

    for j in range(startIndex, endIndex):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1
    array[i], array[endIndex] = array[endIndex], array[i]

    return i

# QuickSort(array)

end_time = time.perf_counter()

if (__name__ == "__main__"):
    print(array)
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

