print(hello world)
board = []
player = "X"

#Copy your functions from the previous activities here:
def print_board():
    print('\t0\t1\t2')
    count = 0
    for row in board:
        print()
        text=str(count) + '\t'
        for col in row:
            text+= str(col) +'\t'
        print(text)
        count += 1
        
def is_valid_move(row, col):
    if row < 0 or row >2 or col < 0 or col >2:
        return False
    return board[row][col] == '-'

def place_player(player, row, col):
    board[row][col] = player
    print()
    print_board()
    
def take_turn(player):
        print()
        print(player,'s turn')
        while True:
            num_row = int(input('Enter a row '))
            num_col = int(input('Enter a col '))
            if is_valid_move(num_row, num_col) == False:
                print('Please enter a valid move')
            else:
                 place_player(player, num_row, num_col)    
                 break
                   
def check_row_win(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False
    
def check_col_win(player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False
    
def check_diag_win(player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False
    
def check_win(player):
     return check_col_win(player) or check_row_win(player) or check_diag_win(player)

def check_tie():
    if "-" in board[0] or "-" in board[1] or "-" in board[2]:
        return False
    return not check_win("X") and not check_win("O")


def check_results():
    if check_win("X"):
        print("X wins!")
    elif check_win("O"):
        print("O wins!")
    else:
        print("It's a tie")

def check_results():
    if check_win("X"):
        print("X wins!")
    elif check_win("O"):
        print("O wins!")
    else:
        print("It's a tie")    

#start
for row in range(3):
    board.append(['-','-','-'])
print("\t\tWelcome to Tic Tac Toe!")
print_board()

while(not check_win("X") and not check_win("O") and not check_tie()):
    take_turn(player)
    if player == "X":
        player = "O"
    else:
        player = "X"
       
check_results()
