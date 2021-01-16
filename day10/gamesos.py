board = ["1","2","3",
         "4","5","6",
         "7","8","9"] 


# global variables
# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None


# choose the first player x or y then return that value to current player is (x/y)
player = input("1st player choose X/Y")
if(player=="x"):
    current_player = player
    
elif(player=="y"):
    current_player = player


def play_game():
    display_board()
    while(game_still_going):
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "y":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# to display board
def display_board():
    print(board[0] + " | " + board[1] + " | "+ board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | "+ board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | "+ board[8])
    print("--|---|--")

def handle_turn(current_player):
    position = input("Enter the choose from 1-9")
    position = int(position) - 1
    board[position] = current_player
    display_board()
        # print(player + "'s turn.")
        # position = input("Choose a position from 1-9: ")
        # valid = False
        # while not valid:
        #     while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        #         position = input("Choose a position from 1-9: ")
        #     position = int(position) - 1
        # board[position] = player
        # display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "1","2","3","4","5","6","7","8","9" 
    row_2 = board[3] == board[4] == board[5] != "1","2","3","4","5","6","7","8","9"
    row_3 = board[6] == board[7] == board[8] != "1","2","3","4","5","6","7","8","9"
     # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0] 
    elif row_2:
        return board[3] 
    elif row_3:
        return board[6] 
    # Or return None if there was no winner
    else:
        return None
    
    
# Check the columns for a win
def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "1","2","3","4","5","6","7","8","9"
    column_2 = board[1] == board[4] == board[7] != "1","2","3","4","5","6","7","8","9"
    column_3 = board[2] == board[5] == board[8] != "1","2","3","4","5","6","7","8","9"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0] 
    elif column_2:
        return board[1] 
    elif column_3:
        return board[2] 
    # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "1","2","3","4","5","6","7","8","9"
    diagonal_2 = board[2] == board[4] == board[6] != "1","2","3","4","5","6","7","8","9"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0] 
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if  ["1","2","3","4","5","6","7","8","9"]  not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False

# Flip the current player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"
    

    

play_game()


# to display board
# run program
#  choose player return the choosed value
#  