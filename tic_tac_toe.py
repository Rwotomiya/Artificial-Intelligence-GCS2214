import random

def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm to determine the best move for the AI.

    Parameters:
    board (list): The current state of the board.
    depth (int): The current depth of the recursion.
    is_maximizing (bool): True if the current move is for the maximizing player (AI), False otherwise.

    Returns:
    int: The best score for the current move.
    """

    # Check for terminal states (win, lose, draw) and return the corresponding score
    result = check_terminal_state(board)
    if result is not None:
        return result

    if is_maximizing:
        best_score = -float('inf')
        for move in get_possible_moves(board):
            # Make the move
            board[move] = "X"
            # Recursively call minimax to simulate the opponent's move
            score = minimax(board, depth + 1, False)
            # Undo the move
            board[move] = " "
            # Choose the maximum score
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_possible_moves(board):
            # Make the move
            board[move] = "O"
            # Recursively call minimax to simulate the opponent's move
            score = minimax(board, depth + 1, True)
            # Undo the move
            board[move] = " "
            # Choose the minimum score
            best_score = min(best_score, score)
        return best_score

def get_possible_moves(board):
    """
    Returns a list of indices representing empty positions on the board.

    Parameters:
    board (list): The current state of the board.

    Returns:
    list: A list of indices representing empty positions.
    """
    return [i for i in range(len(board)) if board[i] == " "]

def check_terminal_state(board):
    """
    Checks if the board is in a terminal state (win, lose, draw).

    Parameters:
    board (list): The current state of the board.

    Returns:
    int: 1 if the maximizing player (AI) wins, -1 if the minimizing player wins, 0 if it's a draw, None if the game is ongoing.
    """
    # Check rows, columns, and diagonals for a win
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return 1 if board[pos[0]] == "X" else -1

    # Check for a draw
    if " " not in board:
        return 0

    # Game is ongoing
    return None

def print_board(board):
    """
    Prints the current state of the board.

    Parameters:
    board (list): The current state of the board.
    """
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def get_best_move(board):
    """
    Determines the best move for the AI using the minimax algorithm.

    Parameters:
    board (list): The current state of the board.

    Returns:
    int: The index of the best move.
    """
    best_score = -float('inf')
    best_move = None
    for move in get_possible_moves(board):
        board[move] = "X"
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main():
    """
    Main function to run the two-player game.
    """
    board = [" "] * 9
    current_player = random.choice(["X", "O"])  # Randomly choose who starts
    print(f"{'AI' if current_player == 'X' else 'You'} will start the game.")

    while True:
        print_board(board)

        if current_player == "X":
            # AI's turn
            move = get_best_move(board)
            board[move] = "X"
            print(f"AI moves to position {move}")
        else:
            # User's turn
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Invalid move. Try again.")
                continue
            board[move] = "O"

        result = check_terminal_state(board)
        if result is not None:
            print_board(board)
            if result == 1:
                print("AI wins!")
            elif result == -1:
                print("You win!")
            else:
                print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
