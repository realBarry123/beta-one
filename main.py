import chess, copy

print("hello world :(")

def score(board):
    return 1

def search(board, depth):

    if depth == 0: return (score(board), "")
    movesDict = {}
    for move in board.legal_moves:
        newBoard = copy.copy(board)
        newBoard.push(move)
        movesDict[search(newBoard, depth-1)[0]] = move
    if board.turn == True:
        return (max(movesDict), movesDict[max(movesDict)])
    return (min(movesDict), movesDict[min(movesDict)])


print(search(chess.Board(),2)[1])