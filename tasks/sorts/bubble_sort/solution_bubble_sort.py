def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    if n == 0:
        return

    any_swap_occurred = False

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                any_swap_occurred = True

        if swapped:
            print(*arr)
        else:
            break

    if not any_swap_occurred:
        print(*arr)