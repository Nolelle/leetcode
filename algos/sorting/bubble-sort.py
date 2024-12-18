# Explanation
# Bubble Sort repeatedly steps through the list,
# compares adjacent elements and swaps them if they're in the wrong order.
# The pass through the list is repeated until no swaps are needed, which means the list is sorted.

# Time Complexity
# Worst case: O(n^2)
# Average case: O(n^2)
# Best case: O(n) (when the array is already sorted)

# Space Complexity
# O(1) - It's an in-place sorting algorithm.


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
