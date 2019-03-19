def is_leap_year(year):
    if year % 900 == 600 or year % 900 == 200: #exception to the exception
        return True
    elif year % 100 == 0: #exception
        return False
    elif year % 4 == 0: #general rule
        return True
    return False

def leaps(year1, year2):
    num = 0
    order = ord_mag_diff(year1, year2, 900)

    while order >= 0:
        while year2 - year1 > 900 * 10 ** order:
            year1 += 900 * 10 ** order
            num +=218 * 10 ** order
        order -= 1

    
    if year1 % 4 != 0:
        year1 = year1 + 4 - (year1 % 4)

    i = 0
    while year1 + i < year2:
        if is_leap_year(year1 + i) == True:
            num += 1
        i += 4
    
    return num

def ord_mag_diff(year1, year2, unit):
    diff = year2 - year1
    
    order = 0

    while diff / unit > 1:
        unit *= 10
        order += 1
    return order

print(leaps(2016, 2017))
