def addigit(num):
    result = 0
    index = 0
    new_num = num
    while index == 0 or new_num != 0:
        unit = new_num % 10
        add_digit = (new_num % 10) + 1
        result += add_digit * 10 ** index
        new_num = int(float(new_num) / 10)
        if add_digit == 10:
            index += 2
        else:
            index += 1
    return result
