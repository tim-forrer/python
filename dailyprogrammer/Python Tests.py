def diagonal_list(square, n):
    """Given a square on a chessboard, generate a list of squares that are diagonal to it"""
    a = ord("a")
    square_col = ord(square[0]) - a
    square_row = int(square[1])
    diagonal_squares_list = []
    print("The square column number is equal to %d (index number)" %square_col)
    i = 1 
    while square_col - i > -1 and square_row - i > 0: #adding squares to the lower left of the square
        lower_left = chr(square_col - i + a) + str(square_row - i)
        diagonal_squares_list.append(lower_left)
        i += 1
    
    i = 1
    while square_col - i > -1 and square_row + i <= n: #adding squares to the upper left of the square
        upper_left = chr(square_col - i + a) + str(square_row + i)
        diagonal_squares_list.append(upper_left)
        i += 1

    i = 1
    while square_col + i <= n - 1 and square_row - i > 0: #adding squares to the lower right of the square
        lower_right = chr(square_col + i + a) + str(square_row - i)
        diagonal_squares_list.append(lower_right)
        i += 1
        print(square_col + i)

    i = 1
    while square_col + i <= n - 1 and square_row + i <= n: #adding squares to the upper right of the square
        upper_right = chr(square_col + i + a) + str(square_row + i)
        diagonal_squares_list.append(upper_right)
        i += 1
    return diagonal_squares_list

print(diagonal_list("c3",4))