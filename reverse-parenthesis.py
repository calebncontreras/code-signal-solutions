# Problem: Reverse Parenthesis

# Write a function that reverses characters in (possibly nested) parentheses in the input string.
# Input strings will always be well-formed with matching ()s.
# For inputString = "(bar)", the output should be
# solution(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# solution(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# solution(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# solution(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim"

# Solution -------------------------------------------------------------------------------------------------------------


def reverse_parentheses(s):
    # loop entire string
    for x in range(len(s)):
        # save index of left parenthesis
        # start will be the index of inner-most parenthesis
        if s[x] == "(":
            start = x
            print(s[:start])
        # save index of right parenthesis
        if s[x] == ")":
            end = x
            print(s[end:])
            # remove parenthesis around target and reverse the string
            # new string is concatenated with the rest of the string and other parenthesis are
            # checked recursively
            return reverse_parentheses(s[:start] + s[start + 1:end][::-1] + s[end + 1:])
    # if no parenthesis are found return the string
    return s


print(reverse_parentheses("foo(bar(baz))blim"))
# nested_parenthesis("foobar")
