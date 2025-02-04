import curses

screen = curses.initscr()

try:
    screen.border(0)
    screen.addstr(2, 2, "Hello World!")
    box1 = screen.subwin(20, 20, 5, 5)
    box1.box()
    screen.getch()

finally:
    curses.endwin()