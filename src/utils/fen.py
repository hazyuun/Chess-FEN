import numpy as np


def FEN_from_board(board, delim='/'):
    FEN = ""
    empty_count = 0
    for line in board:
        for cell in line:
            if cell == '.':
                empty_count += 1
                continue

            if empty_count != 0:
                FEN += str(empty_count)
                empty_count = 0

            FEN += cell
        if empty_count != 0:
            FEN += str(empty_count)
            empty_count = 0

        FEN += delim
    return FEN[:-1]


def board_from_FEN(FEN, delim='/'):
    board = []
    for c in FEN:
        if c == delim:
            continue
        if c in "1234567890":
            board.extend(['.' for i in range(int(c))])
        else:
            board.append(c)
    board = np.array(board)
    return board.reshape(8, 8)


def FEN_get_piece(x, y, FEN, FEN_delim='/'):
    board = board_from_FEN(FEN, delim=FEN_delim)
    return board[y, x]
