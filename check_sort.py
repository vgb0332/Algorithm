def check_sort(A):
    n = len(A)
    for i in range(1, n):
        if A[i-1] > A[i]: return False
    return True
