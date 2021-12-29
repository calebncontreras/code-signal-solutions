# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to
# rearrange the people by their heights in a non-descending order without moving the trees.
# People can be very tall!
# For a = [-1, 150, 190, 170, -1, -1, 160, 180],
# the output should be
# solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

# My Solution

def sort_by_height(array):
    indices = [index for index, element in enumerate(array) if element == -1]

    array.sort()

    result_arr = [x for x in array if x != -1]

    for x in indices:
        result_arr.insert(x, -1)

    return result_arr


a = [-1, 150, 190, 170, -1, -1, 160, 180]
sort_by_height(a)
