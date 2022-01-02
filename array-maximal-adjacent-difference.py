# Problem: Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
#
# Example:
#
# For inputArray = [2, 4, 1, 0], the output should be
# solution(inputArray) = 3.

# Solution -------------------------------------------------------------------------------------------------------------

def solution(a):
    max_diff = 0
    for x in range(len(a) - 1):
        abs_diff = abs(a[x] - a[x + 1])
        if abs_diff > max_diff:
            max_diff = abs_diff
    return max_diff

print(solution([-1, 4, 10, 3, -2]))

