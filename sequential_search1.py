def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return -1
