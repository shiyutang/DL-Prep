import math


def solution(num1, num2):
    # write your code in Python 3.6
    base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    A = base

    for i in range(1, 5):
        for j in range(1, 10):
            b = base[j] ** (2 ** i)
            A.append(b)

    A = A[::-1]
    print(A)

    for idx in range(len(A)):
        if A[idx] in range(num1, num2 + 1, 1):
            word = A[idx]
            print('word', word)
            count = 0
            value = A[idx]
            while math.sqrt(value) == math.sqrt(value) // 1:
                value = math.sqrt(value)
                count += 1
            return count

    print('have not find the answer yet')
    maxcount = 0
    for number in range(num1, num2, 1):
        count = 0
        while math.sqrt(number) == math.sqrt(number) // 1:
            number = math.sqrt(number)
            count += 1
        if count > maxcount:
            maxcount = count
            print('the word is ', number ** (count + 1))
    return maxcount


# sol = solution(4343, 542323)
# sol = solution(76756, 24529457)
sol = solution(390626, 1679615)
# sol = solution(76756, 24529457)

print(sol)
