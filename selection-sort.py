def selectionSort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        sort = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[sort]:
                sort = j
        if arr[i] != arr[sort]:
            arr[i], arr[sort] = arr[sort], arr[i]
    return arr

if __name__ == "__main__":
    arr = [100, 80, 90, 70, 10, 50, 20, 40, 30, 0, 60]
    arr2 = [8, 4, 9, 2, 10, 3]
    print(selectionSort(arr))
    print(selectionSort(arr2))