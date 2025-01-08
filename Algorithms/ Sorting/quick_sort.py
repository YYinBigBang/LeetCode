# Quick Sort Algorithm

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose the first element as pivot
    pivot = arr[0]

    # Elements less than pivot
    left = [x for x in arr[1:] if x < pivot]

    # Elements greater or equal to pivot
    right = [x for x in arr[1:] if x >= pivot]

    # Recursively sort the sub-lists
    return quick_sort(left) + [pivot] + quick_sort(right)

