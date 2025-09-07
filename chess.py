import chess

def score_board(board: chess.Board) -> int:
    """Return a simple evaluation of the board state."""
    if board.is_checkmate():
        return -9999 if board.turn == chess.WHITE else 9999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    score = 0
    for piece, val in values.items():
        score += len(board.pieces(piece, chess.WHITE)) * val
        score -= len(board.pieces(piece, chess.BLACK)) * val

    return score

def minimax_ab(board: chess.Board, depth: int, alpha: int, beta: int, maximize: bool) -> int:
    """Minimax algorithm with alpha-beta pruning."""
    if depth == 0 or board.is_game_over():
        return score_board(board)

    if maximize:
        best_val = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = minimax_ab(board, depth - 1, alpha, beta, False)
            board.pop()
            best_val = max(best_val, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break  
        return best_val
    else:
        best_val = float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = minimax_ab(board, depth - 1, alpha, beta, True)
            board.pop()
            best_val = min(best_val, value)
            beta = min(beta, value)
            if beta <= alpha:
                break  
        return best_val

def select_move(board: chess.Board, depth: int) -> chess.Move:
    """Choose the best move for the current board using minimax+alpha-beta."""
    best_choice = None
    best_eval = -float("inf")

    for move in board.legal_moves:
        board.push(move)
        move_val = minimax_ab(board, depth - 1, -float("inf"), float("inf"), False)
        board.pop()
        if move_val > best_eval:
            best_eval = move_val
            best_choice = move

    return best_choice

def run_game():
    board = chess.Board()
    print("Welcome to Chess AI with Minimax + Alpha-Beta!")
    print("Search depth = 3 by default.")
    print(board)

    side = input("Do you want to play as White (y/n)? ").strip().lower()
    player_is_white = (side == "y")

    while not board.is_game_over():
        if (board.turn == chess.WHITE and player_is_white) or (board.turn == chess.BLACK and not player_is_white):
            move = None
            while move not in board.legal_moves:
                move_str = input("Your move (in UCI, e.g. e2e4): ")
                try:
                    move = chess.Move.from_uci(move_str)
                except:
                    print("Invalid input, try again.")
                    continue
                if move not in board.legal_moves:
                    print("Illegal move, try again.")
            board.push(move)
            print("\nBoard after your move:")
            print(board)
        else:
            ai_move = select_move(board, depth=3)
            board.push(ai_move)
            print(f"\nAI plays: {ai_move}")
            print(board)

    print("\nGame Over! Result:", board.result())


if __name__ == "__main__":
    run_game()
