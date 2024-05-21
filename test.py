def HeapSort(arr: list[int]) -> list[int]:
    for i in range((len(arr)-1//2), -1, -1):
        Heapify(arr, len(arr), i)

    for i in range(len(arr)-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)

    return arr

def Heapify(arr: list[int], len: int, parent: int) -> None:
    Largest = parent
    left = 2 * parent + 1
    right = 2 * parent + 2
    if left < len and arr[left] > arr[Largest]:
        Largest = left
    if right < len and arr[right] > arr[Largest]:
        Largest = right

    if Largest != parent:
        arr[parent], arr[Largest] = arr[Largest], arr[parent]
        Heapify(arr, len, Largest)

if __name__ == "__main__":
    arr = [100, 80, 90, 70, 10, 50, 20, 40, 30, 0, 60]
    arr2 = [8, 4, 9, 2, 10, 3]
    arr3 = [8, 4, 9, 2, 10, 3, 0, 10, 1, 12]
    print(HeapSort(arr))
    print(HeapSort(arr2))
    print(HeapSort(arr3))