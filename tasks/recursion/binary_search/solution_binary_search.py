def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        current_val = arr[mid]

        if current_val == target:
            return mid
        elif current_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1