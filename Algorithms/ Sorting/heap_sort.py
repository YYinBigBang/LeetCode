# Heap Sort Algorithm

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

    return arr


def heapify(arr, heap_size, root_index):
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    # Check if left child is larger
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        # Recursively heapify the affected subtree
        heapify(arr, heap_size, largest)


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print(f"Unsorted data: {data}")

    sorted_data = heap_sort(data)
    print(f"Sorted data: {sorted_data}")

