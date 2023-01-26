from random import choice
x = 'X'
o = 'O'
human_ = None
computer_ = None


def instruction():
    board = [i for i in range(9)]
    print('''Номера клеток на игровом поле''')
    print()
    print(f'''    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}''')


def print_board(board):
    print(f'''{board[0]} | {board[1]} | {board[2]}
---------
{board[3]} | {board[4]} | {board[5]}
---------
{board[6]} | {board[7]} | {board[8]}''')


def first_step():
    global human_
    global computer_
    print('''Выбери кто будет ходить первым
1 - Ты
2 - Компьютер''')
    step = int(input())
    while step not in range(1, 3):
        step = int(input())
    if step == 1:
        human_, computer_ = x, o
    else:
        human_, computer_ = o, x
    return human_, computer_


def board_work(board: list):
    board_copy = []
    for i in range(9):
        if board[i] == x:
            board_copy.append(x)
        elif board[i] == o:
            board_copy.append(o)
        else:
            board_copy.append(i)
    return board_copy


def win(board):
    board_copy = board_work(board)
    win_comb = ((board_copy[0] == board_copy[1] == board_copy[2]),
                (board_copy[3] == board_copy[4] == board_copy[5]),
                (board_copy[6] == board_copy[7] == board_copy[8]),
                (board_copy[0] == board_copy[3] == board_copy[6]),
                (board_copy[1] == board_copy[4] == board_copy[7]),
                (board_copy[2] == board_copy[5] == board_copy[8]),
                (board_copy[0] == board_copy[4] == board_copy[8]),
                (board_copy[2] == board_copy[4] == board_copy[6]))
    true_step = [i for i in board_copy if i not in (x, o)]
    for i in win_comb:
        if i:
            return i
    return False or not true_step


def who_first():
    return human_ == x


def step_human(human, board):
    board_copy = board_work(board)
    true_step = [i for i in board_copy if i not in (x, o)]
    step = int(input('Ведите номер свободного поля '))
    while step not in true_step:
        print(*true_step)
        step = int(input('Ведите номер свободного поля '))
    board[step] = human
    return board


def step_computer(computer, human, board: list):
    board_copy = board_work(board)
    true_steps = [i for i in board_copy if i not in (x, o)]
    win_comb = ((board_copy[0], board_copy[1], board_copy[2]),
                (board_copy[3], board_copy[4], board_copy[5]),
                (board_copy[6], board_copy[7], board_copy[8]),
                (board_copy[0], board_copy[3], board_copy[6]),
                (board_copy[1], board_copy[4], board_copy[7]),
                (board_copy[2], board_copy[5], board_copy[8]),
                (board_copy[0], board_copy[4], board_copy[8]),
                (board_copy[2], board_copy[4], board_copy[6]))
    preferred_steps = ([4], [0, 8, 2, 6], [1, 3, 5, 7])
    def_trap_2 = {1: [0, 2], 7: [6, 8]}
    trap_1 = ((board_copy[0] == board_copy[8] == human) or (board_copy[2] == board_copy[6] == human)
              and board_copy.count(human) == 2)

    def trap_2():
        flag = [i for i in preferred_steps[2] if board_copy[i] == human]
        if len(flag) == 2:
            track = list(filter(lambda st: st == 1 or st == 7, flag))
            return track[0]
        return False
    flag_trap_2 = trap_2()
    for _win in win_comb:
        count_comp = _win.count(computer)
        if count_comp == 2:
            for step in _win:
                if step in true_steps:
                    board[step] = computer
                    return
                else:
                    continue
    for deff in win_comb:
        count_human = deff.count(human)
        if count_human == 2:
            for step in deff:
                if step in true_steps:
                    board[step] = computer
                    return
    if trap_1 and len(true_steps) > 1:
        step = choice(preferred_steps[2])
        board[step] = computer
        return
    if flag_trap_2 and len(true_steps) > 1:
        step = choice(def_trap_2[flag_trap_2])
        board[step] = computer
        return
    for i in preferred_steps:
        tmp_step = [j for j in i if j in true_steps]
        if tmp_step:
            step = choice(tmp_step)
            board[step] = computer
            return board
        else:
            continue


def who_win(board: list, computer, human):
    board_copy = board_work(board)
    win_comb = ((board_copy[0], board_copy[1], board_copy[2]),
                (board_copy[3], board_copy[4], board_copy[5]),
                (board_copy[6], board_copy[7], board_copy[8]),
                (board_copy[0], board_copy[3], board_copy[6]),
                (board_copy[1], board_copy[4], board_copy[7]),
                (board_copy[2], board_copy[5], board_copy[8]),
                (board_copy[0], board_copy[4], board_copy[8]),
                (board_copy[2], board_copy[4], board_copy[6]))
    for i in win_comb:
        count_comp = i.count(computer)
        count_human = i.count(human)
        if count_human == 3:
            print(f'Winner is human. He is {i[0]}')
            return
        elif count_comp == 3:
            print(f'Winner is computer. He is {i[0]}')
            return
    return print('Not win')


def game_human_step_first():
    print_board(game_board)
    print()
    win(game_board)
    while not win(game_board):
        step_human(human_, game_board)
        win(game_board)
        print_board(game_board)
        if win(game_board):
            break
        print()
        step_computer(computer_, human_, game_board)
        win(game_board)
        print_board(game_board)
        if win(game_board):
            break
        print()
    print('-----------------------')
    who_win(game_board, computer_, human_)


def game_computer_step_first():
    print()
    win(game_board)
    while not win(game_board):
        step_computer(computer_, human_, game_board)
        win(game_board)
        print_board(game_board)
        if win(game_board):
            break
        print()
        step_human(human_, game_board)
        win(game_board)
        print_board(game_board)
        if win(game_board):
            break
        print()
    print('----------------------')
    who_win(game_board, computer_, human_)


def main(func):
    if func:
        game_human_step_first()
    else:
        game_computer_step_first()


game_board = ['_']*9
# #Основня часть игры
instruction()
first_step()
main(who_first())
input()