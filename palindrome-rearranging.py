# Problem Given a string, find out if its characters can be rearranged to form a palindrome.
# Example
#
# For inputString = "aabb", the output should be
# solution(inputString) = true.
#
# We can rearrange "aabb" to make "abba", which is a palindrome.

# Solution --------------------------------------------------------------------------------------------------------

def palindrome_rearranging(a):
    prev_occurred= [] # Letters which have been checked not be checked twice
    single_occurrence = 0 # Tracks single occurrence of a letter
    for char in a:
        if char not in prev_occurred:
            if a.count(char) % 2 != 0: # If odd number of the same letter excluding a single occurrence cannot be a
                                       # palindrome
                if single_occurrence == 1: # if more than one single occurrence
                    return False
                else:
                    single_occurrence += 1
            prev_occurred.append(char) # add a new letter after it has been counted
    return True

a = "aabb"
b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
c = "abbcabb"
print(palindrome_rearranging(a))
print(palindrome_rearranging(b))
print(palindrome_rearranging(c))

