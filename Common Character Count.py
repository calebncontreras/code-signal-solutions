# Given two strings, find the number of common characters between them.

# Solution

def common_character_count(s1, s2):
    counter = 0
    for x in range(len(s1)):
        # check if s2 contains the char in s1
        if s1[x] in s2:
            # if true increment counter
            counter += 1
            # get location of char
            loc = s2.index(s1[x])
            # remake string without the char at index x
            s2 = s2[:loc] + s2[loc + 1:]

    print(counter)


string1 = "aabcc"
string2 = "adcaa"

common_character_count(string1, string2)
