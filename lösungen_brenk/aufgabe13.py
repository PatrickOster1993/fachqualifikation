tic_tac_toe = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
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

print("---------")
for i in range(3):
    print("|", end=" ")
    for j in range(3):
        print(tic_tac_toe[i][j], end=" ")
    print("|", end=" ")
    print()
print("---------")

while True:

    player1_x = int(input("Player 1 (X), please tell me the x-coordinate."))
    player1_y = int(input("Player 1 (X), please tell me the y-coordinate."))
    tic_tac_toe[player1_y][player1_x] = "X"
    
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(tic_tac_toe[i][j], end=" ")
        print("|", end=" ")
        print()
    print("---------")

    player_wins = False
    
    for i in range(len(winning_conditions)):

        for condition in winning_conditions[i]:
        
            x, y = condition
            
            if tic_tac_toe[x][y] == "X":
                player_wins = True
            else:
                player_wins = False

    if player_wins == True:
        print("Player 1 wins.")
        break

    player2_x = int(input("Player 2 (O), please tell me the x-coordinate."))
    player2_y = int(input("Player 2 (O), please tell me the y-coordinate."))
    tic_tac_toe[player2_y][player2_x] = "O"
    
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(tic_tac_toe[i][j], end=" ")
        print("|", end=" ")
        print()
    print("---------")

