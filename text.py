# Connect 4 game

# Create an empty game board
def create_board(rows, cols):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    return board

# Display the game board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * len(row) * 2)

# Check if a player has won
def check_win(board, player, row, col):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    for dr, dc in directions:
        count = 1
        for i in range(1, 4):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == player:
                count += 1
            else:
                break
        for i in range(1, 4):
            r, c = row - dr * i, col - dc * i
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == player:
                count += 1
            else:
                break
        if count >= 4:
            return True
    return False

# Main game loop
def connect_four():
    rows, cols = 6, 7
    board = create_board(rows, cols)
    current_player = 'X'

    while True:
        display_board(board)
        col = int(input(f'Player {current_player} , enter a column (0-{cols-1}): '))
        
        if col < 0 or col >= cols:
            print("Invalid input. Please enter a valid column.")
            continue
        
        for row in range(rows - 1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = current_player
                if check_win(board, current_player, row, col):
                    display_board(board)
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
                break

connect_four()
