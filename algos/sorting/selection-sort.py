# Explanation
# Selection Sort divides the input list into two parts:
# a sorted portion at the left end and an unsorted portion at the right end.
# It repeatedly selects the smallest (or largest) element from the unsorted portion
# and moves it to the sorted portion.

# Time Complexity
# Worst case: O(n^2)
# Average case: O(n^2)
# Best case: O(n^2)

# Space Complexity
# O(1) - It's an in-place sorting algorithm.


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
