from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
