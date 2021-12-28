# Problem: Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum
# of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not.

def is_lucky(t_num):

    t_str = str(t_num)
    t_len = len(t_str)
    split_loc = int(t_len / 2)
    first_val = 0
    second_val = 0

    for x in range (split_loc):
        # print(t_str[x])
        first_val += int(t_str[x])

    for x in range(split_loc, t_len):
        # print(t_str[x])
        second_val += int(t_str[x])

    if first_val == second_val:
        return True
    else:
        return False






print(is_lucky(1230))