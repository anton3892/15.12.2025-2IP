import random


def create_board():
    board = [[0] * 8 for _ in range(8)]
    for _ in range(10):
        while True:
            r, c = random.randint(0, 7), random.randint(0, 7)
            if board[r][c] != '*':
                board[r][c] = '*'
                for i in range(max(0, r - 1), min(8, r + 2)):
                    for j in range(max(0, c - 1), min(8, c + 2)):
                        if board[i][j] != '*': board[i][j] += 1
                break
    return board


def print_board(board, show=False):
    print('  0 1 2 3 4 5 6 7')
    for i in range(8):
        row = [str(board[i][j]) if board[i][j] != 0 or show else '.' if board[i][j] != '*' else '*' for j in range(8)]
        print(f'{i} {" ".join(row)}')


def reveal(board, visible, r, c):
    if board[r][c] == '*': return False
    visible[r][c] = str(board[r][c])
    if board[r][c] == 0:
        for i in range(max(0, r - 1), min(8, r + 2)):
            for j in range(max(0, c - 1), min(8, c + 2)):
                if visible[i][j] == '.': reveal(board, visible, i, j)
    return True


def main():
    board = create_board()
    visible = [['.'] * 8 for _ in range(8)]

    while True:
        print_board(visible)
        try:
            r, c = map(int, input('Введите строку и столбец: ').split())
            if not reveal(board, visible, r, c):
                print('Вы проиграли!')
                print_board(board, True)
                break
            if all(visible[i][j] != '.' or board[i][j] == '*' for i in range(8) for j in range(8)):
                print('Победа!')
                print_board(board, True)
                break
        except:
            print('Ошибка ввода')


if __name__ == '__main__':
    main()