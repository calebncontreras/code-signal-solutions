# Problem: Given an array of strings, return another array containing all of its longest strings.

# Solution:

def longest_array(array):
    arr_length = len(array)
    # length of first item
    max_len = len(array[0])

    # get length of longest string
    for x in range(arr_length):
        if max_len < len(array[x]):
            max_len = len(array[x])

    # print(max_len)

    result_array = []
    # if item equal to the longest length
    # append to result array
    for x in range(arr_length):
        if len(array[x]) == max_len:
            result_array.append(array[x])

    print(result_array)


inputArray = ["aba", "aa", "ad", "vcd", "aba"]

longest_array(inputArray)

