def balanced_xy(xy_string):
    check_string = ""
    x_counter = 0
    y_counter = 0
    for i in xy_string:
        if i == "x":
            x_counter += 1
        else:
            y_counter += 1
        
    if x_counter == y_counter:
        return True
    else:
        return False
        
#print(balanced_xy(""))

def check_string(string):
    test_list = []
    for i in range(len(string)):
        if string[i] not in test_list:
            test_list.append(string[i])
    test_string = "".join(test_list)
    return test_string
                
#print(check_string(""))

def balanced(string):
    test_string = check_string(string)
    for i in range(len(test_string) -1):
        if string.count(test_string[i]) != string.count(test_string[i+1]):
            return False
    return True
    
#print(balanced(""))