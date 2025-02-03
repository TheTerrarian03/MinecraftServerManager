import curses
import time

def main_menu(stdscr: curses.window):
    curses.curs_set(0)
    stdscr.clear()

    menu_options = ["Hello", "world"]
    current_option = 0

    while True:
        stdscr.clear()
        window_border(stdscr, 10, 4, 0, 0)

        for idx, option in enumerate(menu_options):
            if idx == current_option:
                stdscr.addstr(idx+1, 1, option, curses.A_REVERSE)
            else:
                stdscr.addstr(idx+1, 1, option)
    
        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(menu_options) - 1:
            current_option += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return

def window_border(stdscr: curses.window, width: int, height:int, x: int, y: int):
    # top border
    stdscr.addch(y, x, 'x');
    stdscr.addstr(y, x+1, "-"*(width-2))    
    stdscr.addch(y, x+width-1, 'x')

    # middle borders
    for i in range(height+1, height):
        stdscr.addch(y+i, x, '|')
        stdscr.addch(y+i, x+width+4, '|')

    # bottom border
    stdscr.addch(y+height-1, x, 'x');
    stdscr.addstr(y+height-1, x+1, "-"*(width-2))    
    stdscr.addch(y+height-1, x+width-1, 'x')