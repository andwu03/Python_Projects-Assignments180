"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
Completed by Andrew Wu and Andre Rodrigues on Nov 21, 2021
"""
def is_empty(board): #done
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] != " "):
                return False
    return True
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if ((x_end + d_x) < 0 or (y_end + d_y) > 7 or (x_end + d_x) > 7): # handles the case where the end square is outside the board
        bound_square1 = None # bound square is off the board
    else:
        bound_square1 = board[y_end + d_y][x_end + d_x]
    if ((y_end - d_y * length) < 0 or (x_end - d_x * length) < 0 or (y_end - d_y * length) > 7 or (x_end - d_x * length) > 7): # handles the case where the end square is outside the board
        bound_square2 = None # bound square is off the board
    else:
        bound_square2 = board[y_end - d_y * length][x_end - d_x * length]

    if bound_square1 == " " and bound_square2 == " ": # both need to be open
        return "OPEN"
    elif bound_square1 == " " or bound_square2 == " ": # this implies that at least one of them is closed or at an edge (None)
        return "SEMIOPEN"
    else:
        return "CLOSED"

def same_colour(board, col, y_start, x_start, length, d_y, d_x): 
    #this method assumes that we are dealing with seq that exist
    for i in range(length):
        if (board[y_start + i * d_y][x_start + i * d_x] != col):
            return False
    return True

def detect_row(board, col, y_start, x_start, length, d_y, d_x): 
    #number of sequences of length that are possible given the starting positions
    if (d_x < 0): # (1, -1)
        num_seq = min(9 - y_start - length, x_start - length + 2)
    elif (d_x + d_y) == 2: # (1, 1)
        num_seq = min(9 - y_start - length, 9 - x_start - length)
    elif (d_y == 1):
        num_seq = 9 - length - y_start
    else:
        num_seq = 9 - length - x_start
    if num_seq < 0: num_seq = 0 #good

    open_seq_count, semi_open_seq_count = 0,0

    for i in range(num_seq): # start from the first possible ending squares
        if ((x_start + d_x * i - d_x) < 0 or (y_start + d_y * i - d_y) < 0 or(y_start + d_y * i - d_y) > 7 or (x_start + d_x * i - d_x) > 7): # handles the case where the end square is outside the board
            bound_square1 = None # bound square is off the board
        else:
            bound_square1 = board[y_start + d_y * i - d_y][x_start + d_x * i - d_x]
        if ((y_start + d_y * i + d_y * (length - 1) + d_y) < 0 or (x_start + d_x * i + d_x * (length - 1) + d_x) < 0 or (y_start + d_y * i + d_y * (length - 1) + d_y) > 7 or (x_start + d_x * i + d_x * (length - 1) + d_x) > 7): # handles the case where the end square is outside the board
            bound_square2 = None # bound square is off the board
        else:
            bound_square2 = board[y_start + d_y * i + d_y * (length - 1) + d_y][x_start + d_x * i + d_x * (length - 1) + d_x] #this is failing

        if (same_colour(board, col, y_start + d_y * i, x_start + d_x * i, length, d_y, d_x) and bound_square1 != col and bound_square2 != col): 
        #we need to check that the seq of length is all the same colour
        #if they are not the same colour, then these sequences are not open or closed
        #we also need to check if the boundary squares are different colours or not
            
            var = is_bounded(board, y_start + d_y * i + d_y * (length - 1), x_start + d_x * i + d_x * (length - 1), length, d_y, d_x)
            if (var == "OPEN"):
                open_seq_count += 1
            elif (var == "SEMIOPEN"):
                semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    
    for i in range(8): #we need to use detect_row with each of the possible d_y and d_x
        a, b = detect_row(board, col, i, 0, length, 0, 1) # this is horizontal, this is failing
        open_seq_count += a
        semi_open_seq_count += b

        a, b = detect_row(board, col, 0, i, length, 1, 0) # this is vertical
        open_seq_count += a
        semi_open_seq_count += b

        a, b = detect_row(board, col, i, 0, length, 1, 1) # this is upp lef to low rt, vert
        open_seq_count += a
        semi_open_seq_count += b

        if i != 0:
            a, b = detect_row(board, col, 0, i, length, 1, 1) # this is upp lef to low rt, horz, WE ALSO NEED TO AVOID DOUBLE-COUNTING
            open_seq_count += a
            semi_open_seq_count += b

        a, b = detect_row(board, col, i, 7, length, 1, -1) # this is low lef to upp rt, vert
        open_seq_count += a
        semi_open_seq_count += b

        if i != 7:
            a, b = detect_row(board, col, 0, i, length, 1, -1) # this is low lef to upp rt, horz, WE ALSO NEED TO AVOID DOUBLE-COUNTING
            open_seq_count += a
            semi_open_seq_count += b

    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    move_y, move_x = 0, 0
    opt_score = float('-inf')

    for y in range(8): #this is y
        for x in range(8): #this is x
            if (board[y][x] == " "):
                board[y][x] = "b" #changes the board
                if score(board) > opt_score:
                    opt_score = score(board)
                    move_y, move_x = y, x
                board[y][x] = " " #reverts it after the move
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i) #this is failing
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def check_five(board, col, y_start, x_start, d_y, d_x): 
    #this method assumes that we are not starting on an illegal square
    #col = board[y_start][x_start]
    if y_start - d_y < 0 or x_start - d_x < 0 or x_start - d_x > 7:
        bound1 = None
    else:
        bound1 = board[y_start - d_y][x_start - d_x]
    if y_start + 5 * d_y > 7 or x_start + 5 * d_x > 7 or x_start + 5 * d_x < 0:
        bound2 = None
    else:
        bound2 = board[y_start + 5 * d_y][x_start + 5 * d_x]
    
    for i in range(5):
        if (board[y_start + i * d_y][x_start + i * d_x] != col):
            return False
    
    #If the function reaches here, then we have found a seq of length 5
    #we cannot have the bound squares have the same col
    if bound1 == col or bound2 == col:
        return False

    return True

def is_win(board): #there can never be more than one winner
    winner = "Continue playing"

    #first we check the horizontals
    for i in range(8):
        for j in range(4):
            if (check_five(board, "b", i, j, 0, 1)):
                winner = "Black won"
            elif (check_five(board, "w", i, j, 0, 1)):
                winner = "White won"
    
    #then we check the verticals
    if (winner == "Continue playing"):
        for i in range(4):
            for j in range(8):
                if (check_five(board, "b", i, j, 1, 0)):
                    winner = "Black won"
                if (check_five(board, "w", i, j, 1, 0)):
                    winner = "White won"

    #then we check upp lef to low rt
    if (winner == "Continue playing"):
        for i in range(4):
            for j in range(4):
                if (check_five(board, "b", i, j, 1, 1)):
                    winner = "Black won"
                if (check_five(board, "w", i, j, 1, 1)):
                    winner = "White won"
    
    #lastly we check the low lef to upp rt
    if (winner == "Continue playing"):
        for i in range(4):
            for j in range(4):
                if (check_five(board, "b", i, j + 4, 1, -1)):
                    winner = "Black won"
                if (check_five(board, "w", i, j + 4, 1, -1)):
                    winner = "White won"
    
    #finally we check for draw
    if (winner == "Continue playing"):
        flag = True

        for i in range(8):
            for j in range(8):
                if board[i][j] == " ":
                    flag = False

        if (flag == True):
            winner = "Draw"
    
    return winner
                    
def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
           
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #    
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
       
if __name__ == '__main__':
    play_gomoku(8)