def max_cyclic_substring_sum(S):
    n = len(S)
    T = S + S
    
    visited = [0] * 26
    left = 0
    current_sum = 0
    max_sum = 0
    
    for right in range(2 * n):
        idx = ord(T[right]) - ord('a')
        
        # Remove duplicates
        while visited[idx] > 0:
            left_idx = ord(T[left]) - ord('a')
            visited[left_idx] -= 1
            current_sum -= (left_idx + 1)
            left += 1
        
        # Add character
        visited[idx] += 1
        current_sum += (idx + 1)
        
        # Keep window size ≤ n
        while (right - left + 1) > n:
            left_idx = ord(T[left]) - ord('a')
            visited[left_idx] -= 1
            current_sum -= (left_idx + 1)
            left += 1
        
        max_sum = max(max_sum, current_sum)
    return max_sum


# User input (exam style)
S = input().strip()
print(max_cyclic_substring_sum(S))
