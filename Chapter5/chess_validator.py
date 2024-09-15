# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.

def isValidChessBoard(chessboard):
    wking = 0
    bking = 0
    wpawn = 0
    bpawn = 0
    wpieces = 0
    bpieces = 0
    for piece in chessboard.values():
        if piece[0] == 'w':
            wpieces += 1
        elif piece[0] == 'b':
            bpieces += 1
        if piece == 'wking':
            wking += 1
        elif piece == 'bking':
            bking += 1
        elif piece == 'wpawn':
            wpawn += 1
        elif piece == 'bpawn':
            bpawn += 1
    if wking != 1 or bking != 1:
        print('This is not a valid chessboard.')
        return False
    if wpawn > 8 or bpawn > 8:
        print('This is not a valid chessboard.')
        return False
    if wpieces > 16 or bpieces > 16:
        print('This is not a valid chessboard.')
        return False
    if len(chessboard.keys()) > 64:
        print('This is not a valid chessboard.')
        return False
    for space in chessboard.keys():
        if int(space[0]) > 8 or int(space[0]) < 1:
            print('This is not a valid chessboard.')
            return False
        # The interesting thing here is that ord() is not something we have learned yet, but it is a built-in function that returns the Unicode code point for a one-character string
        if ord(space[1]) > 104 or ord(space[1]) < 97:
            print('This is not a valid chessboard.')
    print('This is a valid chessboard.')
    return True

chessboard = { '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking' }

invalid_chessboard = { '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '9z': 'bpawn', '8a': 'wking' }

another_invalid_chessboard = {'2z': 'bpawn', '8a': 'wking', '1z': 'bpawn'}

isValidChessBoard(chessboard)
isValidChessBoard(invalid_chessboard)
isValidChessBoard(another_invalid_chessboard)

# This practice project was frustrating for the very simple mistakes that can come from making too many assumptions


