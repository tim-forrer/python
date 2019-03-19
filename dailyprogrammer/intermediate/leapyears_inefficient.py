def is_leap_year(year):
    if year % 900 == 600 or year % 900 == 200: #exception to the exception, referred to as "leape" year
        return True
    elif year % 100 == 0: #exception
        return False
    elif year % 4 == 0: #general rule
        return True
    return False

def num_leap_years(year1, year2):
    num = 0
    i = 0
    while year1 + i < year2:
        if is_leap_year(year1 + i) == True:
            num += 1
        i += 4
    return num

print(num_leap_years(2016, 37847300)) #9166969