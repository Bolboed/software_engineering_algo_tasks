def insertion_sort(arr: list[int]) -> list[int]:

    sorted_arr = arr[:]
    n = len(sorted_arr)

    for i in range(1, n):
        key = sorted_arr[i]
        j = i - 1

        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1

        sorted_arr[j + 1] = key

    return sorted_arr