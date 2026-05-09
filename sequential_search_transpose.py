#교환하기 전략이 추가된 순차 탐색 알고리즘
def sequential_search_transpose(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            if i>low:
                A[i], A[i-1] = A[i-1], A[i]
                i = i-1
            return i
    return -1
