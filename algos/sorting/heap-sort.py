# Explanation
# Heap Sort is a comparison-based sorting technique based on Binary Heap data structure. It involves building a Heap data structure from the given array and then sorting the array.

# Time Complexity

# Worst case: O(n log n)
# Average case: O(n log n)
# Best case: O(n log n)

# Space Complexity
# O(1) - It's an in-place sorting algorithm.


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


test = [64, 25, 12, 22, 11]

print(heap_sort(test))
