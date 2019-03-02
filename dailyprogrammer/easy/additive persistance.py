def list_sum(lst):
    sum = 0
    for i in lst:
        sum += int(i)
    return sum

def additive_persisitance(number):
    list_number = list(str(number))
    print(list_number)
    count = 0

    while int("".join(list_number)) > 9:
        new_number = list_sum(list_number)
        list_number = list(str(new_number))
        print(list_number)
        count += 1
    return count