'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random, copy

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
#Problem3
def is_row_all_marks(board, row_i, mark):
    flag = True

    for i in range(3):
        if (board[row_i][i] is not mark):
            flag = False

    return flag

def is_col_all_marks(board, col_i, mark):
    flag = True

    for i in range(3):
        if (board[i][col_i] is not mark):
            flag = False
    
    return flag

def is_pos_diagonal_all_marks(board, mark):
    flag = True

    i, j = 0,2

    while(flag and i < 3):
        if (board[i][j] is not mark):
            flag = False
        i += 1
        j -= 1

    return flag

def is_neg_diagonal_all_marks(board, mark):
    flag = True

    i, j = 0,0

    while(flag and i < 3):
        if (board[i][j] is not mark):
            flag = False
        i += 1
        j += 1

    return flag

def is_win(board, mark):
    flag = False

    count = 0
    while (not flag and count < 3):
        if (is_row_all_marks(board, count, mark)):
            flag = True
        count += 1
    
    count = 0
    while (not flag and count < 3):
        if (is_col_all_marks(board, count, mark)):
            flag = True
        count += 1

    if (not flag and is_pos_diagonal_all_marks(board, mark)):
        flag = True
    if (not flag and is_neg_diagonal_all_marks(board, mark)):
        flag = True

    return flag

def game_over(board, move_list):
    winner = "None"

    if (is_win(board, "X")):
        winner = "X"
    elif (is_win(board, "O")):
        winner = "O"
    elif(len(move_list) is 9):
        winner = "Tie"

    return winner
#End of Problem 3

