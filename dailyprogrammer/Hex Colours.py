def hex_colour(red, green, blue):
    colour_list = [red, green, blue]
    hex_value = "#"
    for i in colour_list:
        if 0<= i <=15:
            individual_hex = "0%X" % i
        else:
            individual_hex = "%X" % i
        
        hex_value = hex_value + individual_hex
    
    return hex_value

def avg_list(alist):
    return int(round(sum(alist) / len(alist)))

def blend(alist):
    red_list = []
    green_list = []
    blue_list = []

    for i in alist:
        red_list.append(int(i[1:3], 16))
        green_list.append(int(i[3:5], 16))
        blue_list.append(int(i[5:], 16))
    
    red = avg_list(red_list)
    green = avg_list(green_list)
    blue = avg_list(blue_list)
    return hex_colour(red, green, blue)

print(blend({"#000000", "#778899"}))