def BinarySearch(arr: list[int], val: int) -> str:
    arr.sort()
    lb = 0 
    ub = len(arr) - 1
    mid = int((lb+ub)/2)
    while lb < ub and arr[mid] != val:
        if val < arr[mid]:
            ub = mid - 1
        else:
            lb = mid + 1
        mid = int((lb+ub)/2)
    if arr [mid] == val : return "Match Found! at " + str(mid) 
    else : return "Match Not Found!"



if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(BinarySearch(arr, 200))