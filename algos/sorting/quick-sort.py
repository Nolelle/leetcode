# Explanation
# Quick Sort is also a divide-and-conquer algorithm.
# It picks an element as pivot and partitions the given array around the picked pivot.
# There are different versions of quickSort that pick pivot in different ways.

# Time Complexity

# Worst case: O(n^2)
# Average case: O(n log n)
# Best case: O(n log n)

# Space Complexity
# O(log n) - Due to the recursive call stack.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


test = [64, 25, 12, 22, 11]

print(quick_sort(test))
