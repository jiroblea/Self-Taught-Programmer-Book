# I don't know if this will be a tic-tac-toe game

board = " 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 "
print(board)


player_symbol = "O"

location = str(input("Your move, choose a number: "))

board = board.replace(location, player_symbol)

print(board)