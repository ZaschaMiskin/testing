import pygame
import sys
import numpy as np

board = [[0 for i in range(3)] for j in range(3)]
board_size = 180
turn = 1
pygame.init()
window = pygame.display.set_mode((800, 600))
run = True
gamedone = False


def check():
    """
    checks board for winner
    :return: the winner if there is one
    """
    npboard = np.array(board)
    npboard = npboard.transpose()
    winner = 0

    for i in range(3):
        if (npboard[i] == np.array([1, 1, 1])).all():
            winner = 1
        if (npboard[0] == [2, 2, 2]).all():
            winner = 2
    for i in range(3):
        if (npboard[:, i] == [1, 1, 1]).all():
            winner = 1
        if (npboard[:, i] == [2, 2, 2]).all():
            winner = 2
    if (npboard.diagonal() == [1, 1, 1]).all():
        winner = 1
    if (npboard.diagonal() == [2, 2, 2]).all():
        winner = 2
    if (np.fliplr(npboard).diagonal() == [1, 1, 1]).all():
        winner = 1
    if (np.fliplr(npboard).diagonal() == [2, 2, 2]).all():
        winner = 2
    if winner != 0:
        print("player " + str(winner) + " wins")
        global gamedone
        gamedone = True


while run:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if int(x / board_size) > 2 or int(y / board_size) > 2:
                continue
            x_pos = int(x / board_size)
            y_pos = int(y / board_size)
            if board[x_pos][y_pos] == 0 and not gamedone:
                board[x_pos][y_pos] = turn
            if turn == 1:
                turn = 2
            else:
                turn = 1
            if not gamedone:
                check()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = [[0 for i in range(3)] for j in range(3)]
                gamedone = False
                turn = 1
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run = False
                sys.exit(0)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(window, (255, 0, 0), (board_size * i + 1, board_size * j + 1, board_size, board_size), 2)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                pygame.draw.line(window, (255, 0, 0), (board_size * i, board_size * j),
                                 (board_size * i + board_size, board_size * j + board_size))
                pygame.draw.line(window, (255, 0, 0), (board_size * i + board_size, board_size * j),
                                 (board_size * i, board_size * j + board_size))
            if board[i][j] == 2:
                pygame.draw.ellipse(window, (255, 0, 0), (
                    board_size * i + 1 + 10, board_size * j + 1 + 10, board_size - 20, board_size - 20), 2)

    pygame.display.flip()
