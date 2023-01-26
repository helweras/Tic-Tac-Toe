import tkinter as tk
from random import choice

x = 'X'
o = '@'
human_ = None
computer_ = None
game_board = ['_'] * 9


def win_(board):
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
            return True
    return False or len(true_step) == 0


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


count = 0


def step_computer(computer, human, board: list):
    board_copy = board_work(board)
    true_steps = [i for i in board_copy if str(i).isdigit()]
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
        if board_copy.count(human) == 2:
            flag = [i for i in preferred_steps[2] if board_copy[i] == human]
            if len(flag) == 2:
                track = list(filter(lambda st: st == 1 or st == 7, flag))
                if track:
                    return track[0]
        return False

    def trap_Phill():
        flag_diag = False
        flag_bock = False
        if board_copy.count(human) == 2:
            for ind in preferred_steps[1]:
                if board_copy[ind] == human:
                    flag_diag = True
                    break
            for ind1 in preferred_steps[2]:
                if board_copy[ind1] == human:
                    flag_bock = True
                    break
        return flag_bock and flag_diag

    flag_trap_2 = trap_2()
    flag_trap_Phill = trap_Phill()
    for _win in win_comb:
        count_comp = _win.count(computer)
        if count_comp == 2:
            for step in _win:
                if step in true_steps:
                    board[step] = computer
                    dick[step]['text'] = computer
                    dick[step]['state'] = tk.DISABLED
                    print('win')
                    return
    for deff in win_comb:
        count_human = deff.count(human)
        if count_human == 2:
            for step in deff:
                if step in true_steps:
                    board[step] = computer
                    dick[step]['text'] = computer
                    dick[step]['state'] = tk.DISABLED
                    print('def')
                    return
        else:
            continue
    if trap_1:
        step = choice(preferred_steps[2])
        board[step] = computer
        dick[step]['text'] = computer
        dick[step]['state'] = tk.DISABLED
        print('trap1')
        return
    if flag_trap_2:
        step = choice(def_trap_2[flag_trap_2])
        board[step] = computer
        dick[step]['text'] = computer
        dick[step]['state'] = tk.DISABLED
        print('trap2')
        return
    if flag_trap_Phill:
        diag = ((board_copy[0], board_copy[4], board_copy[8]),
                (board_copy[2], board_copy[4], board_copy[6]))
        step = None
        for i in diag:
            lst = [j for j in i if str(j).isdigit()]
            if len(lst) == 1:
                step = lst[0]
        print(f'step = {step}')
        board[step] = computer
        dick[step]['text'] = computer
        dick[step]['state'] = tk.DISABLED
        return

    for i in preferred_steps:
        tmp_step = [j for j in i if j in true_steps]
        if tmp_step:
            step = choice(tmp_step)
            board[step] = computer
            dick[step]['text'] = computer
            dick[step]['state'] = tk.DISABLED
            print('prefer')
            return board
        else:
            continue


def first_step1():
    global human_
    global computer_
    for i in dick:
        dick[i]['state'] = tk.NORMAL
    human_ = x
    computer_ = o

    btn_hum['state'] = tk.DISABLED
    btn_comp['state'] = tk.DISABLED


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
    index_win_comb = {0: (0, 1, 2), 1: (3, 4, 5), 2: (6, 7, 8),
                      3: (0, 3, 6), 4: (1, 4, 7), 5: (2, 5, 8),
                      6: (0, 4, 8), 7: (2, 4, 6)}
    for ind, i in enumerate(win_comb):
        count_comp = i.count(computer)
        count_human = i.count(human)
        if count_human == 3:
            return index_win_comb[ind]
        elif count_comp == 3:
            return index_win_comb[ind]
    return tuple(range(9))


def first_step2():
    global human_
    global computer_
    for i in dick:
        dick[i]['state'] = tk.NORMAL
    human_ = o
    computer_ = x
    step_computer(computer_, human_, game_board)
    btn_hum['state'] = tk.DISABLED
    btn_comp['state'] = tk.DISABLED


def change_board(borad, index, human):
    borad[index] = human
    dick[index]['text'] = human
    dick[index]['state'] = tk.DISABLED
    win1 = win_(game_board)
    if not win1:
        step_computer(computer_, human_, game_board)
        if not win_(game_board):
            return borad
        else:
            ind = who_win(game_board, computer_, human_)
            for i in dick:
                dick[i]['state'] = tk.DISABLED
            for num in ind:
                dick[num]['background'] = 'red'
                dick[num]['state'] = tk.DISABLED

    else:
        ind = who_win(game_board, computer_, human_)
        for i in dick:
            dick[i]['state'] = tk.DISABLED
        for num in ind:
            dick[num]['background'] = 'red'
            dick[num]['state'] = tk.DISABLED


win = tk.Tk()

win.geometry('400x400+300+200')
win.title('game')

btn1 = tk.Button(win, command=lambda: change_board(game_board, 0, human_), state=tk.DISABLED)
btn2 = tk.Button(win, command=lambda: change_board(game_board, 1, human_), state=tk.DISABLED)
btn3 = tk.Button(win, command=lambda: change_board(game_board, 2, human_), state=tk.DISABLED)
btn4 = tk.Button(win, command=lambda: change_board(game_board, 3, human_), state=tk.DISABLED)
btn5 = tk.Button(win, command=lambda: change_board(game_board, 4, human_), state=tk.DISABLED)
btn6 = tk.Button(win, command=lambda: change_board(game_board, 5, human_), state=tk.DISABLED)
btn7 = tk.Button(win, command=lambda: change_board(game_board, 6, human_), state=tk.DISABLED)
btn8 = tk.Button(win, command=lambda: change_board(game_board, 7, human_), state=tk.DISABLED)
btn9 = tk.Button(win, command=lambda: change_board(game_board, 8, human_), state=tk.DISABLED)
btn_hum = tk.Button(win, text='you', command=first_step1)
btn_comp = tk.Button(win, text='comp', command=first_step2)

dick = {0: btn1, 1: btn2, 2: btn3, 3: btn4, 4: btn5, 5: btn6, 6: btn7, 7: btn8, 8: btn9}

label = tk.Label(win, text='Кто пойдет первым?')

btn1.grid(row=0, column=0, stick='we')
btn2.grid(row=0, column=1, stick='we')
btn3.grid(row=0, column=2, stick='we')
btn4.grid(row=1, column=0, stick='we')
btn5.grid(row=1, column=1, stick='we')
btn6.grid(row=1, column=2, stick='we')
btn7.grid(row=2, column=0, stick='we')
btn8.grid(row=2, column=1, stick='we')
btn9.grid(row=2, column=2, stick='we')

label.grid(row=3, column=0, columnspan=3)
btn_hum.grid(row=4, column=0)
btn_comp.grid(row=4, column=2)

win.grid_columnconfigure(0, minsize=70)
win.grid_columnconfigure(1, minsize=70)
win.grid_columnconfigure(2, minsize=70)

win.mainloop()