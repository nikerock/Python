#__________________Global Variable_______________________

#game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

#if game is still going
game_still_going =True

#who won? or Tie?
winner = None

#who's turn is it?
current_player = "X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


#Play a game of tic tack toe
def play_game():

    #display initial board
    display_board()

    #while the game is still going
    while game_still_going:

        #handle a single turn of an arbitrary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip to the other player
        flip_player()

    #the game has ended
    if winner =="X" or winner == "O":
        print(winner +" won.")
    elif winner == None:
        print("Tie.")


#handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s Turn")
    position = input("chose a position from 1-9: ")

    valid = False

    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    #set up global variables
    global winner

    #check row
    row_winner = check_rows()
    #check column
    column_winner = check_columns()
    #check diagonal
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None

    return

def check_rows():
    #set up global variable
    global game_still_going
    #check if any  of the rows have all the same value and not empty
    row_1 = board[0] == board[1] ==board[2] != "-"
    row_2 = board[3] == board[4] ==board[5] != "-"
    row_3 = board[6] == board[7] ==board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner(X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():

    #set up global variable
    global game_still_going
    #check if any  of the column have all the same value and not empty
    column_1 = board[0] == board[3] ==board[6] != "-"
    column_2 = board[1] == board[4] ==board[7] != "-"
    column_3 = board[2] == board[5] ==board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    #return the winner(X or O)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    #set up global variable
    global game_still_going
    #check if any  of the diagonal have all the same value and not empty
    diagonal_1 = board[0] == board[4] ==board[8] != "-"
    diagonal_2 = board[2] == board[4] ==board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    #return the winner(X or O)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]

    return


def check_if_tie():
    #global variable we need.
    global game_still_going
    #check weather it is tie.
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    #global variable we need
    global current_player
    #if the current player was X,then change it to O
    if current_player == "X":
        current_player = "O"
    #if the current player was O,then change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()