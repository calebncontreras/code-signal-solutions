# Problem: Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements
# in one of the arrays. Given two arrays a and b, check whether they are similar.
# Examples: For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# solution(a, b) = true.
#
# The arrays are equal, no need to swap any elements.
#
# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# solution(a, b) = true.
#
# We can obtain b from a by swapping 2 and 1 in b.
#
# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# solution(a, b) = false.
#
# Any swap of any two elements either in a or in b won't make a and b equal.

# Solution -------------------------------------------------------------------------------------------------------------

def solution(a, b):
    arr_len = len(a)  # Check if arrays are equal
    if a == b:
        return True
    for x in range(arr_len):
        if a[x] != b[x]:  # Check for unequal elements
            y = x + 1  # Set index for forward searching loop
            while y < arr_len:  # Begin forward search
                temp = a[::]  # Loop starts with a fresh copy on every iteration
                temp[x], temp[y] = temp[y], temp[x]  # Swap elements
                # print(temp)
                if temp == b:  # Check for equality
                    return True
                else:
                    y += 1  # Iterate forward
            y = x - 1  # Set index for backward loop
            while y >= 0:  # Begin backward loop
                temp = a[::]
                temp[x], temp[y] = temp[y], temp[x]
                # print(temp)
                if temp == b:
                    return True
                else:
                    y -= 1
            else:
                return False
    return False

a = [1, 2, 3]
b = [2, 1, 3]

solution(a, b)