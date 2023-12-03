def search(arr, N, x):
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
if __name__ == "__main__":
    arr = [10, 50, 30, 70, 80,20, 90, 40]
    x = 80
    N = len(arr)

    # Function call
    result = search(arr, N, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
