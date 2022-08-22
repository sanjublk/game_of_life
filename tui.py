import curses
import time

import logic



def display_help(stdscr):
    k = 0
    stdscr.clear()
    while k != ord('q'):
        stdscr.addstr(0, 0, "help menu: 'q' go back")
        stdscr.addstr(1, 0, "'h', 'j', 'k', 'l' : left, down, up, right")
        stdscr.addstr(2, 0, "'SPACE' : make cells alive/dead")
        stdscr.addstr(3, 0, "'ENTER' : start simulating generations")
        stdscr.addstr(4, 0, "'c' to make all cells dead")
        stdscr.refresh()
        k = stdscr.getch()

def draw_at_mid(stdscr, sentence, x_pos):
    y_max = curses.COLS
    y_begining = (y_max // 2) - (len(sentence) // 2)
    stdscr.addstr(x_pos, y_begining,  sentence)
    stdscr.refresh()

def welcome_screen(stdscr):
    k = 0
    while k == 0:
        stdscr.clear()
        draw_at_mid(stdscr, "Welcome to Game of Life", curses.LINES//2)
        draw_at_mid(stdscr, 'Press any key to continue', curses.LINES//2 + 1)
        k = stdscr.getch()

def display_matrix(stdscr, matrix):
    i = 0
    buffer = []
    stdscr.clear()
    for row in matrix:
        for col in row:
            if col:
                buffer.append('✺')
            else:
                buffer.append('•')
        stdscr.addstr(i, 0, ''.join(buffer))
        i += 1
        stdscr.move(i, 0)
        buffer = []


def simulate_generations(stdscr, generation_count, matrix,):
    i = 0
    while i < generation_count: 
        try:
            matrix[:] = logic.next_generation(matrix)
            display_matrix(stdscr, matrix)
            draw_dash_borad(stdscr, f'^C: stop | gen: {i + 1}')
            stdscr.refresh()
            time.sleep(.4)
            i += 1
        except KeyboardInterrupt:
            break
def draw_dash_borad(stdscr, sentence):
    x_bottom = curses.LINES
    y_begining = 0
    stdscr.addstr(x_bottom - 1, y_begining, sentence)

def draw_game(stdscr):
    matrix = logic.get_matrix(curses.LINES - 1, curses.COLS)
    stdscr.clear()
    welcome_screen(stdscr)
    k = 0
    curser_y = 0 
    curser_x = 0
    while k != ord('q'): # quits game
        stdscr.clear()
        if k == curses.KEY_DOWN or k == ord('j'): # curser down
            curser_y += 1
        if k == curses.KEY_UP or k == ord('k'): # curser up
            curser_y -= 1
        if k == curses.KEY_LEFT or k == ord('h'): # curser left
            curser_x -= 1
        if k == curses.KEY_RIGHT or k == ord('l'): # curser right
            curser_x += 1
        if k == ord(' '): # changes cell state
            matrix[curser_y][curser_x] = not matrix[curser_y][curser_x]
        if k == ord('c'): # clears matrix
            matrix = logic.get_matrix(curses.LINES - 1, curses.COLS)
        if k == 10: # starts simulation 
            simulate_generations(stdscr, 100, matrix)
            stdscr.clear()
        if k == 63:
            display_help(stdscr)


        if curser_x < 0:
            curser_x = curses.COLS - 1
        if curser_x > curses.COLS - 1:
            curser_x = 0
        if curser_y < 0:
            curser_y = curses.LINES - 2
        if curser_y > curses.LINES - 2:
            curser_y = 0

        display_matrix(stdscr, matrix)
        draw_dash_borad(stdscr, "q: quit | ?: help")
        stdscr.refresh()
        stdscr.move(curser_y, curser_x)
        k = stdscr.getch()
    
# def main():
#     curses.wrapper(draw_game)

# if __name__ == '__main__':
#     main()
