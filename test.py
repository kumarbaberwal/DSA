def bubbleSort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [100, 80, 90, 70, 10, 50, 20, 40, 30, 0, 60]
    arr2 = [8, 4, 9, 2, 10, 3]
    print(bubbleSort(arr))
    print(bubbleSort(arr2))