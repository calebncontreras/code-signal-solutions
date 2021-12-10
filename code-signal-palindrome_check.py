def solution(inputString):
    input_string_list = list(inputString)
    # print(type(input_string_list))
    if input_string_list == input_string_list[::-1]:
        print "True"
    else:
        return "False"
        

user_string = input("type in a string to check for palindrome: ") 
solution(user_string)