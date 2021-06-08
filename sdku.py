import pygame
import pygame.freetype
import sys
import numpy as np
import threading
import time

screen_width = 451
screen_height = 451
selected_tile = (0, 0)
grid = [[4, -1, 5, -1, 2, -1, -1, -1, -1],
        [-1, -1, -1, 7, 5, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 4, -1, 3],
        [-1, 2, -1, -1, -1, 8, -1, -1, 6],
        [-1, -1, -1, -1, -1, -1, 7, -1, 1],
        [-1, 8, -1, -1, 9, -1, -1, -1, -1],
        [-1, -1, 3, 2, 7, -1, -1, -1, -1],
        [-1, -1, 1, -1, -1, -1, 6, 9, -1],
        [-1, -1, 7, 6, -1, -1, -1, 1, -1]]

hard = [[False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False]]


def changelast(x, y):
    x -= 1
    if x < 0:
        x = 8
        y -= 1
    if y < 0:
        sys.exit(0)
    while hard[y][x]:
        x -= 1
        if x < 0:
            x = 8
            y -= 1
        if y < 0:
            sys.exit(0)
    autosolve_from(x, y, grid[y][x] + 1)


def autosolve_from(x_start, y_start, starter=1):
    for y, line in enumerate(grid):
        for x, el in enumerate(line):
            if (y == y_start and x >= x_start) or (y > y_start):
                if not hard[y][x]:
                    if starter > 9:
                        grid[y][x] = -1
                        changelast(x, y)
                        return
                    if grid[y][x] == -1:
                        grid[y][x] = 1
                    for i in range(starter, 10):
                        grid[y][x] = i
                        # time.sleep(0.005)
                        # refresh()
                        if validate():
                            break
                        elif i >= 9:
                            grid[y][x] = -1
                            changelast(x, y)
                            return
                    starter = 1


def validate():
    for line in grid:
        seen = []
        for el in line:
            if el in seen and not el == -1:
                # panic
                return False
            seen.append(el)
    for x in range(len(grid)):
        seen = []
        for y in range(len(grid)):
            if grid[y][x] in seen and not grid[y][x] == -1:
                # panic
                return False
            seen.append(grid[y][x])

    tmp = []
    for el in grid[0:3]:
        tmp.append(el[:3])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[3:6]:
        tmp.append(el[:3])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[6:]:
        tmp.append(el[:3])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[0:3]:
        tmp.append(el[3:6])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[3:6]:
        tmp.append(el[3:6])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[6:9]:
        tmp.append(el[3:6])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[0:3]:
        tmp.append(el[6:9])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[3:6]:
        tmp.append(el[6:9])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    tmp = []
    for el in grid[6:9]:
        tmp.append(el[6:9])
    tmp = np.array(tmp)
    tmp = tmp.ravel()
    tmp = list(tmp)
    seen = []
    for el in tmp:
        if el in seen and not el == -1:
            # panic
            return False
        seen.append(el)

    return True


def refresh():
    global selected_tile, window
    window.fill((0, 0, 0))

    # grid
    for x in range(0, 451, 50):
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, 450))
        pygame.draw.line(window, (255, 255, 255), (0, x), (450, x))
    for x in range(0, 451, 150):
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, 450), 3)
        pygame.draw.line(window, (255, 255, 255), (0, x), (450, x), 3)

    for y, line in enumerate(grid):
        for x, el in enumerate(line):
            if hard[y][x]:
                basefont.render_to(window, (15 + x * 50, 15 + y * 50), str(grid[y][x]), (255, 0, 0))
            else:
                if not grid[y][x] == -1:
                    basefont.render_to(window, (15 + x * 50, 15 + y * 50), str(grid[y][x]), (255, 255, 255))
    pygame.display.flip()


def main():
    global window, selected_tile
    for i, line in enumerate(hard):
        for j, el in enumerate(line):
            if not grid[i][j] == -1:
                hard[i][j] = True
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # onclick
                x, y = pygame.mouse.get_pos()
                x = int(x / 50)
                y = int(y / 50)
                selected_tile = (x, y)
                print(selected_tile)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    run = False
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    autosolve_from(0, 0)
                    # time.sleep(20)
                if event.key == pygame.K_1:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 1
                if event.key == pygame.K_2:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 2
                if event.key == pygame.K_3:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 3
                if event.key == pygame.K_4:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 4
                if event.key == pygame.K_5:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 5
                if event.key == pygame.K_6:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 6
                if event.key == pygame.K_7:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 7
                if event.key == pygame.K_8:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 8
                if event.key == pygame.K_9:
                    if not hard[selected_tile[1]][selected_tile[0]]:
                        grid[selected_tile[1]][selected_tile[0]] = 9
                if not validate():
                    print("erreur")
        refresh()


pygame.init()
basefont = pygame.freetype.Font('Roboto-Black.ttf', 30)
window = pygame.display.set_mode((screen_width, screen_height))
main()
