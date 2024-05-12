def linearSearch(arr: list[int], val: int) -> str:
    for i in range(len(arr)):
        if val == arr[i]:
            return "Element is Present in the Array."
        
    return "Match NOT Found!"

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(linearSearch(arr,35))