# Problem: Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example
# For
# picture = ["abc",
#           "ded"]
# the output should be
# solution(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]

# Solution -------------------------------------------------------------------------------------------------------------
def add_border(m):
    # get length of elements in matrix
    e_len = len(m[0])

    # create top and bottom of matrix
    end_cap = "*" * (e_len + 2)

    # append border to elements in matrix
    new_m = ["*" + i + "*" for i in m]

    # insert top and bottom border
    new_m.insert(0, end_cap)
    new_m.insert(len(new_m), end_cap)

    return new_m


picture = ["abc",
           "ded"]

print(add_border(picture))
