import curses
import time
import ui

def main_menu(stdscr: curses.window):
    ui.main_menu(stdscr)
    
    # curses.curs_set(0)
    # stdscr.clear()

    # menu_options = ["1) Print hello", "2) Clock", "3) Exit"]
    # current_option = 0

    # while True:
    #     stdscr.clear()
    #     for idx, option in enumerate(menu_options):
    #         if idx == current_option:
    #             stdscr.addstr(idx, 0, option, curses.A_REVERSE)
    #         else:
    #             stdscr.addstr(idx, 0, option)
    
    #     stdscr.refresh()
    #     key = stdscr.getch()

    #     if key == curses.KEY_UP and current_option > 0:
    #         current_option -= 1
    #     elif key == curses.KEY_DOWN and current_option < len(menu_options) - 1:
    #         current_option += 1
    #     elif key == curses.KEY_ENTER or key in [10, 13]:
    #         if current_option == 0:
    #             message_window(stdscr, "Hello!")
    #         elif current_option == 1:
    #             time_window(stdscr)
    #         elif current_option == 2:
    #             quit()
        
def message_window(stdscr: curses.window, message):
    stdscr.clear()
    stdscr.addstr(0, 0, message)
    stdscr.addstr(1, 0, "Press any key to return the main menu")
    stdscr.refresh()
    stdscr.getch()

def time_window(stdscr: curses.window):
    stdscr.clear()
    stdscr.addstr(0, 0, "Current Time:")
    stdscr.refresh()

    stdscr.timeout(100)

    while True:
        current_time = time.strftime("%H:%M:%S")
        stdscr.addstr(1, 0, current_time)
        stdscr.refresh()
        time.sleep(1)

        if stdscr.getch() != -1:
            break

if __name__ == "__main__":
    curses.wrapper(main_menu)
