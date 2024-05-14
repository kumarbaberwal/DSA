def insertionSort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        pivot = arr [i]
        j = i - 1
        while j >= 0 and pivot < arr [j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivot

    return arr


if __name__ == "__main__":
    arr = [100, 80, 90, 70, 10, 50, 20, 40, 30, 0, 60]
    arr2 = [8, 4, 9, 2, 10, 3]
    print(insertionSort(arr))
    print(insertionSort(arr2))