# ShallowMind BetaOne

import chess, copy, math

print("hello world :(")
pieceScores = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9}

def score(board):
    finalScore = 0
    pieces = str(board)
    for i in pieceScores:
        finalScore += (pieces.count(i.lower())*pieceScores[i.lower()])
    for i in pieceScores:
        finalScore -= (pieces.count(i)*pieceScores[i])
    finalScore += len(list(board.legal_moves))
    return finalScore

def search(board, depth, isWhite):

    if depth == 0: return (score(board), "")
    if board.is_checkmate():
        if board.turn == isWhite: return (-math.inf, "n")
        return (math.inf, "n")
    movesDict = {}
    for move in board.legal_moves:
        newBoard = copy.copy(board)
        newBoard.push(move)
        movesDict[search(newBoard, depth-1, isWhite)[0]] = move
    if board.turn == isWhite:
        return (max(movesDict), movesDict[max(movesDict)])
    return (min(movesDict), movesDict[min(movesDict)])

chessBoard = chess.Board()

for i in range(5):
    nextMove = search(chessBoard,2,True)[1]
    chessBoard.push(nextMove)
    print(chessBoard)
    print(score(chessBoard))
    nextMove = search(chessBoard, 2, False)[1]
    chessBoard.push(nextMove)
    print(chessBoard)
    print(score(chessBoard))