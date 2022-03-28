def tic_tac_toe_winner(board: str):
    b = board.lower()
    row_1 = b[:3]
    row_2 = b[3:6]
    row_3 = b[6:]

    column_1 = row_1[0] + row_2[0] + row_3[0]
    column_2 = row_1[1] + row_2[1] + row_3[1]
    column_3 = row_1[2] + row_2[2] + row_2[2]

    diagonal_1 = row_1[0] + row_2[1] + row_3[2]
    diagonal_2 = row_1[2] + row_2[1] + row_3[0]

    rows = [row_1, row_2, row_3]
    columns = [column_1, column_2, column_3]
    diagonals = [diagonal_1, diagonal_2]

    for row in rows:
        if row == "xxx":
            return "x"
        elif row == "ooo":
            return "o"
    for column in columns:
        if column == "xxx":
            return "x"
        elif column == "ooo":
            return "o"
    for diagonal in diagonals:
        if diagonal == "xxx":
            return "x"
        elif diagonal == "ooo":
            return "o"
    return None


if __name__ == '__main__':
    test_cases = {
        'XO  X O X': 'x',
        'OX  O X O': 'o',
        'XXOOXXXOO': None,
        'xxx o o  ': 'x',
        'x  ooo x ': 'o',
        'xo x  xo ': 'x',
        ' xo xo  o': 'o',
        'xo ox   x': 'x',
        'x oxo ox ': 'o',
        'xx   oo  ': None,
        '         ': None,
    }

    for board, expectation in test_cases.items():
        response = tic_tac_toe_winner(board)
        assert response == expectation, f'Expected = {expectation}, got = {response}'
