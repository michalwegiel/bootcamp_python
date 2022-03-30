def tic_tac_toe_winner(board: str):
    b = board.lower()
    if (b.count("x") - b.count("o"))**2 > 1:
        raise ValueError

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

    result = ""
    for row in rows:
        if row == "xxx":
            result += "x"
        elif row == "ooo":
            result += "o"
    for column in columns:
        if column == "xxx":
            result += "x"
        elif column == "ooo":
            result += "o"
    for diagonal in diagonals:
        if diagonal == "xxx":
            result += "x"
        elif diagonal == "ooo":
            result += "o"

    if len(result) > 1:
        raise ValueError

    return result if result != "" else None

