# Explanation
# Merge Sort is a divide-and-conquer algorithm.
# It divides the input array into two halves, calls itself for the two halves,
# and then merges the two sorted halves.

# Time Complexity
# Worst case: O(n log n)
# Average case: O(n log n)
# Best case: O(n log n)

# Space Complexity
# O(n) - It requires additional space proportional to the size of the input array.


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


test = [64, 25, 12, 22, 11]

print(merge_sort(test))
