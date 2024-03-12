def selection_sort(arr): # O(n^2)
    for i in range(len(arr) - 1): # n -> O(n)
        min = i # 1 * n -> O(n)

        for j in range(i + 1, len(arr)): # n * n -> O(n^2)
            if(arr[j] < arr[min]): # 1 * n * n -> O(n^2)
                min = j # 1 * n * n -> O(n^2)

        if min != i: # 1 * n -> O(n)
	        arr[i], arr[min] = arr[min], arr[i] # 1 * n -> O(n)



array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

selection_sort(array)

print("After: ", array)
