# Merge Sort Algorithm

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0
    # Merge two sorted sublists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted data: {data}")

    sorted_data = merge_sort(data)
    print(f"Sorted data: {sorted_data}")

