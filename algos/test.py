def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(j - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            min_idx = j
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
