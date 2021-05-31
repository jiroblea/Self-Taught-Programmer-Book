# A TIC-TAC-TOE GAME!

# print(board[1], board[5], board[9])
# print(board[13], board[17], board[21])
# print(board[25], board[29], board[33])

def checker(board, player, plyr_symbol):
    if (plyr_symbol == board[1] == board[5] == board[9]) or (plyr_symbol == board[13] == board[17] == board[21]) or (plyr_symbol == board[25] == board[29] == board[33]):
        print(f"{player} wins!")
        return False
    elif (plyr_symbol == board[1] == board[13] == board[25]) or (plyr_symbol == board[5] == board[17] == board[29]) or (plyr_symbol == board[9] == board[21] == board[33]):
        print(f"{player} wins!")
        return False
    elif (plyr_symbol == board[1] == board[17] == board[33]) or (plyr_symbol == board[9] == board[17] == board[25]):
        print(f"{player} wins!")
        return False
    return True

def tieChecker(board):
    if ("1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9") not in board:
        print("TIE!")
        return False
    return True


print("TIC-TAC-TOE GAME")
print("Do you want to play (y/n)? ")
start_game = input("").lower()

if start_game == "y":
    game = True
else:
    game = False

while game:
    board = " 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 "

    player1 = input("Who will be player one? ")
    print(f"{player1} will be \'O\'")
    player2 = input("Who will be player two? ")
    print(f"{player2} will be \'X\'")

    plyr1_symbol = "O"
    plyr2_symbol = "X"

    while True:

        print(board)
        while True:
            location = str(input(f"{player1}\'s move, choose a number: "))
            if (location != (plyr1_symbol or plyr2_symbol or  " ")):
                board = board.replace(location, plyr1_symbol)
                break
            else: 
                print("That location is already taken. Try another one.")

        if checker(board, player1, plyr1_symbol) == False:
            break
        elif tieChecker(board) == False:
            break

        print(board)
        while True:
            location = str(input(f"{player2}\'s move, choose a number: "))
            if (location != plyr1_symbol or plyr2_symbol or " "):
                board = board.replace(location, plyr2_symbol)
                break
            else: 
                print("That location is already taken. Try another one.")
        
        if checker(board, player2, plyr2_symbol) == False:
            break
        elif tieChecker(board) == False:
            break

    print("Do you want to play again (y/n)? ")
    start_game = input("").lower()

    if start_game == "y":
        game = True
    else:
        game = False