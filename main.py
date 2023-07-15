# ShallowMind BetaOne

import chess, copy, math

print("hello world :(")
pieceScores = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9}
positions_evaluated = 0

def score(board):
    finalScore = 0
    pieces = str(board)
    for i in pieceScores:
        finalScore += (pieces.count(i.lower())*pieceScores[i.lower()])
    for i in pieceScores:
        finalScore -= (pieces.count(i)*pieceScores[i])
    if board.turn:
        finalScore += len(list(board.legal_moves))/10
    else:
        finalScore -= len(list(board.legal_moves))/10
    return finalScore

def search(board, depth, isWhite):
    global positions_evaluated
    positions_evaluated += 1
    if depth == 0: return (score(board), "")  # return "n" as well as a move?
    if board.is_checkmate():
        if board.turn == isWhite: return (-math.inf, "n")  # "n" signifies end of game or no moves
        return (math.inf, "n")  # add special case checking for "n" as returned move
    movesDict = {}
    for move in board.legal_moves:  # keep in mind that move represents a Move object and not a string
        newBoard = copy.copy(board)
        newBoard.push(move)
        movesDict[search(newBoard, depth-1, isWhite)[0]] = move
    if board.turn == isWhite:  # replace isWhite with chess.WHITE?
        return (max(movesDict), movesDict[max(movesDict)])
    return (min(movesDict), movesDict[min(movesDict)])

chessBoard = chess.Board()

for i in range(20):
    print(positions_evaluated)
    positions_evaluated = 0
    nextMove = search(chessBoard,3,True)[1]
    chessBoard.push(nextMove)
    print(chessBoard)
    print(positions_evaluated)
    positions_evaluated = 0
    print(score(chessBoard))
    nextMove = search(chessBoard, 3, False)[1]
    chessBoard.push(nextMove)
    '''
    try:
        chessBoard.push(nextMove)
    except AttributeError:
        break
    '''
    print(chessBoard)
    print(score(chessBoard))