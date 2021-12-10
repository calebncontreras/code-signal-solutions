def solution(year):
    str_year = str(year)
    str_year_len = len(str_year)
    
    result = 0
    if str_year_len < 3:
        result = 1
    elif str_year_len == 3:
        result = int(str_year[0])
    else:
        result = int(str_year[0:2])
    
    return result + 1

print(solution(1970))