board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]


# Функция для вывода доски
def print_board(board):
    print("  a b c d e f g h")
    for i in range(8):
        print(1 + i, end="|")
        for j in range(8):
            print(board[i][j], end=" ")
        print("|")
    print("  a b c d e f g h")


# Функция для выполнения хода
def make_move(board, start, end):
    piece = board[start[0]][start[1]]
    board[start[0]][start[1]] = '.'
    board[end[0]][end[1]] = piece


def is_valid_move(board, start, end):
    piece = board[start[0]][start[1]]
    if piece == '.':
        return False
    if board[end[0]][end[1]] == '.':
        if piece.isupper():
            if start[0] == 6 and start[0] - end[0] == 2 and start[1] == end[1]:
                return True
            elif start[0] - end[0] == 1 and start[1] == end[1]:
                return True
        else:
            if start[0] == 1 and end[0] - start[0] == 2 and start[1] == end[1]:
                return True
            elif end[0] - start[0] == 1 and start[1] == end[1]:
                return True
    if piece.isupper() != board[end[0]][end[1]].isupper():
        if piece == 'P' and start[0] - end[0] == 1 and abs(start[1] - end[1]) == 1:
            return True
        elif piece == 'p' and end[0] - start[0] == 1 and abs(start[1] - end[1]) == 1:
            return True

    if piece == '.':
        return False
    if board[end[0]][end[1]] == '.':
        if piece.isupper():
            if piece == 'R' or piece == 'r':
                if start[0] == end[0] or start[1] == end[1]:
                    if start[0] == end[0]:
                        for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                            if board[start[0]][i] != '.':
                                return False
                    else:
                        for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                            if board[i][start[1]] != '.':
                                return False
                    return True
            elif piece == 'N' or piece == 'n':
                if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                    return True
                elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                    return True
            elif piece == 'B' or piece == 'b':
                if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                    row_dir = 1 if end[0] - start[0] > 0 else -1
                    col_dir = 1 if end[1] - start[1] > 0 else -1
                    for i in range(1, abs(start[0] - end[0])):
                        if board[start[0] + (i * row_dir)][start[1] + (i * col_dir)] != '.':
                            return False
                    return True
        else:
            if piece == 'r' or piece == 'r':
                if start[0] == end[0] or start[1] == end[1]:
                    if start[0] == end[0]:
                        for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                            if board[start[0]][i] != '.':
                                return False
                    else:
                        for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                            if board[i][start[1]] != '.':
                                return False
                    return True
            elif piece == 'n' or piece == 'n':
                if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                    return True
                elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                    return True
            elif piece == 'b' or piece == 'b':
                if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                    row_dir = 1 if end[0] - start[0] > 0 else -1
                    col_dir = 1 if end[1] - start[1] > 0 else -1
                    for i in range(1, abs(start[0] - end[0])):
                        if board[start[0] + (i * row_dir)][start[1] + (i * col_dir)] != '.':
                            return False
                    return True
    if piece.isupper() != board[end[0]][end[1]].isupper():
        if piece == 'R' or piece == 'r':
            if start[0] == end[0] or start[1] == end[1]:
                if start[0] == end[0]:
                    for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                        if board[start[0]][i] != '.':
                            return False
                else:
                    for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                        if board[i][start[1]] != '.':
                            return False
                return True
        elif piece == 'N' or piece == 'n':
            if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                return True
            elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                return True
        elif piece == 'B' or piece == 'b':
            if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                row_dir = 1 if end[0] - start[0] > 0 else -1
                col_dir = 1 if end[1] - start[1] > 0 else -1
                for i in range(1, abs(start[0] - end[0])):
                    if board[start[0] + (i * row_dir)][start[1] + (i * col_dir)] != '.':
                        return False
                return True

    if piece.upper() != 'Q':
        return False

    if start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1]):
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                if board[start[0]][i] != '.':
                    return False
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                if board[i][start[1]] != '.':
                    return False
        else:
            row_dir = abs(start[0] - end[0])
            col_dir = abs(start[1] - end[1])
            for i in range(1, row_dir):
                if start[0] < end[0]:
                    row = start[0] + i
                else:
                    row = start[0] - i
                if start[1] < end[1]:
                    col = start[1] + i
                else:
                    col = start[1] - i
                if board[row][col] != '.':
                    return False
        return True

    piece = board[start[0]][start[1]]
    if piece.upper() != 'K':
        return False

    if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
        return True
    else:
        return False


# shindyaikin kirill
# Функция для игры
def play_game():
    turn = 0
    while True:
        print_board(board)
        if turn % 2 == 0:
            print("Ход белых:")
        else:
            print("Ход черных:")
        start = input("Введите начальное положение фигуры (например, e2): ")
        end = input("Введите конечное положение фигуры (например, e4): ")
        start_row = int(start[1]) - 1
        start_col = ord(start[0]) - ord('a')
        end_row = int(end[1]) - 1
        end_col = ord(end[0]) - ord('a')
        if is_valid_move(board, (start_row, start_col), (end_row, end_col)):
            make_move(board, (start_row, start_col), (end_row, end_col))
            turn += 1
        else:
            print("Некорректный ход. Попробуйте еще раз.")


# Запуск игры
play_game()
