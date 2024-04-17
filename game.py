
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# it for row
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    # it belongs to column
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # it for diagonal
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
       
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")

    for turn in range(9):
        print_board(board)
        print(f"Player {players[current_player]}'s turn")

        while True:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = players[current_player]
                break
            else:
                print("Invalid move. Try again.")

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        current_player = (current_player + 1) % 2
    else:
        print_board(board)
        print("It's a draw!")


if __name__ == "__main__":
    tic_tac_toe()