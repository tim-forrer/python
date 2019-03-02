def row_check(soln):
    """Checking that the no queen shares a row number with another queen"""
    row_check = []
    for item in soln:
        if item in row_check:
            return False
        else:
            row_check.append(item)
    return True

def diagonal_list(square, n):
    """Given a square on a chessboard, generate a list of squares that are diagonal to it"""
    a = ord("a")
    square_col = ord(square[0]) - a
    square_row = int(square[1])

    diagonal_squares_list = []
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

    i = 1
    while square_col + i <= n - 1 and square_row + i <= n: #adding squares to the upper right of the square
        upper_right = chr(square_col + i + a) + str(square_row + i)
        diagonal_squares_list.append(upper_right)
        i += 1
    return diagonal_squares_list


def diagonal_check(soln):
    """Checking that no queens are diagonal to each other"""
    n = len(soln)
    col_letters = []
    for i in range(n):
        col_letters.append(chr(ord("a") + i))

    char_solution = [] #generating the solution that corresponds the letter column to the row number
    for i in range(n):
        char_solution.append(col_letters[i] + str(soln[i]))
    
    diagonal_squares = []
    for item in char_solution:
        diagonal_squares.extend(diagonal_list(item, n))

    for item in char_solution:
        if item in diagonal_squares:
            return False

    return True


def valid_solution(soln):
    """Checks if a given solution is valid"""
    if diagonal_check(soln) == True and row_check(soln) == False:
        return print("Your solution is invalid, it has queens in the same row.")
    elif diagonal_check(soln) == False and row_check(soln) == True:
        return print("Your solution is invalid, it has queens in the same diagonal.")
    elif diagonal_check(soln) == False and row_check(soln) == False:
        return print("Your solution has queens sharing rows and diagonals.")
    else:
        return print("Your solution is valid!")
            
def potential_solution():
    """ User inputs the potential solution"""
    n = int(input("How many rows does your chessboard have? "))
    while True:
        num_solution = [] #as dealing with soley integers is easier for now, the character columns have been omitted from the solution inputted
        for i in range(n):
            row_number = int(input("Which row number can the queen in column %s be found? "%(chr(ord("a") + i))) )
            num_solution.append(row_number)
        return valid_solution(num_solution)

potential_solution()