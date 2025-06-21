from operator import indexOf
from random import randrange


def display_board(board: list):
    brd = f"+-------+-------+-------+\n|       |       |       |\n|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n|       |       |       |\n+-------+-------+-------+"

    print(brd)


def enter_move(board: list):
    user_input: str = int(input("Enter your move: "))

    if user_input not in [1, 2, 3, 4, 6, 7, 8, 9]:
        print("Only numbers are allowed.")
        return None

    if user_input in board[0]:
        board[indexOf(board, board[0])][indexOf(board[0], user_input)] = "o"

    if user_input in board[1]:
        board[indexOf(board, board[1])][indexOf(board[1], user_input)] = "o"

    if user_input in board[2]:
        board[indexOf(board, board[2])][indexOf(board[2], user_input)] = "o"

    return board


def make_list_of_free_fields(board: list):

    new_board: list = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] not in ["o", "x"]:
                free_sqr: tuple = (row, col)
                new_board.append(free_sqr)

    return new_board


def victory_for(board: list, sign: str):

    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True

    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True

    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True

    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True

    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True

    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        if sign == "o":
            return True
        if sign == "x":
            return True


def draw_move(board: list):
    row = randrange(0, 3)
    col = randrange(0, 3)

    while True:
        row = randrange(0, 3)
        col = randrange(0, 3)

        if board[row][col] != "x" and board[row][col] != "o":
            board[row][col] = "x"
            break

    return board


matrix = [[1, 2, 3], [4, "x", 6], [7, 8, 9]]

while True:
    display_board(matrix)
    enter_move(matrix)

    if victory_for(matrix, "o"):
        display_board(matrix)
        print("You Won!")

        break

    draw_move(matrix)

    if victory_for(matrix, "x"):
        display_board(matrix)
        print("Computer Won!")

        break

    if len(make_list_of_free_fields(matrix)) == 0:
        display_board(matrix)
        print("Tie!!")

        break
