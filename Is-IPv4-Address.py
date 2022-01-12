# Problem: An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a
# computer network that uses the Internet Protocol for communication. There are two versions of the Internet
# protocol, and thus two versions of addresses. One of them is the IPv4 address.
#
# Given a string, find out if it satisfies the IPv4 address naming rules

# Example
# For inputString = "172.16.254.1", the output should be
# solution(inputString) = true;
#
# For inputString = "172.316.254.1", the output should be
# solution(inputString) = false.
#
# 316 is not in range [0, 255].
#
# For inputString = ".254.255.0", the output should be
# solution(inputString) = false.
#
# There is no first number.

# My Failed Regex Solution -------------------------------------------------------------------------------------------------------------

# Rules
# 1: Must be 3 groups of 3 digits and 1 group of one digit seperated by '.'
# 2: The three-digit numbers must be in the range of [0, 255]
import re


def solution(input_str):

    # print(input_str)
    # beg = input_str[0]
    # end = input_str[-1]
    if not re.fullmatch("^\d\.\d\.\d\.\d$", input_str):
        return False
    else:
        split_values = input_str.split('.')  # Split input string into list of digits
        # print(split_values)
        for x in range(len(split_values)):
            n_block = split_values[x]
            n_block = int(n_block)  # If not empty cast to int
            if n_block < 0 or n_block > 255:  # Must be between 0 and 255
                return False
            # if not n_block:  # Empty string
            #     return False
            # else:
            #     if x == len(split_values) - 1:  # If last number in list
            #         if n_block != 1 and n_block != 0:  # Last number must be 1 or 0
            #             return Fals

        return True

# Code Signal solution
def solution_2(input_str):
    p = input_str.split('.')  # Split input string into list of digits

    return len(p) == 4 and all(n.isdigit() and 0 < int(n) < 255 for n in p)

a = "3"
b = "172.316.254.5"
c = ".254.255.0"
d = "255.255.255.255abcdekjhf"
e = "129380129831213981.255.255.255"
f = "172.16.254.1"
g = "0.254.255.0"
print(solution_2(a))
print(solution_2(b))
print(solution_2(c))
print(solution_2(d))
print(solution_2(e))
print(solution_2(f))
print(solution_2(g))
