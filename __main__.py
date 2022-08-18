import argparse
import tui
from curses import wrapper


def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    return parser.parse_args()


def main(stdscr):
    args = parse_args()
    tui.draw_game(stdscr)
    
if __name__ == '__main__':
    wrapper(main)


