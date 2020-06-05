def solution(A):
    count, idx = 0, 0

    while A[idx] != -1:
        value = A[idx]
        idx = value
        count += 1
    count += 1
    return count


sol = solution([1, 4, -1, 3, 2])
print(sol)
