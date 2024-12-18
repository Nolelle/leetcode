# Explanation
# Insertion Sort builds the final sorted array one item at a time.
# It iterates through an input array and removes one element per iteration,
# finds the place the element belongs in the sorted list, and inserts it there.

# Time Complexity

# Worst case: O(n^2)
# Average case: O(n^2)
# Best case: O(n) (when the array is already sorted)

# Space Complexity
# O(1) - It's an in-place sorting algorithm.


def insertionsort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key

    return arr
