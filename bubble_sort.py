def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range (0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

                swapped = True

        if not swapped:
            break

if __name__ == "__main__":
    array_to_sort = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", array_to_sort)
    bubble_sort(array_to_sort)
    print("Sorted array:", array_to_sort)