def quickSort(arr: list[int], start: int, end: int) -> list[int]:
    if start < end:
        index = partition(arr, start, end)
        quickSort(arr, start, index-1)
        quickSort(arr, index+1, end)

    return arr

def partition(arr: list[int], start: int, end: int) -> int:
    low = start + 1
    high = end
    pivot = arr[start]
    while True:
        while low <= high and arr[low] <= pivot:
            low += 1
        while low <= high and arr[high] >= pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high 

if __name__ == "__main__":
    arr = [100, 80, 90, 70, 10, 50, 20, 40, 30, 0, 60]
    arr2 = [8, 4, 9, 2, 10, 3]
    arr3 = [8, 4, 9, 2, 10, 3, 0, 10, 1, 12]
    print(quickSort(arr, 0, len(arr)-1))
    print(quickSort(arr2, 0, len(arr2)-1))
    print(quickSort(arr3, 0, len(arr3)-1))