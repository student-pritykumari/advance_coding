def min_operations(n, A, K):
    # Step 1: Check feasibility
    remainder = A[0] % K
    for num in A:
        if num % K != remainder:
            return -1

    # Step 2: Sort array
    A.sort()

    # Step 3: Choose median
    median = A[n // 2]

    # Step 4: Count operations
    operations = 0
    for num in A:
        operations += abs(num - median) // K

    return operations


# User input (exam format)
n = int(input())
A = list(map(int, input().split()))
K = int(input())

print(min_operations(n, A, K))