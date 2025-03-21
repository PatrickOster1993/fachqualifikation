####### DATA #######
tic_tac_toe = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
    ]

winning_conditions = [
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],

    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],

    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]]
    ]

players = [
    ["player_1", "X"],
    ["player_2", "O"]
    ]

####### FUNCTIONS #######

def show_board():
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(tic_tac_toe[i][j], end=" ")
        print("|", end=" ")
        print()
    print("---------")

def move(player, sign):
    player_x = int(input(f"{player} ({sign}), please tell me the x-coordinate."))
    player_y = int(input(f"{player} ({sign}), please tell me the y-coordinate."))
    tic_tac_toe[player_y][player_x] = sign

def check_winning_conditions():
    win = False

    for i in range(len(winning_conditions)):
        for condition in winning_conditions[i]:
        
            x, y = condition
            
            if tic_tac_toe[x][y] == players[0][1] or tic_tac_toe[x][y] == players[1][1]:
                win = True
            else:
                win = False
    
    return win

def round(player, sign):
    move(player, sign)
    show_board()

    player_wins = check_winning_conditions()
    
    if player_wins == True:
        print(f"{player} wins.")
        return "win"
    else: 
        return None

####### PROGRAM #######

show_board()

while True:

    result = round(players[0][0], players[0][1])
    if result == "win":
        break

    result = round(players[1][0], players[1][1])
    if result == "win":
        break

