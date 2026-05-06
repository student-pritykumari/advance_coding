def min_operations(n, A, K):
    remainder = A[0] % K
    for num in A:
        if num % K != remainder:
            return -1
    A.sort()
    median = A[n // 2]

    operations = 0
    for num in A:
        operations += abs(num - median) // K

    return operations

n = int(input())
A = list(map(int, input().split()))
K = int(input())

print(min_operations(n, A, K))
