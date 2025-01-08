# Selection Sort Algorithm

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_index = i
        for j in range(i + 1, n):
            # Update min_index if a smaller element is found
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

