def upc_final_digit(upc):
    insert_zeroes_number = 11 - len(str(upc))
    upc_list = [ "0" for i in range(insert_zeroes_number)]
    upc_list.append(str(upc))
    upc_string = "".join(upc_list)

    odd_sum = 0
    even_sum = 0
    for i in range(0, len(upc_string), 2):
        odd_sum += int(upc_string[i])
    
    odd_sum *= 3

    for i in range(1, len(upc_string), 2):
        even_sum += int(upc_string[i])
    
    final_sum = odd_sum + even_sum
    potential_digit = final_sum % 10

    if potential_digit != 0:
        final_digit = 10 - potential_digit
    else:
        final_digit = 0
    
    return final_digit

assert upc_final_digit(1234567)