#Problem1
def move(integer_num):
    coord = []

    coord.append((integer_num - 1)//3)
    coord.append((integer_num - 1) % 3)

    return coord

def put_in_board(board, mark, square_num):
    coord = move(square_num)
    board[coord[0]][coord[1]] = mark

def is_legal(move, move_list):
    legal_moves = ["1","2","3","4","5","6","7","8","9"]
    if (not (move in legal_moves) or (move in move_list)):
        print("Illegal move, try again")
        return False
    
    return True
        
def vs_human(board, move_list):
    player = False

    while (game_over(board, move_list) is "None"):
        legal = False
        while (not legal):
            turn = input("Player " + str(int(player + 1)) + ", please make a legal move: ")
            if (turn is "q"):
                exit()
            legal = is_legal(turn, move_list)
            if (legal):
                move_list.append(turn) #here turn is a string

        char = "X"
        if (player):
            char = "O"

        put_in_board(board, char, int(move_list[-1]))

        player = not player

        print_board_and_legend(board) 

        print("\n")
    
    if (game_over(board, move_list) is "Tie"):
        print("THe game was a tie.")
    else:
        if (game_over(board, move_list) is "X"):
            print("Congrats Player 1! You win!")
        else:
            print("Congrats Player 2! You win!")
#End of Problem 1

#Problem 2

def is_emh(input):
    if (input == "e" or input == "m" or input == "h"):
        return True
    else:
        return False

def is_12(input):
    if (input == "1" or input == "2"):
        return True
    else: 
        return False

def get_free_squares(move_list):
    free = []
    value = []

    for i in range(9): #goes from 0 to 8
        if (not (str(i + 1) in move_list)):
            value.append((i//3))
            value.append(i % 3)
            free.append(value)
            value = []
    
    return free

def make_random_moves(board, mark, move_list):
    free = get_free_squares(move_list)

    num = int(len(free) * random.random())

    square_num = free[num][0] * 3 + free[num][1] + 1

    put_in_board(board, mark, square_num)

    return square_num

def one_move_ahead(board, mark, move_list): #add a return value for the square_num or -1 for nothing
    free = get_free_squares(move_list)
    flag = False
    i = 0
    
    while(i < len(free)):
        board2 = copy.deepcopy(board)
        move_list2 = copy.deepcopy(move_list)

        square_num = free[i][0] * 3 + free[i][1] + 1

        move_list2.append(str(square_num))

        put_in_board(board2, mark, square_num)

        if (game_over(board2, move_list2) == mark):
            return square_num
        i += 1

    return -1

def you_cannot_win_hehe(board, mark, player_mark, move_list, player):
    #for Turn, False means com is 2, True means com is 1

    if (player == True): #computer goes first
        num1 = one_move_ahead(board, mark, move_list) 
        num2 = one_move_ahead(board, player_mark, move_list)
        if (len(move_list) == 0): #this is the deafult first move
                put_in_board(board, mark, 5)
                move_list.append("5")
        elif (num1 != -1): #checks if computer has a win, if so, plays it
            put_in_board(board, mark, num1)
            move_list.append(str(num1))
        elif (num2 != -1): #checks if player has a win if computer plays sub-optimally, if so, blocks it
            put_in_board(board, mark, num2)
            move_list.append(str(num2))
        else:
            last_move = int(move_list[-1])
            if (last_move % 2 == 1 and len(move_list) == 2):
                if (last_move == 1 or last_move == 9):
                    put_in_board(board, mark, 3)
                    move_list.append("3")
                else:
                    put_in_board(board, mark, 1)
                    move_list.append("1")
            elif (last_move % 2 == 0 and len(move_list) == 2):
                if (last_move == 2 or last_move == 4):
                    put_in_board(board, mark, 9)
                    move_list.append("9")
                else:
                    put_in_board(board, mark, 1)
                    move_list.append("1")
            else:
                num = make_random_moves(board, mark, move_list)
                move_list.append(str(num))

    if (player == False): #if computer goes second
        num1 = one_move_ahead(board, mark, move_list) 
        num2 = one_move_ahead(board, player_mark, move_list)
         #player's last move
        if (num1 != -1): #checks if computer has a win, if so, plays it
            put_in_board(board, mark, num1)
            move_list.append(str(num1))
        elif (num2 != -1): #checks if player has a win if computer plays sub-optimally, if so, blocks it
            put_in_board(board, mark, num2)
            move_list.append(str(num2))
        else: #this executs if the computer does not see an immediate win for anyone
            if (len(move_list) == 1):
                num = int(move_list[-1])
                if (num == 5): #if user starts with the center
                    put_in_board(board, mark, 1)
                    move_list.append("1")
                else: #if user starts with an edge or a corner
                    put_in_board(board, mark, 5)
                    move_list.append("5")
            elif (len(move_list) == 3):
                start = int(move_list[-3])
                last = int(move_list[-1])
                if (start == 5 and last == 9): #if user starts in center
                    put_in_board(board, mark, 3)
                    move_list.append("3")
                elif (start == 1):
                    if (last == 9): #this is the opposite case
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                    elif (last == 6 or last == 8):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                elif (start == 9):
                    if (last == 1):
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                    elif (last == 2 or last == 4):
                        put_in_board(board, mark, 1)
                        move_list.append("9")
                elif (start == 3):
                    if (last == 7): #this is the opposite case
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                    elif (last == 4 or last == 8):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                elif (start == 7):
                    if (last == 3): #this is the opposite case
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                    elif (last == 2 or last == 6):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                elif (start == 2): #if user starts on an edge
                    if (last == 4):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
                    elif (last == 6):
                        put_in_board(board, mark, 1)
                        move_list.append("1")
                    elif (last == 7):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
                    elif (last == 9):
                        put_in_board(board, mark, 1)
                        move_list.append("1")
                    elif (last == 8):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                elif (start == 8):
                    if (last == 4):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                    elif (last == 6):
                        put_in_board(board, mark, 7)
                        move_list.append("7")
                    elif (last == 2):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                    elif (last == 1):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                    elif (last == 3):
                        put_in_board(board, mark, 7)
                        move_list.append("7")
                elif (start == 4):
                    if (last == 2):
                        put_in_board(board, mark, 7)
                        move_list.append("7")
                    elif (last == 8):
                        put_in_board(board, mark, 1)
                        move_list.append("1")
                    elif (last == 6):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                    elif (last == 3):
                        put_in_board(board, mark, 7)
                        move_list.append("7")
                    elif (last == 9):
                        put_in_board(board, mark, 1)
                        move_list.append("1")
                elif (start == 6):
                    if (last == 2):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                    elif (last == 8):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
                    elif (last == 4):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                    elif (last == 1):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                    elif (last == 7):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
            elif (len(move_list) == 5):
                start = int(move_list[-5])
                second = int(move_list[-3])
                last = int(move_list[-1])
                if (start == 5):
                    if (second == 2 and last == 9):
                        put_in_board(board, mark, 4)
                        move_list.append("4")
                    elif (second == 4 and last == 9):
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                elif (start == 1):
                    if (second == 3):
                        put_in_board(board, mark, 4)
                        move_list.append("4")
                    if (second == 7):
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                elif (start == 3):
                    if (second == 1):
                        put_in_board(board, mark, 4)
                        move_list.append("4")
                    if (second == 9):
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                elif (start == 9):
                    if (second == 3):
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                    if (second == 7):
                        put_in_board(board, mark, 4)
                        move_list.append("4")
                elif (start == 7):
                    if (second == 1):
                        put_in_board(board, mark, 2)
                        move_list.append("2")
                    if (second == 9):
                        put_in_board(board, mark, 4)
                        move_list.append("4")
                elif (start == 2):
                    if (second == 7 and last == 6):
                        put_in_board(board, mark, 1)
                        move_list.append("1")
                    if (second == 9 and last == 4):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
                elif (start == 4):
                    if (second == 9 and last == 2):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
                    if (second == 3 and last == 8):
                        put_in_board(board, mark, 9)
                        move_list.append("9")
                elif (start == 6):
                    if (second == 7 and last == 2):
                        put_in_board(board, mark, 1)
                        move_list.append("1")
                    if (second == 1 and last == 8):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
                elif (start == 8):
                    if (second == 3 and last == 4):
                        put_in_board(board, mark, 1)
                        move_list.append("1")
                    if (second == 1 and last == 6):
                        put_in_board(board, mark, 3)
                        move_list.append("3")
            else: #this is the non-specific block, if everything else has already been checked, play a random move that does not lose
                num = make_random_moves(board, mark, move_list)
                move_list.append(str(num))
            
def vs_computer(board, move_list):
    flag1 = False
    flag2 = False
    
    while (not flag1):
        difficulty = input("Type e for easy mode, m for medium mode, and h for hard mode: ")
        flag1 = is_emh(difficulty)
    while (not flag2):
        player = input("Type 1 for Player 1 and type 2 for Player 2: ")
        flag2 = is_12(player)
    
    if (player is "1"):
        player = False
    else:
        player = True

    player_char, computer_char = "X", "O"
    if (player):
        player_char, computer_char = computer_char, player_char
        
    while (game_over(board, move_list) is "None" and not player):
        legal = False
        while (not legal):
            turn = input("Player " + str(int(player + 1)) + ", please make a legal move: ")
            if (turn is "q"):
                print("Goodbye.")
                exit()
            legal = is_legal(turn, move_list)
            if (legal):
                move_list.append(turn) #here turn is a string

        put_in_board(board, player_char, int(move_list[-1]))

        print_board_and_legend(board)

        if (len(move_list) < 9 and game_over(board, move_list) is "None"):
            if (difficulty == "e"):
                num = make_random_moves(board, computer_char, move_list)
                move_list.append(str(num))
            elif (difficulty == "m"):
                num = one_move_ahead(board, computer_char, move_list)

                if (num != -1):
                    put_in_board(board, computer_char, num)
                else:
                    num = make_random_moves(board, computer_char, move_list)
                
                move_list.append(str(num))
            elif (difficulty == "h"):
                you_cannot_win_hehe(board, computer_char, player_char, move_list, player)

            print("\nComputer's Move:")

            print_board_and_legend(board)

        print("\n")
        
    while (game_over(board, move_list) is "None" and player):
        if (difficulty == "e"):
            num = make_random_moves(board, computer_char, move_list)
            move_list.append(str(num))
        elif (difficulty == "m"):
            num = one_move_ahead(board, computer_char, move_list)

            if (num != -1):
                put_in_board(board, computer_char, num)
            else:
                num = make_random_moves(board, computer_char, move_list)
                
            move_list.append(str(num))
        elif (difficulty == "h"):
            you_cannot_win_hehe(board, computer_char, player_char, move_list, player)

        print("\nComputer's Move:")

        print_board_and_legend(board)

        print("\n")
            
        if (game_over(board, move_list) is "None"):
            legal = False
            while (not legal):
                turn = input("Player " + str(int(player + 1)) + ", please make a legal move: ")
                if (turn is "q"):
                    print("Goodbye.")
                    exit()
                legal = is_legal(turn, move_list)
                if (legal):
                    move_list.append(turn) #here turn is a string

            put_in_board(board, player_char, int(move_list[-1]))

            print_board_and_legend(board)

            print("\n")

    if (game_over(board, move_list) is "Tie"):
        print("The game was a tie.")
    else:
        if (game_over(board, move_list) is "X" and player is False):
            print("Congrats! You win!")
        elif (game_over(board, move_list) is "O" and player is True):
            print("Congrats! You win!")
        else:
            print("Better luck next time!")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def is_0or1(input):
    if (input == "0" or input == "1"):
        return True
    return False

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    move_list = []
    
    print("\n")
    
    flag = False

    while (not flag):
        val = input("Type 0 for vs_human or 1 for vs_computer: ")
        flag = is_0or1(val)
    if (val == "0"):
        vs_human(board, move_list)
    else:
        vs_computer(board, move_list)  