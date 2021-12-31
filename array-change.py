# Problem: You are given an array of integers. On each move you are allowed to increase exactly one of its element by
# one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

# Example:
# For inputArray = [1, 1, 1], the output should be
# solution(inputArray) = 3.

# Solution -------------------------------------------------------------------------------------------------------------

def solution(a):
    a_len = len(a)
    counter = 0
    for x in range(a_len - 1):
        if a[x] >= a[x + 1]:
            diff = (a[x] - a[x + 1]) + 1
            a[x + 1] += (a[x] - a[x + 1]) + 1
            counter += diff

    return counter


a = [1, 1, 1]
b = [-1000, 0, -2, 0]
c = [2, 1, 10, 1]
print(solution(a))
print(solution(b))
print(solution(c))
