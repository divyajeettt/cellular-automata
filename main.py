import pygame
import starting_window as win


"""
The Priciple of Cellular Automata: The Game of Life
• every box is called a cell
• every cell can be:
    • BLACK, i.e. Alive
    • WHITE, i.e. Dead
• in the next generation:
    • any live cell with fewer than 2 live neighbours dies
    • any live cell with exactly 2 or 3 live neighbours surrvives
    • any live cell with more than 3 live neighbours dies
    • any dead cell with exactly 3 live neighbours becomes alive
"""


pygame.font.init()
win.main()


NUM = win.N
SIDE = 625           # side of the main window
CELL = SIDE / NUM    # side of each cell
SPEED = 250

WINDOW = pygame.display.set_mode((SIDE + 200, SIDE))
FPS = 60

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

FONT1 = pygame.font.SysFont("consolas", 27)
FONT2 = pygame.font.SysFont("consolas", 18, "bold")

CELLS = {
    (i, j): [pygame.Rect(CELL*i, CELL*j, CELL, CELL), WHITE]
    for i in range(NUM) for j in range(NUM)
}

pygame.display.set_caption("Cellular Automata: The Game of Life")


def message(*lines):
    draw_lines()
    text = [FONT2.render(msg, 1, WHITE) for msg in lines]
    for i in range(3):
        for j in range(len(lines)):
            WINDOW.blit(text[j], (630, 20*j+200))
        pygame.display.update()
        pygame.time.delay(500)
        if i == 2 and "Gen" in lines[1]:
            continue
        pygame.draw.rect(WINDOW, BLACK, (630, 200, 200, 100))
        pygame.display.update()
        pygame.time.delay(500)


def draw_lines():
    for i in range(NUM + 1):
        x = CELL*i - 1
        pygame.draw.line(WINDOW, GRAY, (x, 0), (x, SIDE), 2)
        pygame.draw.line(WINDOW, GRAY, (0, x), (SIDE, x), 2)


def select_cells(x, y):
    cell, color = CELLS[x, y]
    color = BLACK if color == WHITE else WHITE
    CELLS[x, y] = [cell, color]
    pygame.draw.rect(WINDOW, color, cell)


def get_neighbours(x, y):
    # return a list of moore-neighbours of given cell at index (x, y)
    # x  x  x
    # x  C  x
    # x  x  x

    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            try:
                neighbours.append(CELLS[x+i, y+j])
            except KeyError:
                continue
    return neighbours


def update_cells(gen):
    pygame.time.delay(SPEED)

    change = []
    for ((i, j), (cell, color)) in CELLS.items():
        neighbours = get_neighbours(i, j)

        live = dead = 0
        for _, status in neighbours:
            if status == WHITE:
                dead += 1
            else:
                live += 1

        if color == WHITE and live == 3:
            change.append((i, j))
        elif color == BLACK and live not in {2, 3}:
            change.append((i, j))

    for x, y in change:
        select_cells(x, y)


def update_generation(gen):
    pygame.draw.rect(WINDOW, BLACK, (630, 595, 200, 30))
    WINDOW.blit(FONT2.render(str(gen), 1, WHITE), (635, 600))


def reset():
    pygame.draw.rect(WINDOW, BLACK, (630, 200, 200, 100))
    pygame.display.update()
    update_generation(0)
    for i in range(NUM):
        for j in range(NUM):
            cell, color = CELLS[i, j]
            if color != WHITE:
                CELLS[i, j][1] = WHITE
                pygame.draw.rect(WINDOW, WHITE, cell)


def main():
    GENERATION = 0

    pygame.draw.rect(WINDOW, WHITE, (0, 0, SIDE, SIDE))

    texts = ("START", "PAUSE", "RESET")
    for i, text in enumerate(texts):
        WINDOW.blit(FONT1.render(text.center(14), 1, WHITE), (625, 52*i+11))
        pygame.draw.rect(WINDOW, WHITE, (625, 50*(i+1), 200, 3))

    WINDOW.blit(FONT2.render("Generation:", 1, WHITE), (635, 565))
    WINDOW.blit(FONT2.render(str(GENERATION), 1, WHITE), (635, 600))
    pygame.draw.rect(WINDOW, WHITE, (625, 590, 200, 3))

    clock = pygame.time.Clock()

    RUNNING = False
    RUN = True
    while RUN:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 1:
                    continue

                x, y = event.pos

                if not RUNNING:
                    if x <= 625:
                        select_cells((x // CELL), (y // CELL))

                    elif y < 63:
                        RUNNING = True

                    elif 115 < y < 167:
                        GENERATION = 0
                        RUNNING = False
                        reset()

                elif x > 625 and 63 < y < 115:
                    RUNNING = False

        if RUNNING:
            if GENERATION == 0:
                for cell, color in CELLS.values():
                    if color == BLACK:
                        break
                else:
                    message("Select at least", "one cell to start")
                    RUNNING = False

        if RUNNING:
            update_cells(GENERATION)
            pygame.display.update()

            GENERATION += 1
            update_generation(GENERATION)

            for cell, color in CELLS.values():
                if color == BLACK:
                    break
            else:
                if GENERATION > 0:
                    message("The Game of Life", f"ended at Gen: {GENERATION}")
                    GENERATION = 0
                    RUNNING = False
                    reset()

        draw_lines()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()