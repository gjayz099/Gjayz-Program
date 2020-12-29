board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

your_player = "X"


running_game = True


def play_game():
    

    display_board()
    
    while running_game:

        pick_num(your_player)

        check_if_game_over()

        change_player()

def display_board():
    print(board[6] + " | " + board[7] + " | " + board[8] + "\t" + " 7 | 8 | 9 ")
    print(board[3] + " | " + board[4] + " | " + board[5] + "\t" + " 4 | 5 | 6 ")
    print(board[0] + " | " + board[1] + " | " + board[2] + "\t" + " 1 | 2 | 3 ")


def pick_num(player):

    print(player + "'s turn.....")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:    
            print("You can't go there. Go again.")

    board[position] = player

    display_board()

def check_if_game_over():
    check_winner()
    check_tie()
 
def check_winner():
    
    #check rows 
    if((board[0] == board[1]) and (board[1]== board[2]) and (board[0] == your_player)):
        print("wins the game!!\t",your_player)
        quit()
    elif((board[3] == board[4]) and (board[4]== board[5]) and (board[3] == your_player)):
        print("wins the game!!\t",your_player)
        quit()
    elif((board[6] == board[7]) and (board[7]== board[8]) and (board[6] == your_player)):
        print("wins the game!!\t",your_player)
        quit()
    #check collums
    elif((board[0] == board[3]) and (board[3]== board[6]) and (board[0] == your_player)):
        print("wins the game!!\t",your_player)
        quit()
    elif((board[1] == board[4]) and (board[4]== board[7]) and (board[1] == your_player)):
        print("wins the game!!\t",your_player)
        quit()
    elif((board[2] == board[5]) and (board[5]== board[8]) and (board[2] == your_player)):
        print("wins the game!!\t", your_player)
        quit()
    #check diagonals
    elif((board[0] == board[4]) and (board[4] == board[8]) and (board[0] == your_player)):
        print("wins the game!!\t", your_player)
        quit()
    elif((board[2] == board[4]) and (board[4] == board[6]) and (board[2] == your_player)):
        print("wins the game!!\t", your_player)
        quit()

def check_tie():
    
    global running_game

    if "-" not in board:
        running_game = False
        print("The game is over!IT'S A TIE")
        return running_game
    else:
        running_game = True
        return running_game 

def change_player():

    global your_player

    if your_player == "X":
        your_player = "O"

    elif your_player == "O":
        your_player = "X"
    return


play_game()
quit()