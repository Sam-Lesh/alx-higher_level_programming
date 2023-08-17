def subtracting(list_num):
    return max(list_num) - sum(list_num)

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_num = [0]
    number = 0
    last_roman = 0
    
    for a in roman_string:
        if a in roman_num:
            if roman_num[a] <= last_roman:
                number += subtracting(list_num)
                list_num = [roman_num[a]]
            else:
                list_num.append(roman_num[a])
            
            last_roman = roman_num[a]
    
    number += subtracting(list_num)
    return number
