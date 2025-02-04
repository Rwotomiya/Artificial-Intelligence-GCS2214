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
    # ... (terminal state check code here) ...

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

# Example board visualization:
# Board positions are indexed as follows:
#  0 | 1 | 2
# -----------
#  3 | 4 | 5
# -----------
#  6 | 7 | 8

# Example of a board state:
#  X | O | X
# -----------
#  O | X |  
# -----------
#    | O |  

# get_possible_moves(board) would return the list of empty positions, e.g., [5, 6, 8]