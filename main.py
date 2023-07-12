import chess


print("hello world :(")

def score(board):
    return 1

def search(board, depth):

    if depth == 0: return score(board)

    for move in board.legal_moves:
        newBoard = board
        newBoard.push(move)
        search(newBoard, depth-1)

print(search(chess.Board(),2))